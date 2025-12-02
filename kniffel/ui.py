import random
import pygame

class Interface:
    surface: pygame.Surface
    dimensions: pygame.Vector2

    def __init__(self) -> None:
        pygame.init()

        self.surface = self.get_surface()
        self.dimensions = self.get_dimensions()

    def get_dimensions(self) -> pygame.Vector2:
        info = pygame.display.Info()
        dimensions = pygame.Vector2(info.current_w, info.current_h)
        return dimensions

    def get_surface(self) -> pygame.Surface:
        surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        return surface

    def prepare(self):
        self.surface.fill((255, 255, 255))

    def finish(self):
        pygame.display.flip()
