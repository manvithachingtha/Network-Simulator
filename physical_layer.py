# physical_layer.py
class Device:
    def __init__(self, label):
        self.label = label
        self.link = None

    def attach(self, other):
        self.link = other
        print(f"{self.label} attached to {other.label}")

    def transmit(self, message):
        if self.link:
            print(f"{self.label} transmitting: {message}")
            self.link.receive(message, self)

    def receive(self, message, source):
        print(f"{self.label} received from {source.label}: {message}")


class Hub:
    def __init__(self, label):
        self.label = label
        self.members = []

    def attach(self, device):
        self.members.append(device)
        device.link = self
        print(f"{device.label} joined hub {self.label}")

    def receive(self, message, source):
        print(f"Hub {self.label} broadcasting '{message}' from {source.label}")
        for d in self.members:
            if d != source:
                d.receive(message, source)
