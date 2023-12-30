from .components import Navx , Encoder

class PIDController:
    def __init__(self,encoder:Encoder=None,navx:Navx=None,kP:int=0,kI:int=0,kD:int=0) -> None:
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.navx = navx
        self.encoder = encoder

    def getResult(self):
        result = self.kP * self.kI * self.kD 
        return result

    def __getNavx(self):
        if self.navx is None:return False
        else:return True  

    def __getEncoder(self):
        if self.encoder is None :return False
        else : return True

    def __set(self):
        if self.__getNavx() and self.__getEncoder() :return False
        else:return True
    