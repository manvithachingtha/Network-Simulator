# Network Simulator ( Lab)

## Overview
This project simulates basic networking concepts at the physical and data link layers. It allows you to create devices, hubs, and switches, and test simple communication protocols. The simulator is educational and does not transmit real data — it only demonstrates the logic of networking.

## Features
- End devices that can send and receive messages
- Hub that broadcasts to all connected devices
- Switch with MAC learning and forwarding
- Protocols: checksum, Stop-and-Wait, CSMA/CD

## Project Structure
network_simulator/
├── physical_layer.py
├── data_link.py
├── protocols.py
└── run_simulator.py   # main entry point

## How to Run
1. Install Python 3.8 or higher.
2. Navigate to the project folder.
3. Run:
   ```bash
   python run_simulator.py
