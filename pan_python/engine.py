import pygame


class Engine:
    def __init__(self, img_path, init_cam_pos=(0, 0), screen_resolution=(1920, 1080)):
        self.screen = pygame.display.set_mode(screen_resolution)
        self.img = pygame.image.load(img_path)
        self.view_w, self.view_h = self.screen.get_size()
        self.clock = pygame.time.Clock()
        self.cam_x, self.cam_y = init_cam_pos  # Store as float.
        self.cam_x_int, self.cam_y_int = self.cam_x, self.cam_y  # Store as int for rendering.
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run(self, start_index=0):
        # Update position after each step
        for i in range(start_index):
            self.cam_x, self.cam_y = self.steps[i].calculate_position(self)

        # Display the initial image first
        self.screen.blit(self.img, (0, 0), (self.cam_x, self.cam_y, self.view_w, self.view_h))
        pygame.display.flip()

        for step in self.steps[start_index:]:
            self.clock.tick(60)  # Limit the framerate to 60 FPS.
            step.execute(self)
        pygame.display.flip()
