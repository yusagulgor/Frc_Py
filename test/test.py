# from ylib import *
# startCoding("testing")

from ylib.sysCheck import Check  # sysCheck klasörünü doğrudan import et
from Drive import Drive 

d = Drive()
c = Check(d)
t = c.checkPID()

if __name__ == "__main__":
    print(t)
