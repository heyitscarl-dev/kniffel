import pygame
import dice

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True 

open = dice.Dice(50, 50)
kept = dice.Dice(50, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                open.roll()
            elif event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            dice = open.dice
            rects = open.rects((500, 500))

            indices = [ i for (i, rect) in enumerate(rects) if rect.collidepoint(pos) ]
            for i in indices:
                clicked = open.dice.pop(i)
                kept.append(clicked)

    screen.fill((255, 255, 255))

    screen.blit(open.draw(), (500, 500))
    screen.blit(open.draw(), (500, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()