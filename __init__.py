import os
import requests

class NexusDecision:
    def __init__(self, data: dict):
        self.action = data.get("action", "stop")
        self.risk = data.get("risk", 1.0)
        self.risk_level = data.get("risk_level", "critical")
        self.confidence = data.get("confidence", 0.0)
        self.surface = data.get("surface", "unknown")
        self.speed = data.get("speed", 0.0)

class NexusRobot:
    """
    Client interface wrapper for interacting safely with the 
    private proprietary NEXUS-MM physical evaluation servers.
    """
    def __init__(self, api_key: str = None, base_url: str = "https://api.nexusmm.site"):
        self.api_key = api_key or os.getenv("NEXUS_API_KEY")
        self.base_url = base_url.rstrip("/")
        
        if not self.api_key:
            raise ValueError(
                "NEXUS_API_KEY not found. Pass it to NexusRobot() or set it "
                "as an environment variable: export NEXUS_API_KEY='nxk_...'"
            )
            
        self.headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def decide(self, action: str, surface: str, speed: float, distance_to_obstacle: float = None) -> NexusDecision:
        """
        Pipes state parameters to the NEXUS core engine to evaluate physical system limits.
        """
        url = f"{self.base_url}/api/robot/decide"
        payload = {
            "action": action,
            "surface": surface,
            "speed": float(speed)
        }
        if distance_to_obstacle is not None:
            payload["distance_to_obstacle"] = float(distance_to_obstacle)

        try:
            response = requests.post(url, json=payload, headers=self.headers, timeout=1.5)
            if response.status_code == 200:
                return NexusDecision(response.json())
            elif response.status_code == 403:
                return NexusDecision({"action": "stop", "risk": 1.0, "risk_level": "critical", "error": "Plan limits exceeded or inactive API key"})
            else:
                return NexusDecision({"action": "stop", "risk": 1.0, "risk_level": "critical", "error": f"HTTP {response.status_code}"})
        except requests.RequestException:
            # Safe hardware default fallback loop if connection fails
            return NexusDecision({"action": "stop", "risk": 1.0, "risk_level": "critical", "error": "Hardware Network Timeout"})

    def health(self) -> dict:
        """Checks API reachability and software environment mapping engine versions."""
        try:
            # Hit base url to verify gateway activity status
            response = requests.get(f"{self.base_url}/api/robot/decide", headers=self.headers, timeout=2.0)
            return {"status": "connected" if response.status_code != 404 else "offline", "sdk_version": "8.1.1"}
        except requests.RequestException:
            return {"status": "offline", "sdk_version": "8.1.1"}
