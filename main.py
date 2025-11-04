import sys, pygame

WIDTH, HEIGHT = 1000, 700
BOX_WIDTH, BOX_HEIGHT = 65, 38
BOX_X, BOX_Y = 196, 83


def new_box(image_x, image_y, box_x, box_y):
    x = image_x + BOX_X + (box_x * BOX_WIDTH)
    y = image_y + BOX_Y + (box_y * BOX_HEIGHT)
    return pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)

pygame.init()
screen = pygame.display.set_mode ((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
WHITE  =(255,255,255)
BLACK =(0,0,0)
font= pygame.font.Font(None, 50)

ONE = new_box(100, 100, 0, 0)
TWO = new_box(100, 100, 0, 1)
THREE = new_box(100,100, 0, 2)
FOUR = new_box(100,100, 0,3)
FIVE = new_box (100,100,0,4)
SIX = new_box (100,100,0,5)
SUM_BLOCK_1 = new_box (100,100, 0,6)
SUM_BLOCK_2 = new_box (100,100,0,7)
SUM_BLOCK_3 = new_box (100,100,0,8)
THREE_OF_A_KIND = new_box (100,100, 0,9)
Liste = [2,2,2,3,3]
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
            elif THREE_OF_A_KIND.collidepoint(event.pos):
                 Liste.count(1) = 3, Liste
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Liste = [2, 5, 6, 1, 1]  
                choice_made= False
                
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Liste = [5,5,5,5,5]
                choice_made= False

    screen.fill(WHITE)
    screen.blit(block, (100, 100))

    if AMOUNT_ONE != None and AMOUNT_TWO != None and AMOUNT_THREE != None and AMOUNT_FOUR != None and AMOUNT_FIVE != None and AMOUNT_SIX != None:            
        SUM_1 = AMOUNT_ONE + AMOUNT_TWO + AMOUNT_THREE + AMOUNT_FOUR + AMOUNT_FIVE + AMOUNT_SIX
        txt_surface = font.render(str(SUM_1), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_1.x, SUM_BLOCK_1.y))
        if SUM_1 > 63:
           SUM_2 = SUM_1 + 63
           txt_surface = font.render(str(SUM_2), True, color_ONE)
           screen.blit(txt_surface, (SUM_BLOCK_3.x, SUM_BLOCK_3.y))
           txt_surface = font.render(str(35), True, color_ONE)
           screen.blit(txt_surface, (SUM_BLOCK_2.x, SUM_BLOCK_2.y))
    
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
