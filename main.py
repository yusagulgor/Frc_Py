from ylib import Simulator
from Drive import Drive
drive = Drive()
autos = drive.DriveAuto()

if __name__ == "__main__":
    simulator = Simulator(drive)

    # Simülasyonu başlat
    simulator.run_simulator(autos)
    simulator.run()

    