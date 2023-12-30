from ..simu import Simulator
s = Simulator()


class Navx :...
class Encoder:
    def __init__(self):
        self.pulses = 0
        self.now :int= s.robot_position[0] - 400  

    def updatePosition(self):
        self.now += 1

    def reset(self):
        self.pulses = 0

    def get(self):
        return self.now

