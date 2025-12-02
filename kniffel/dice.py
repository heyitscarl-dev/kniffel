import random
import pygame

DIE_SIZE = 50
DIE_BACKGROUND = (0, 0, 0)
DIE_BACKGROUND_KEPT = (100, 100, 100)
DIE_FOREGROUND = (255, 255, 255)
DIE_PIP_SIZE = DIE_SIZE // 10

DIE_ANIMATION_MILLIS = 1000
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

    current: int = 1
    rolling: bool = False
    cycle: int = 0
    time: float = 0

    def __init__(self, value: int) -> None:
        self.value = value
        self.current = value
        self.kept = False

    def roll(self):
        if self.kept or self.rolling: 
            return

        self.rolling = True
        self.value = random.randint(1, 6)
        self.current = random.randint(1, 6)

    def toggle_keep(self):
        if self.rolling:
            return

        self.kept = not self.kept

    def tick(self, dt: float):
        if not self.rolling:
            return

        self.time += dt

        if self.time >= DIE_ANIMATION_MILLIS:
            self.time = 0
            self.cycle = 0
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
        surface = pygame.Surface((DIE_SIZE, DIE_SIZE), pygame.SRCALPHA)
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

DIE_GROUP_MARGIN = 50
DIE_GROUP_SIZE = 5
DIE_GROUP_WIDTH = DIE_SIZE * DIE_GROUP_SIZE + DIE_GROUP_MARGIN * ( DIE_GROUP_SIZE - 1 )

class Dice:
    group: list[Die]

    def __init__(self, length: int):
        self.group = [Die(i + 1) for i in range(length)]

    def toggle_keep(self, index: int):
        self.group[index].toggle_keep()

    def roll(self):
        for die in self.group:
            die.roll()

    def tick(self, dt: float):
        for die in self.group:
            die.tick(dt)

    def draw(self) -> pygame.Surface:
        surface = pygame.Surface((
            DIE_GROUP_WIDTH, 
            DIE_SIZE
        ), pygame.SRCALPHA)

        for i, die in enumerate(self.group):
            surface.blit(die.draw(), (
                DIE_SIZE * i + DIE_GROUP_MARGIN * ( i ),
                0
            ))

        return surface
