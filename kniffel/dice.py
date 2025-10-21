import random
import pygame

DIE_SIZE = 50
DIE_BACKGROUND = (0, 0, 0)
DIE_BACKGROUND_KEPT = (50, 50, 50)
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

    def roll(self):
        if self.kept: return
        self.value = random.randint(1, 6)

    def toggle_keep(self):
        self.kept = not self.kept

    def draw(self) -> pygame.Surface:
        surface = pygame.Surface((DIE_SIZE, DIE_SIZE))
        pygame.draw.rect(
            surface, 
            DIE_BACKGROUND if not self.kept else DIE_BACKGROUND_KEPT, 
            [0, 0, DIE_SIZE, DIE_SIZE]
        )

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
        
        return surface
