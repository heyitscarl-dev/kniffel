import pygame

MAXIMUM_FPS = 30

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True 

def handle_mouse_event(event: pygame.event.Event) -> bool:
    return True

def handle_key_event(event: pygame.event.Event) -> bool:
    return True

def handle_event(event: pygame.event.Event) -> bool:
    if event.type == pygame.QUIT:
            return False
    elif event.type == pygame.KEYDOWN:
            return handle_key_event(event)
    elif event.type == pygame.MOUSEBUTTONDOWN:
            return handle_mouse_event(event)
    else:
        return True

def handle_events():
    for event in pygame.event.get():
        if not handle_event(event):
            return False
    return True

while running:
    running = handle_events()

    pygame.display.flip()
    clock.tick(MAXIMUM_FPS)

pygame.quit()
