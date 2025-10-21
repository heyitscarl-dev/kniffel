import random
import pygame

DIE_SIZE = 50
DIE_BACKGROUND = (0, 0, 0)
DIE_BACKGROUND_KEPT = (50, 50, 50)
DIE_FOREGROUND = (255, 255, 255)
DIE_PIP_SIZE = DIE_SIZE // 10

DIE_ANIMATION_MILLIS = 2000
DIE_ANIMATION_MILLIS_PER_CYCLE = 250
DIE_ANIMATION_CYCLES = DIE_ANIMATION_MILLIS // DIE_ANIMATION_MILLIS_PER_CYCLE

LEFT = 0.2
CENTER = 0.5
RIGHT = 0.8

TOP = 0.2
BOTTOM = 0.8

class Die:
    value: int
    kept: bool

    current: int | None = None
    rolling: bool = False
    cycle: int = 1
    time: float = 0

    def __init__(self, value: int) -> None:
        self.value = value
        self.kept = False

    def roll(self):
        if self.kept or self.rolling: 
            return

        self.rolling = True
        self.value = random.randint(1, 6)
        self.current = random.randint(1, 6)

    def toggle_keep(self):
        self.kept = not self.kept

    def tick(self, dt: float):
        self.time += dt

        if not self.rolling:
            return

        if self.time >= DIE_ANIMATION_MILLIS:
            self.time = 0
            self.cycle = 1
            self.rolling = False 
            self.current = self.value
        
        next_cycle_starts_at = self.cycle * DIE_ANIMATION_MILLIS_PER_CYCLE

        if self.time >= next_cycle_starts_at:
            self.cycle += 1
            next_cycle_value = random.randint(1, 6)
            if next_cycle_value == self.current:
                next_cycle_value += 1
            if next_cycle_value > 6:
                next_cycle_value = 1
            self.current = next_cycle_value

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

        if self.current == 1:
            pip(CENTER, CENTER)
        elif self.current == 2:
            pip(LEFT, TOP)
            pip(RIGHT, BOTTOM)
        elif self.current == 3:
            pip(LEFT, TOP)
            pip(CENTER, CENTER)
            pip(RIGHT, BOTTOM)
        elif self.current == 4:
            pip(LEFT, TOP)
            pip(LEFT, BOTTOM)
            pip(RIGHT, TOP)
            pip(RIGHT, BOTTOM)
        elif self.current == 5:
            pip(LEFT, TOP)
            pip(LEFT, BOTTOM)
            pip(RIGHT, TOP)
            pip(RIGHT, BOTTOM)
            pip(CENTER, CENTER)
        elif self.current == 6:
            pip(LEFT, TOP)
            pip(LEFT, CENTER)
            pip(LEFT, BOTTOM)
            pip(RIGHT, TOP)
            pip(RIGHT, CENTER)
            pip(RIGHT, BOTTOM)
        
        return surface
