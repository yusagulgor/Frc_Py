# motorS.py
from .typeMC import MotorType
from ..components import Encoder

class MotorController:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.voltage = 0.0
        self.motor_type = None

    def setVoltage(self, voltage):
        self.voltage = voltage

    def getID(self):
        return self.id

class Victor(MotorController):
    def __init__(self, PWM_ID: int) -> None:
        super().__init__(id=PWM_ID)
        self.PWM_ID: int = PWM_ID

    def getID(self):
        return super().getID()

    def setVoltage(self, voltage):
        super().setVoltage(voltage=voltage)

class SparkMax(MotorController):
    def __init__(self, CAN_ID: int, motor_type:MotorType) -> None:
        super().__init__(id=CAN_ID)
        self.CAN_ID: int = CAN_ID
        self.motor_type = motor_type

    def setVoltage(self, voltage):
        super().setVoltage(voltage=voltage)

    def relativeEncoder(self)-> Encoder:...   
