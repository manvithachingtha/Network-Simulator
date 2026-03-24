from physical_layer import Device, Hub
from data_link import Switch
from protocols import SimpleChecksum, StopAndWaitProtocol, SlidingWindowProtocol, CSMA_CD

# --- End-to-End Devices ---
a = Device("A")
b = Device("B")
a.attach(b)
a.transmit("Hello B")

# --- Hub Topology ---
hub = Hub("CentralHub")
nodes = [Device(f"N{i}") for i in range(1, 6)]
for n in nodes:
    hub.attach(n)
nodes[0].transmit("Broadcast test")

# --- Switch Forwarding ---
sw = Switch("MainSwitch")
c = Device("C")
d = Device("D")
sw.attach(c, "00:11:22:01")
sw.attach(d, "00:11:22:02")

# Teach switch about D first
sw.receive(("00:11:22:01", "Learning frame"), "00:11:22:02")
sw.receive(("00:11:22:02", "Message via Switch"), "00:11:22:01")

# --- Protocols ---
print("\n--- Protocol Tests ---")

# Error Control
data = "TestMessage"
checksum = SimpleChecksum.generate(data)
print(f"Checksum generated for '{data}': {checksum}")
print("Checksum valid?", SimpleChecksum.validate(data, checksum))

# Flow Control (Stop-and-Wait)
proto = StopAndWaitProtocol()
proto.send(a, b, "Reliable delivery message")

# Flow Control (Sliding Window)
sliding = SlidingWindowProtocol()
sliding.send(c, d, ["Frame1", "Frame2", "Frame3"], window_size=2)

# Access Control (CSMA/CD)
csma = CSMA_CD()
group = [a, b, c, d]
csma.transmit(c, group, "Shared medium message")

# --- Domain Reporting ---
print("\n--- Domain Report ---")
print("Hub topology: 1 collision domain, 1 broadcast domain")
print("Switch topology: each port = separate collision domain, 1 broadcast domain")

