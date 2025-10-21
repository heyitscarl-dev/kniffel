from enum import Enum, auto
from kniffel import dice, ui

import pygame

FRAMERATE = 60

def main() -> None:
    die_group = dice.Dice(5)

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
                die_group.roll()
            # elif e.type == pygame.KEYDOWN and e.key == pygame.K_k:
            #     die.toggle_keep()

        die_group.tick(dt)

        interface.prepare()

        interface.surface.blit(die_group.draw(), pygame.Vector2(
            interface.dimensions.x // 2 - dice.DIE_GROUP_WIDTH // 2,
            interface.dimensions.y // 2 - dice.DIE_SIZE // 2
        ))

        interface.finish()

    pygame.quit()
