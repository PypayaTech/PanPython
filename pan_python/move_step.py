import pygame
from pan_python.step import Step


class MoveStep(Step):
    def __init__(self, duration, target_x, target_y, is_relative=True, delay=0.017):
        super().__init__()
        self.duration = duration
        self.target_x = target_x
        self.target_y = target_y
        self.is_relative = is_relative
        self.delay = delay

    def calculate_position(self, engine):
        target_x = self.target_x + engine.cam_x if self.is_relative else self.target_x
        target_y = self.target_y + engine.cam_y if self.is_relative else self.target_y
        return target_x, target_y

    def execute(self, engine):
        start_time = pygame.time.get_ticks()
        start_x, start_y = engine.cam_x, engine.cam_y

        target_x, target_y = self.calculate_position(engine)

        STEPS = self.duration / self.delay  # Expected number of steps

        step_x = (target_x - start_x) / STEPS
        step_y = (target_y - start_y) / STEPS

        for _ in range(int(STEPS)):
            engine.cam_x += step_x
            engine.cam_y += step_y
            engine.cam_x_int, engine.cam_y_int = int(engine.cam_x), int(engine.cam_y)

            # Record start time of frame render
            frame_start_time = pygame.time.get_ticks()

            engine.screen.blit(engine.img, (0, 0), (engine.cam_x_int,
                                                    engine.cam_y_int,
                                                    engine.view_w, engine.view_h))
            pygame.display.flip()

            # Calculate time taken to render frame
            frame_render_time = pygame.time.get_ticks() - frame_start_time

            # Wait for remaining time, if any
            if self.delay * 1000 > frame_render_time:
                pygame.time.wait(int(self.delay * 1000 - frame_render_time))

        engine.cam_x, engine.cam_y = target_x, target_y
        engine.cam_x_int, engine.cam_y_int = int(engine.cam_x), int(engine.cam_y)

        engine.screen.blit(engine.img, (0, 0), (engine.cam_x_int,
                                                engine.cam_y_int,
                                                engine.view_w, engine.view_h))
        pygame.display.flip()
