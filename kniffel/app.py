from enum import Enum, auto
from kniffel import dice, ui

import pygame

FRAMERATE = 60

class Phase(Enum):
    ROLL = 1
    NOTE = 2
    WAIT = 3

def main() -> None:
    die_group = dice.Dice(5)
    phase = Phase.ROLL

    running = True

    interface = ui.Interface()
    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(FRAMERATE)

        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE
            or e.type == pygame.QUIT):
                running = False
            
            if phase == Phase.ROLL:
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    die_group.roll()
                elif e.type == pygame.KEYDOWN and e.key == pygame.K_1:
                    die_group.toggle_keep(0)
                elif e.type == pygame.KEYDOWN and e.key == pygame.K_2:
                    die_group.toggle_keep(1)
                elif e.type == pygame.KEYDOWN and e.key == pygame.K_3:
                    die_group.toggle_keep(2)
                elif e.type == pygame.KEYDOWN and e.key == pygame.K_4:
                    die_group.toggle_keep(3)
                elif e.type == pygame.KEYDOWN and e.key == pygame.K_5:
                    die_group.toggle_keep(4)
            elif phase == Phase.NOTE:
                print("tobi")
                # TOBI IST TOLL
            elif phase == Phase.WAIT:
                print("waiting")

        die_group.tick(dt)

        interface.prepare()

        interface.surface.blit(die_group.draw(), pygame.Vector2(
            interface.dimensions.x // 2 - dice.DIE_GROUP_WIDTH // 2,
            interface.dimensions.y // 2 - dice.DIE_SIZE // 2
        ))

        interface.finish()

    pygame.quit()
