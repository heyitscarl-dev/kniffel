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

DIE_SIZE = 50
DIE_BACKGROUND = (0, 0, 0)
DIE_FOREGROUND = (255, 255, 255)
DIE_PIP_SIZE = DIE_SIZE // 10

LEFT = 0.2
CENTER = 0.5
RIGHT = 0.8

TOP = 0.2
BOTTOM = 0.8

class Die:
    value: int
    kept: bool

    def __init__(self, value: int) -> None:
        self.value = value
        self.kept = False

    def set(self, value: int):
        self.value = value

    def toggle_keep(self):
        self.kept = not self.kept

    def draw(self, interface: Interface, center: pygame.Vector2):
        surface = pygame.Surface((DIE_SIZE, DIE_SIZE))
        pygame.draw.rect(surface, DIE_BACKGROUND, [0, 0, DIE_SIZE, DIE_SIZE])

        def pip(relative_x: float, relative_y: float):
            pygame.draw.circle(
                surface,
                DIE_FOREGROUND, 
                (relative_x * DIE_SIZE, relative_y * DIE_SIZE), 
                DIE_PIP_SIZE
            )

        if self.value == 1:
            pip(CENTER, CENTER)
        elif self.value == 2:
            pip(LEFT, TOP)
            pip(RIGHT, BOTTOM)
        elif self.value == 3:
            pip(LEFT, TOP)
            pip(CENTER, CENTER)
            pip(RIGHT, BOTTOM)
        elif self.value == 4:
            pip(LEFT, TOP)
            pip(LEFT, BOTTOM)
            pip(RIGHT, TOP)
            pip(RIGHT, BOTTOM)
        elif self.value == 5:
            pip(LEFT, TOP)
            pip(LEFT, BOTTOM)
            pip(RIGHT, TOP)
            pip(RIGHT, BOTTOM)
            pip(CENTER, CENTER)
        elif self.value == 6:
            pip(LEFT, TOP)
            pip(LEFT, CENTER)
            pip(LEFT, BOTTOM)
            pip(RIGHT, TOP)
            pip(RIGHT, CENTER)
            pip(RIGHT, BOTTOM)

        interface.surface.blit(surface, (
            center.x - DIE_SIZE // 2,
            center.y - DIE_SIZE // 2
        ))
