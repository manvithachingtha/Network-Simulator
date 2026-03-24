# protocols.py
class SimpleChecksum:
    @staticmethod
    def generate(data):
        return sum(ord(ch) for ch in data) % 256

    @staticmethod
    def validate(data, checksum):
        return SimpleChecksum.generate(data) == checksum


class StopAndWaitProtocol:
    def send(self, sender, receiver, message):
        print(f"{sender.label} sends with Stop-and-Wait")
        receiver.receive(message, sender)
        print(f"{sender.label} waits for ACK")
        print(f"{receiver.label} replies with ACK")


class SlidingWindowProtocol:
    def send(self, sender, receiver, messages, window_size=2):
        print(f"{sender.label} starts Sliding Window (size={window_size})")
        for i, msg in enumerate(messages):
            print(f"{sender.label} sends frame {i}: {msg}")
            receiver.receive(msg, sender)
            print(f"{receiver.label} ACKs frame {i}")


class CSMA_CD:
    def transmit(self, sender, group, message):
        print(f"{sender.label} using CSMA/CD")
        for dev in group:
            if dev != sender:
                dev.receive(message, sender)
