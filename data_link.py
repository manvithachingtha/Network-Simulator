# data_link.py
class Switch:
    def __init__(self, label):
        self.label = label
        self.ports = {}
        self.forwarding_table = {}

    def attach(self, device, mac):
        self.ports[mac] = device
        device.link = self
        print(f"{device.label} connected to switch {self.label} with MAC {mac}")

    def receive(self, frame, src_mac):
        dest_mac, payload = frame
        # Learn source MAC
        self.forwarding_table[src_mac] = self.ports[src_mac]

        if dest_mac in self.forwarding_table:
            sender = self.ports[src_mac]
            receiver = self.forwarding_table[dest_mac]
            print(f"Switch {self.label} forwarding '{payload}' from {sender.label} ({src_mac}) to {receiver.label} ({dest_mac})")
            receiver.receive(payload, sender)
        else:
            sender = self.ports[src_mac]
            print(f"Switch {self.label} flooding '{payload}' (unknown destination {dest_mac})")
            for mac, dev in self.ports.items():
                if mac != src_mac:
                    dev.receive(payload, sender)
