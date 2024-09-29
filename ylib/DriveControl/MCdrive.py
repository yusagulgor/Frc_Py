# MCdrive.py
from abc import ABC, abstractmethod
from .automation import PIDController
from .components import Encoder
from enum import Enum


class MotorType(Enum):
    kBrushed = 0
    kBrushless = 1


class MotorController:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.voltage = 0.0
        self.motor_type: MotorType = MotorType.kBrushed

    def setVoltage(self, voltage: float) -> None:
        """Motorun voltajını ayarla"""
        self.voltage = voltage

    def getID(self) -> int:
        """Motorun ID'sini döndür"""
        return self.id


class Victor(MotorController):
    def __init__(self, PWM_ID: int) -> None:
        super().__init__(id=PWM_ID)
        self.PWM_ID: int = PWM_ID

    def setVoltage(self, voltage: float) -> None:
        super().setVoltage(voltage)

    def getID(self) -> int:
        return super().getID()


class SparkMax(MotorController):
    def __init__(self, CAN_ID: int, motor_type: MotorType) -> None:
        super().__init__(id=CAN_ID)
        self.CAN_ID: int = CAN_ID
        self.motor_type: MotorType = motor_type
        self.encoder = Encoder()

    def setVoltage(self, voltage: float) -> None:
        super().setVoltage(voltage)

    def relativeEncoder(self) -> Encoder:
        """Motorun encoder'ını döndür"""
        return self.encoder 


class MotorControllerGroup:
    def __init__(self, motor1: MotorController, motor2: MotorController, isInverted: bool = False) -> None:
        """İki motoru tek bir grup halinde çalıştır."""
        self.isInverted = isInverted
        self.motor1 = motor1
        self.motor2 = motor2

        if self.isInverted:
            self.motor1.setVoltage(-self.motor1.voltage)
            self.motor2.setVoltage(-self.motor2.voltage)

    def getMotors(self):
        """Motorları döndür"""
        return self.motor1, self.motor2


class DifferentialDrive:
    def __init__(self, mGroupLeft: MotorControllerGroup, mGroupRight: MotorControllerGroup) -> None:
        """İki motor grubunu diferansiyel sürüş ile kontrol eder."""
        self.mGroupLeft = mGroupLeft
        self.mGroupRight = mGroupRight

    def arcadeDrive(self, PIDController: PIDController = None, xSpeed: float = 0.0, zRotation: float = 0.0) -> bool:
        """Arcade tarzı sürüş. xSpeed ileri-geri, zRotation sağ-sol."""
        xSpeed = max(-1.0, min(1.0, xSpeed))
        zRotation = max(-1.0, min(1.0, zRotation))

        leftMotorSpeed = xSpeed + zRotation
        rightMotorSpeed = xSpeed - zRotation

        self.mGroupLeft.motor1.setVoltage(leftMotorSpeed)
        self.mGroupLeft.motor2.setVoltage(leftMotorSpeed)
        self.mGroupRight.motor1.setVoltage(rightMotorSpeed)
        self.mGroupRight.motor2.setVoltage(rightMotorSpeed)

        if PIDController is not None:
            result = PIDController.getResult()
            print(f"PID Result: {result}")
            return True
        return False

    def getMGroup(self):
        """Motor gruplarını döndür"""
        return self.mGroupLeft, self.mGroupRight

    def getMotorsType(self):
        """Motor türlerini döndür"""
        leftMotors = self.mGroupLeft.getMotors()
        rightMotors = self.mGroupRight.getMotors()

        leftMotorType = leftMotors[0].motor_type if leftMotors else None
        rightMotorType = rightMotors[0].motor_type if rightMotors else None

        return leftMotorType, rightMotorType

    def areAllMotorTypesSame(self) -> bool:
        """Motor türlerinin aynı olup olmadığını kontrol et"""
        motorTypes = self.getMotorsType()
        return motorTypes[0] == motorTypes[1] if motorTypes[0] and motorTypes[1] else False


class MyRobot(ABC):
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
        super().__init__()

    @abstractmethod
    def getDrive(self) -> DifferentialDrive:
        pass

    @abstractmethod
    def DriveAuto(self) -> None:
        pass