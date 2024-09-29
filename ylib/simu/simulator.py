import pygame
import sys
from ..DriveControl import MyRobot, SparkMax

class Simulator:
    def __init__(self, drive_instance: MyRobot):
        self.simulated_robot = drive_instance
        self.robot_position = [400, 300]  # Robotun başlangıç pozisyonu
        self.robot_size = [50, 50]  # Robotun boyutları
        self.robot_image_original = pygame.Surface(self.robot_size)
        self.robot_image_original.fill((255, 255, 255))  # Beyaz bir kare olarak başlar

        self.rot = 0  # Başlangıç rotasyonu 0

    def update_position(self, x_speed, time_step):
        self.robot_position[0] += x_speed * time_step
        self.robot_image = pygame.transform.rotate(self.robot_image_original, self.rot)

    def run_simulator(self, time_step=0.1):
        if callable(self.simulated_robot.DriveAuto):
            self.simulated_robot.DriveAuto()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Robot Simülasyonu")
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
            rotated_image, rotated_rect = self.rot_center(self.robot_image, self.rot, self.robot_position)
            screen.blit(rotated_image, rotated_rect.topleft)

            pygame.display.flip()
            clock.tick(60)  # FPS ayarı

    def update_simulator(self):
        mGroupLeft, mGroupRight = self.simulated_robot.getDrive().getMGroup()

        left_speed = mGroupLeft.motor1.voltage
        right_speed = mGroupRight.motor1.voltage

        result = 1.3 if isinstance(mGroupRight.motor1, SparkMax) else 1.0

        x_speed = (left_speed + right_speed) / 2.0
        self.update_position(x_speed, result)

    def rot_center(self, image, angle, position):
        """Rotates an image while keeping its center."""
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(center=position).center)
        return rotated_image, new_rect
