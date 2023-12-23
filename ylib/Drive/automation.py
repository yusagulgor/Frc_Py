from ..components import Navx

class PIDController:
    def __init__(self,navx:Navx=None,kP:int=0,kI:int=0,kD:int=0) -> None:
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.navx = navx

    def getResult(self):
        result = self.kP * self.kI * self.kD    
        return result

    def __result(self):
        if self.navx is None:
            return False
        else:
            return True    
    