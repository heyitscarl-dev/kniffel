from enum import Enum, auto
from kniffel import dice, ui

import pygame
import random

FRAMERATE = 60

def main() -> None:
    die = dice.Die(5)

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
                die.roll()
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_k:
                die.toggle_keep()

        interface.prepare()

        interface.surface.blit(die.draw(), pygame.Vector2(
            interface.dimensions.x // 2 - dice.DIE_SIZE // 2,
            interface.dimensions.y // 2 - dice.DIE_SIZE // 2
        ))

        interface.finish()

    pygame.quit()
