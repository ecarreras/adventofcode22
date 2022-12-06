class Decoder:
    def __init__(self, stream, packet_length=4):
        self.stream = stream
        self.packet_length = packet_length
    
    def find_first_marker(self):
        for idx in range(0, len(self.stream)):
            marker = self.stream[idx: idx + self.packet_length]
            if len(set(marker)) == self.packet_length:
                return idx + self.packet_length
