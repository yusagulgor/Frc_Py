

class Navx :...
class Encoder:
    def __init__(self):
        self.pulses = 0
        self.now = 0

    def updatePosition(self):
        self.now += 1

    def reset(self):
        self.pulses = 0

    def get(self):
        return self.now

