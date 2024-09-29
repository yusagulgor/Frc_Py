from ylib import *
import time

class Drive(MyRobot):
    def __init__(self) -> None:
        super().__init__()

        self.Leftfront = SparkMax(1, MotorType.kBrushless)
        self.Leftrear = SparkMax(2, MotorType.kBrushless)
        self.Rightfront = SparkMax(3, MotorType.kBrushless)
        self.Rightrear = SparkMax(4, MotorType.kBrushless)

        self.rGroup = MotorControllerGroup(motor1=self.Rightfront, motor2=self.Rightrear,isInverted=True)
        self.lGroup = MotorControllerGroup(motor1=self.Leftfront, motor2=self.Leftrear)

        self.drive = DifferentialDrive(self.lGroup, self.rGroup)

        self.navx = Navx()
        self.encoder = Encoder()

        self.MotorEncoder = self.Leftfront.relativeEncoder()

        self.PIDController = PIDController(encoder=self.encoder, navx=self.navx, kP=1, kI=2, kD=1)
        self.PIDMotorEncoderController = PIDController(encoder=self.MotorEncoder, navx=self.navx, kP=1, kI=1, kD=1)

    def getDrive(self) -> DifferentialDrive:
        return self.drive

    def goFunc(self):
        return self.drive.arcadeDrive(PIDController=self.PIDController, xSpeed=-1, zRotation=0)

    def goXmeter(self, x_meters: float, speed: float):
        self.encoder.reset()  
        target_position = x_meters * 10  
        current_position = 0

        while current_position < target_position:
            current_position = self.encoder.get()

            self.drive.arcadeDrive(xSpeed=speed, zRotation=0)
            # print(f"Current Position: {current_position}, Target: {target_position}")

        self.drive.arcadeDrive(xSpeed=0, zRotation=0)
        print("Target reached, stopping.")

    def turnXDegree(self, xSpeed: float, angle: float):
        rotation_time = angle / 360  
        duration = max(0.1, rotation_time)  
        start_time = time.time()

        # Dönüş işlemi
        while time.time() - start_time < duration:
            self.drive.arcadeDrive(xSpeed=0, zRotation=xSpeed)  
            time.sleep(0.02)  

        self.drive.arcadeDrive(xSpeed=0, zRotation=0)

    def goZero(self):
        return self.drive.arcadeDrive()

    def DriveAuto(self):
        return self.turnXDegree(1, 12) 
