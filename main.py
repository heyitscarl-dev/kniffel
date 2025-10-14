import sys, pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
WHITE  =(255,255,255)
BLACK =(0,0,0)
font= pygame.font.Font(None, 36)
input_box=pygame.Rect (150,150,300,50)
color_active= BLACK
color_inactive = WHITE
text ="hallo"
active= False
block = pygame.image.load("Kniffel-Block-1.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color =color_active if active else color_inactive 




    screen.fill("white")
    txt_surface = font.render(text, True, BLACK)
    width = max(300, txt_surface.get_width()+10)
    input_box.w = width 
    screen.blit(block, (250, 50))
    screen.blit(txt_surface, (input_box.x + 50, input_box.y + 10))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()