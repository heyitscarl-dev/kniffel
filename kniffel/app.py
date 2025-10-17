from enum import Enum, auto
from kniffel import ui

import pygame

FRAMERATE = 60

class Consequence(Enum):
    CONTINUE = auto()
    QUIT = auto()

def update() -> Consequence:
    for e in pygame.event.get():
        if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE
        or e.type == pygame.QUIT):
            return Consequence.QUIT

    return Consequence.CONTINUE

def main() -> None:
    running = True

    interface = ui.Interface()
    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(FRAMERATE)

        if update() == Consequence.QUIT:
            running = False

        interface.prepare()
        interface.finish()

    pygame.quit()
