import pygame
from pan_python.step import Step


class WaitStep(Step):
    def __init__(self):
        super().__init__()

    def calculate_position(self, engine):
        return engine.cam_x, engine.cam_y

    def execute(self, engine):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
