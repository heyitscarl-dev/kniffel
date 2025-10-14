import random
import pygame

DOT_RATIO = 1 / 10

class Die:
    def __init__(
            self, 
            value: int,
            size: int,
            foreground: tuple[int, int, int] = (255, 255, 255),
            background: tuple[int, int, int] = (0, 0, 0)
    ):
        self.value = value
        self.size = size
        self.foreground = foreground
        self.background = background

        self.can_roll = True

    def roll(self):
        if self.can_roll:
            self.value = random.randint(1, 6)
    
    def draw(self) -> pygame.Surface:
        surface = pygame.Surface((self.size, self.size))
        surface.fill(self.background)

        dot_radius = int(self.size * DOT_RATIO)
        offset = self.size // 4
        center = self.size // 2

        def dot(x, y):
            pygame.draw.circle(surface, self.foreground, (x, y), dot_radius)

        positions = {
            1: [(center, center)],
            2: [(offset, offset), (self.size - offset, self.size - offset)],
            3: [(offset, offset), (center, center), (self.size - offset, self.size - offset)],
            4: [(offset, offset), (self.size - offset, offset),
                (offset, self.size - offset), (self.size - offset, self.size - offset)],
            5: [(offset, offset), (self.size - offset, offset),
                (center, center),
                (offset, self.size - offset), (self.size - offset, self.size - offset)],
            6: [(offset, offset), (self.size - offset, offset),
                (offset, center), (self.size - offset, center),
                (offset, self.size - offset), (self.size - offset, self.size - offset)]
        }

        for pos in positions[self.value]:
            dot(*pos)
        
        return surface
    
    def rect(self, topleft: tuple[int, int]) -> pygame.Rect:
        r = pygame.Rect(0, 0, self.size, self.size)
        r.topleft = topleft
        return r

class Dice:
    def __init__(
            self,
            size: int, 
            padding: int,
            background: tuple[int, int, int] = (255, 255, 255),
            dice: list[Die] = []
    ):
        self.dice = dice
        self.count = len(dice)
        self.size = size
        self.padding = padding
        self.background = background
    
    def append(self, die: Die):
        self.dice.append(die)
        self.count += 1

    def roll(self):
        for die in self.dice:
            die.roll()
    
    def draw(self) -> pygame.Surface:
        width = self.count * self.size + (self.count - 1) * self.padding
        height = self.size

        surface = pygame.Surface((width, height))
        surface.fill(self.background)

        for i, die in enumerate(self.dice):
            surface.blit(die.draw(), (i * (self.padding + self.size), 0))

        return surface
    
    def rects(self, topleft: tuple[int, int]) -> list[pygame.Rect]:
        anchor_x, anchor_y = topleft
        rects = []

        for i in range(self.count):
            x = anchor_x + i * (self.size + self.padding)
            rects.append(pygame.Rect(x, anchor_y, self.size, self.size))
        
        return rects