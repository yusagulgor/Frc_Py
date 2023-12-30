# MCdrive.py
from .automation import PIDController

from .typeMC import MotorType
from .components import Encoder

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

    def arcadeDrive(self,PIDController:PIDController=None,xSpeed: float=0, zRotation: float=0):
        xSpeed = max(-1, min(1, xSpeed))
        zRotation = max(-1, min(1, zRotation))

        left_motor_speed = xSpeed + zRotation
        right_motor_speed = xSpeed - zRotation

        self.mGroupLeft.motor1.setVoltage(left_motor_speed)
        self.mGroupLeft.motor2.setVoltage(left_motor_speed)
        self.mGroupRight.motor1.setVoltage(right_motor_speed)
        self.mGroupRight.motor2.setVoltage(right_motor_speed)

        pid = False

        if PIDController is not None:
            pid = True

        return pid    


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
    
class MyRobot:
    """
    MyRobot

    >>> class Drive(MyRobot):
    >>>     def __init__(self) -> None:

    motorlarımız(fazlasıyla eksik bir kod örneği) TODO : NOT RECOMENDED
    >>>         motor1 = Victor(1) # motor variable
    >>>         motor2 = Victor(2) # motor variable

    motor grupları(fazlasıyla eksik bir kod örneği) TODO : NOT RECOMENDED
    >>>         rGroup = MotorControllerGroup(motor1,motor2)
    >>>         lGroup = MotorControllerGroup(motor1,motor2)

    sürüş kısmı(fazlasıyla eksik bir kod örneği) TODO : NOT RECOMENDED
    >>>         self.drive = DifferantielDrive(lGroup,rGroup)

    komponentler(fazlasıyla eksik bir kod örneği) TODO : NOT RECOMENDED

    Zorunlu olarak doldurulması gereken alan
    >>>     def getDrive(self)-> DifferantielDrive:return self.drive 
    """

    def __init__(self) -> None:
        pass

    def getDrive(self)-> DifferantielDrive:pass 

    def DriveAuto(self):pass    
