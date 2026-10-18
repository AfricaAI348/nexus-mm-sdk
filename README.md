# NEXUS-MM Python SDK

A physics-grounded world model for robot safety decisions. NEXUS-MM processes environmental telemetry, surface characteristics, and velocities to deliver ultra-low latency safety overrides.

[![PyPI version](https://shields.io)](https://pypi.org)
[![License](https://shields.io)](https://nexusmm.site/docs)

NEXUS-MM tells robots when to **go**, **slow down**, or **stop** based on real friction, gravity, and stability calculations rather than basic pattern matching.

## Installation

Install the official SDK wrapper via pip:

```bash
pip install nexus-mm-sdk
```

## Authentication

Get your API key starting with `nxk_` from your [NEXUS-MM Dashboard](https://nexusmm.site). Set it as an environment variable:

```bash
export NEXUS_API_KEY="nxk_your_key_here"
```

## Quick Start

```python
from nexus_mm_sdk import NexusRobot

# The client automatically loads NEXUS_API_KEY from your environment variables
robot = NexusRobot()

# Evaluate telemetry boundaries instantly
decision = robot.decide(
    action="move_forward", 
    surface="ice", 
    speed=0.8
)

print(f"Action: {decision.action}")       # Output: stop
print(f"Risk Score: {decision.risk}")     # Output: 0.75
print(f"Risk Level: {decision.risk_level}") # Output: critical
print(f"Confidence: {decision.confidence}") # Output: 0.92
```

## Advanced Usage (Obstacle Avoidance)

```python
decision = robot.decide(
    action="move_forward",
    surface="concrete",
    speed=1.2,
    distance_to_obstacle=1.1
)
print(decision.action) # Output: stop (due to critical proximity)
```

## Architecture
This open-source SDK serves as a secure, high-performance client interface. All core physical calculations, friction transformations, and proprietary world model inference algorithms are computed securely via the encrypted NEXUS-MM Cloud API engine.

* **Website & Live Workshop:** [https://nexusmm.site](https://nexusmm.site)
* **API Documentation:** [https://nexusmm.site/docs](https://nexusmm.site/docs)
* **Support Contact:** support@nexusmm.site
