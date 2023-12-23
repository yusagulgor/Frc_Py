from ylib import *

class Drive(MyRobot):
    def __init__(self) -> None:
        super().__init__()

        Leftfront = SparkMax(1,MotorType.kBrushless)
        Leftrear = SparkMax(2,MotorType.kBrushless)
        Rightfront = SparkMax(3,MotorType.kBrushless)
        Rightrear = SparkMax(4,MotorType.kBrushless)

        rGruop = MotorControllerGroup(motor1=Rightfront,motor2=Rightrear,m_isInverted=True)
        lGroup = MotorControllerGroup(motor1=Leftfront,motor2=Leftrear)

        self.drive = DifferantielDrive(lGroup,rGruop)

        self.navx = Navx()

        self.PID = PIDController(navx=self.navx,kP=1,kI=2,kD=1)


    def getDrive(self) -> DifferantielDrive:
        return self.drive
    
    def goXmeter(self,x:float):
        return self.drive.arcadeDrive(x,0)
    
    def turnXDegree(self,xSpeed:float,x:int):
        return self.drive.arcadeDrive(xSpeed=xSpeed,zRotation=x)
    
    def DriveAuto(self):
        return self.turnXDegree(1,10)