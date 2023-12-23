# MCdrive.py
from typing import overload
from .motorS import MotorController
from .automation import PIDController

class MotorControllerGroup:
    def __init__(self, motor1: MotorController, motor2: MotorController, m_isInverted: bool = False) -> None:
        self.m_isInverted = m_isInverted 
        self.motor1 = motor1
        self.motor2 = motor2 

        if hasattr(self.motor1, 'voltage') and hasattr(self.motor2, 'voltage') and self.m_isInverted:
            self.motor1.setVoltage(-self.motor1.voltage)
            self.motor2.setVoltage(-self.motor2.voltage)

    def getMotors(self) -> MotorController:
        return self.motor1, self.motor2

class DifferantielDrive:
    def __init__(self, mGroupLeft: MotorControllerGroup, mGroupRight: MotorControllerGroup) -> None:
        self.mGroupLeft = mGroupLeft
        self.mGroupRight = mGroupRight

    @overload
    def arcadeDrive(self, xSpeed: float, zRotation: float):
        xSpeed = max(-1, min(1, xSpeed))
        zRotation = max(-1, min(1, zRotation))

        left_motor_speed = xSpeed + zRotation
        right_motor_speed = xSpeed - zRotation

        self.mGroupLeft.motor1.setVoltage(left_motor_speed)
        self.mGroupLeft.motor2.setVoltage(left_motor_speed)
        self.mGroupRight.motor1.setVoltage(right_motor_speed)
        self.mGroupRight.motor2.setVoltage(right_motor_speed)

    @overload
    def arcadeDrive(self,PIDController:PIDController,xSpeed: float, zRotation: float):
        xSpeed = max(-1, min(1, xSpeed))
        zRotation = max(-1, min(1, zRotation))

        left_motor_speed = xSpeed + zRotation
        right_motor_speed = xSpeed - zRotation

        self.mGroupLeft.motor1.setVoltage(left_motor_speed)
        self.mGroupLeft.motor2.setVoltage(left_motor_speed)
        self.mGroupRight.motor1.setVoltage(right_motor_speed)
        self.mGroupRight.motor2.setVoltage(right_motor_speed)    

    def getMGroup(self) -> MotorControllerGroup:
        return self.mGroupLeft, self.mGroupRight

    def getMotorsType(self):
        left_motors = self.mGroupLeft.getMotors()
        right_motors = self.mGroupRight.getMotors()

        left_motor_type = left_motors[0].motor_type if left_motors else None
        right_motor_type = right_motors[0].motor_type if right_motors else None

        return left_motor_type, right_motor_type

    def are_all_motor_types_same(self):
        motor_types = self.getMotorsType()
        return all(type == motor_types[0] for type in motor_types)
