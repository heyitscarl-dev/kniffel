import sys, pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
WHITE  =(255,255,255)
BLACK =(0,0,0)
font= pygame.font.Font(None, 40)
ONE =pygame.Rect (540,125,60,30)
TWO =pygame.Rect (540,155,60,30)
THREE = pygame.Rect (540,185,60,30)
FOUR = pygame.Rect (540,215,60,30)
FIVE = pygame.Rect (540,245,60,30)
SIX = pygame.Rect (540,275,60,30)
Liste = [2,2, 2, 3, 3]
block = pygame.image.load("Kniffel-Block-1.png")
AMOUNT_ONE = None
AMOUNT_TWO = None
AMOUNT_THREE = None
AMOUNT_FOUR = None
AMOUNT_FIVE = None
AMOUNT_SIX = None
choice_made =False
while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False      
        if event.type == pygame.MOUSEBUTTONDOWN and not choice_made :
            if ONE.collidepoint(event.pos):
                color_ONE = BLACK
                AMOUNT_ONE = Liste.count(1)*1
                choice_made = True
            elif TWO.collidepoint(event.pos):
                color_ONE = BLACK
                AMOUNT_TWO = Liste.count(2)*2
                choice_made = True
            elif THREE.collidepoint(event.pos):
                color_ONE = BLACK
                AMOUNT_THREE = Liste.count(3)*3
                choice_made = True
            elif FOUR.collidepoint(event.pos):
                color_ONE = BLACK
                AMOUNT_FOUR = Liste.count(4)*4
                choice_made = True
            elif FIVE.collidepoint(event.pos):
                color_ONE = BLACK
                AMOUNT_FIVE = Liste.count(5)*5
                choice_made = True
            elif SIX.collidepoint(event.pos):
                color_ONE = BLACK
                AMOUNT_SIX = Liste.count(6)*6
                choice_made = True
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Liste = [2, 5, 6, 1, 1]  
                choice_made= False
                
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Liste = [5,5,5,5,5]
                choice_made= False
                   
            
    
    screen.fill(WHITE)
    screen.blit(block, (250, 50))           
    if AMOUNT_ONE is not None:
        txt_surface = font.render(str(AMOUNT_ONE), True, color_ONE)
        screen.blit(txt_surface, (ONE.x, ONE.y))
    if AMOUNT_TWO is not None:
        txt_surface = font.render(str(AMOUNT_TWO), True, color_ONE)
        screen.blit(txt_surface, (TWO.x, TWO.y))
    if AMOUNT_THREE is not None:
        txt_surface = font.render(str(AMOUNT_THREE), True, color_ONE)
        screen.blit(txt_surface, (THREE.x, THREE.y))
    if AMOUNT_FOUR is not None:
        txt_surface = font.render(str(AMOUNT_FOUR), True, color_ONE)
        screen.blit(txt_surface, (FOUR.x, FOUR.y))
    if AMOUNT_FIVE is not None:
        txt_surface = font.render(str(AMOUNT_FIVE), True, color_ONE)
        screen.blit(txt_surface, (FIVE.x, FIVE.y))
    if AMOUNT_SIX is not None:
        txt_surface = font.render(str(AMOUNT_SIX), True, color_ONE)
        screen.blit(txt_surface, (SIX.x, SIX.y))


 

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
