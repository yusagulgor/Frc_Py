
from ylib import *

class testing(MyRobot):
    def __init__(self) -> None:
        super().__init__()

    # ZORUNLU ALAN !!! bu fonksiyon your DifferantielDrive return etmesi gerek 
    def getDrive(self) -> DifferantielDrive:pass

    # ZORUNLU ALAN !!! robotun autonomous area
    def DriveAuto(self):return None
