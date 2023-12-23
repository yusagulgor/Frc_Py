from ..Drive import DifferantielDrive

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

    def getDrive(self)-> DifferantielDrive:... 

    def DriveAuto(self):pass

