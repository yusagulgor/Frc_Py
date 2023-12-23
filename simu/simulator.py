# Simulator.py

import pygame
import sys
from Drive import Drive
from ..ylib import *

class Simulator:
    def __init__(self, drive_instance: Drive):
        self.simulated_robot = drive_instance
        self.robot_position = [400, 300]  # Küpün başlangıç konumu
        self.robot_size = [50, 50]  # Küpün boyutları

    def update_position(self, x_speed, time_step):
        # Simülasyon robotunun pozisyonunu güncelle
        self.robot_position[0] += x_speed * time_step

    def run_simulator(self, time_step=0.1):
        if callable(self.simulated_robot.DriveAuto):
            self.simulated_robot.DriveAuto()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Siyah Ekran")
        black = (0, 0, 0)

        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Simülasyonu güncelle
            self.update_simulator()

            screen.fill(black)
            pygame.draw.rect(screen, (255, 255, 255), (*self.robot_position, *self.robot_size))

            pygame.display.flip()
            clock.tick(60)  # FPS ayarı

    def update_simulator(self):
        # Robotun hızını al
        mGroupLeft: MotorControllerGroup = self.simulated_robot.getDrive().getMGroup()[0]
        mGroupRight: MotorControllerGroup = self.simulated_robot.getDrive().getMGroup()[1]

        left_speed = mGroupLeft.motor1.voltage
        right_speed = mGroupRight.motor1.voltage

        # Lambda fonksiyonu ile motor türüne göre hızı ayarla
        result = lambda: 1.3 if mGroupRight.motor1.__class__.__name__ == 'SparkMax' else 1.0

        # Hızları topla ve ortalamasını al
        x_speed = (left_speed + right_speed) / 2.0

        # Simülasyonu güncelle
        self.update_position(x_speed, result())
