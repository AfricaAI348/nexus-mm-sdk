# NEXUS-MM

A physics-grounded world model for robot safety decisions.

NEXUS-MM tells robots when to **go**, **slow down**, or **stop** 
based on the surface they're on and their current speed.

## Install

\`\`\`bash
pip install nexus-mm-sdk
\`\`\`

## Quick Start

\`\`\`python
from nexus_sdk import NexusRobot

robot = NexusRobot()
d = robot.decide(action="move_forward", surface="ice", speed=0.8)

print(d.action)   # stop
print(d.risk)     # 0.95
\`\`\`

## What it does

- Accepts surface type and current speed
- Returns one action: `go`, `slow_down`, `stop`, or `caution`
- Returns a risk score (0.0 = safe, 1.0 = critical)
- Runs on edge hardware (Raspberry Pi class)

## Live Demo

https://nexusmm.site

## Documentation

https://nexusmm.site/docs

## License

Proprietary. SDK usage subject to Terms of Service.
