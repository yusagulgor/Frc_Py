from ylib import *

class Drive(MyRobot):
    def __init__(self) -> None:
        super().__init__()

        self.Leftfront = SparkMax(1,MotorType.kBrushless)
        self.Leftrear = SparkMax(2,MotorType.kBrushless)
        self.Rightfront = SparkMax(3,MotorType.kBrushless)
        self.Rightrear = SparkMax(4,MotorType.kBrushless)

        self.rGruop = MotorControllerGroup(motor1=self.Rightfront,motor2=self.Rightrear,m_isInverted=True)
        self.lGroup = MotorControllerGroup(motor1=self.Leftfront,motor2=self.Leftrear)

        self.drive = DifferantielDrive(self.lGroup,self.rGruop)

        self.navx = Navx()
        self.encoder = Encoder()

        self.MotorEncoder = self.Leftfront.relativeEncoder()

        self.PIDController = PIDController(encoder=self.encoder,navx=self.navx,kP=1,kI=2,kD=1)
        self.PIDController = PIDController(encoder=self.MotorEncoder,navx=self.navx,kP=1,kI=1,kD=1)


    def getDrive(self) -> DifferantielDrive:
        return self.drive
    
    def goFunc(self):
        return self.drive.arcadeDrive(PIDController=self.PIDController,xSpeed=1,zRotation=0)
    
    def goXmeter(self, x_meters: float, speed: float):

        # Encoder'ı sıfırla (başlangıç pozisyonunu belirleme)
        self.encoder.reset()

        # Hedef pulse'a ulaşana kadar ileri git
        while self.encoder.get() <= x_meters:
            # Her bir pulse geldiğinde encoder'ı güncelle
            self.encoder.updatePosition()

            # İleri gitme kodu buraya eklenebilir
            self.drive.arcadeDrive(xSpeed=speed, zRotation=0)

    
    def turnXDegree(self,xSpeed:float,x:int):
        return self.drive.arcadeDrive(xSpeed=xSpeed,zRotation=x)
    
    def DriveAuto(self):
        return self.goXmeter(1,0.5)
    
