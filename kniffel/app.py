from enum import Enum, auto
from kniffel import ui

import pygame
import random

FRAMERATE = 60

def main() -> None:
    die = ui.Die(5)

    running = True

    interface = ui.Interface()
    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(FRAMERATE)

        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE
            or e.type == pygame.QUIT):
                running = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                die.set(random.randint(1, 6))

        interface.prepare()

        die.draw(interface, pygame.Vector2(
            interface.dimensions.x // 2,
            interface.dimensions.y // 2
        ))

        interface.finish()

    pygame.quit()
