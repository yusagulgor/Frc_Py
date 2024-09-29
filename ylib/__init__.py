from .DriveControl import *
from .simu import *

class Error(Exception):
    def __init__(self, message="Bir hata oluştu"):
        self.message = message
        super().__init__(self.message)

def load_robot(drive: DifferentialDrive):
    # Check left and right motor groups
    leftG = drive.mGroupLeft
    rightG = drive.mGroupRight 

    # Check motor types
    if not drive.are_all_motor_types_same():
        raise ValueError("This code is not currently supported")
    
    if rightG.m_isInverted is False:
        raise Error("This robot have a problem")

       
    if leftG.motor1.id == 1 and leftG.motor2.id == 2:
        if rightG.motor1.id == 3 and rightG.motor2.id == 4:
            return True
        
    if leftG.motor1.id == 2 and leftG.motor2.id == 1:
        if rightG.motor1.id == 4 and rightG.motor2.id == 3:
            return True          

    # Error message if conditions are not met
    raise Error("This code is not currently supported")

def startCoding(robot_name: str):
    robot_code = f"""
from ylib import *

class {robot_name}(MyRobot):
    def __init__(self) -> None:
        super().__init__()

    # ZORUNLU ALAN !!! bu fonksiyon your DifferentialDrive return etmesi gerek 
    def getDrive(self) -> DifferentialDrive:pass

    # ZORUNLU ALAN !!! robotun autonomous area
    def DriveAuto(self):return None
"""

    with open(f"{robot_name}.py", "w") as file:
        file.write(robot_code)


__all__ = ["Victor", "SparkMax", "DifferentialDrive", "MotorControllerGroup", "MotorType","PIDController","Navx","Encoder","MyRobot","load_robot","startCoding","Simulator"]
