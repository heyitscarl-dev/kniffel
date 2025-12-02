import sys, pygame

BOX_WIDTH, BOX_HEIGHT = 135 // 2, 80 // 2
BOX_X, BOX_Y = 414 // 2, 216 // 2


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

OFFSET = 20 // 2 # Lücke zwischen dem ersten und zweiten Teil des Blocks

ONE = new_box(100, 50, 0, 0)
TWO = new_box(100, 50, 0, 1)
THREE = new_box(100,50, 0, 2)
FOUR = new_box(100,50, 0,3)
FIVE = new_box (100,50,0,4)
SIX = new_box (100,50,0,5)
SUM_BLOCK_1 = new_box (100,50, 0,6)
SUM_BLOCK_2 = new_box (100,50,0,7)
SUM_BLOCK_3 = new_box (100,50,0,8)
THREE_OF_A_KIND = new_box (100,50 + OFFSET,0,9)
FOUR_OF_A_KIND = new_box (100,50 + OFFSET,0,10)
FULL_HOUSE = new_box (100,50 + OFFSET,0,11)
SMALL_STREET = new_box (100,50 + OFFSET,0,12)
BIG_STREET = new_box (100,50 + OFFSET,0,13)
KNIFFEL = new_box (100,50 + OFFSET,0,14)
CHANCE = new_box(100,50 + OFFSET,0,15)
SUM_BLOCK_4 = new_box (100,50 + OFFSET,0,16)
SUM_BLOCK_5 = new_box (100,50 + OFFSET,0,17)
SUM_BLOCK_6 = new_box (100,50 + OFFSET,0,18)
screen.fill(WHITE)
block = pygame.image.load("Kniffel-Block-3.jpg")
WIDTH, HEIGHT = 547, 869
block = pygame.transform.scale(block, (WIDTH, HEIGHT))

screen.blit(block, (100, 50))


choice_made = False
Liste = [1,1,1,4,4]

AMOUNT_ONE = None
AMOUNT_TWO = None
AMOUNT_THREE = None
AMOUNT_FOUR = None
AMOUNT_FIVE = None
AMOUNT_SIX = None
AMOUNT_THREE_OF_A_KIND = None
AMOUNT_FOUR_OF_A_KIND = None
AMOUNT_FULL_HOUSE = None
AMOUNT_SMALL_STREET = None
AMOUNT_BIG_STREET = None
AMOUNT_KNIFFEL = None
AMOUNT_CHANCE = None


ONE_DONE = False
TWO_DONE = False
THREE_DONE= False
FOUR_DONE = False
FIVE_DONE = False
SIX_DONE = False
THREE_OF_A_KIND_DONE = False
FOUR_OF_A_KIND_DONE = False
FULL_HOUSE_DONE = False
SMALL_STREET_DONE = False
BIG_STREET_DONE = False
KNIFFEL_DONE = False
CHANCE_DONE = False

while running:

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN and not choice_made:
            if ONE.collidepoint(event.pos) and not ONE_DONE:
                color_ONE = BLACK
                AMOUNT_ONE = Liste.count(1)*1
                choice_made = True
            elif TWO.collidepoint(event.pos) and not TWO_DONE:
                color_ONE = BLACK
                AMOUNT_TWO = Liste.count(2)*2
                choice_made = True
            elif THREE.collidepoint(event.pos) and not THREE_DONE:
                color_ONE = BLACK
                AMOUNT_THREE = Liste.count(3)*3
                choice_made = True
            elif FOUR.collidepoint(event.pos) and not FOUR_DONE:
                color_ONE = BLACK
                AMOUNT_FOUR = Liste.count(4)*4
                choice_made = True
            elif FIVE.collidepoint(event.pos) and not FIVE_DONE:
                color_ONE = BLACK
                AMOUNT_FIVE = Liste.count(5)*5
                choice_made = True
            elif SIX.collidepoint(event.pos) and not SIX_DONE:
                color_ONE = BLACK
                AMOUNT_SIX = Liste.count(6)*6
                choice_made = True
            elif THREE_OF_A_KIND.collidepoint(event.pos) and not THREE_OF_A_KIND_DONE:
                if Liste.count(1) > 2 or Liste.count(2) > 2 or Liste.count(3) > 2 or Liste.count(4) >2 or Liste.count(5) >2 or Liste.count(6) >2:
                    AMOUNT_THREE_OF_A_KIND = sum(Liste)
                    color_ONE = BLACK
                    choice_made = True
                else:
                    AMOUNT_THREE_OF_A_KIND = 0
                    color_ONE = BLACK
                    choice_made = True
            elif FOUR_OF_A_KIND.collidepoint(event.pos) and not FOUR_OF_A_KIND_DONE:
                if Liste.count(1) > 3 or Liste.count(2) > 3 or Liste.count(3) > 3 or Liste.count(4) >3 or Liste.count(5) >3 or Liste.count(6) >3:
                    AMOUNT_FOUR_OF_A_KIND = sum(Liste)
                    color_ONE = BLACK
                    choice_made = True
                else:
                    AMOUNT_FOUR_OF_A_KIND = 0
                    color_ONE = BLACK
                    choice_made = True
            elif FULL_HOUSE.collidepoint(event.pos) and not FULL_HOUSE_DONE:     
                if (Liste.count(1) == 3 or Liste.count(2) == 3 or Liste.count(3) == 3 or Liste.count(4) == 3 or Liste.count(5) == 3 or Liste.count(6) == 3) and (Liste.count(1) == 2 or Liste.count(2) == 2 or Liste.count(3) == 2 or Liste.count(4) == 2 or Liste.count(5) == 2 or Liste.count(6) == 2):
                    AMOUNT_FULL_HOUSE = 25
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    AMOUNT_FULL_HOUSE = 0
                    color_ONE = BLACK
                    choice_made = True
            elif SMALL_STREET.collidepoint(event.pos) and not SMALL_STREET_DONE:
                if 1 in Liste and 2 in Liste and 3  in Liste and 4 in Liste or 2 in Liste and 3 in Liste and  4 in Liste and 5 in Liste or 3 in Liste and 4 in Liste and 5 in Liste and 6 in Liste:
                    AMOUNT_SMALL_STREET = 30
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    AMOUNT_SMALL_STREET = 0
                    color_ONE = BLACK
                    choice_made = True
            elif BIG_STREET.collidepoint(event.pos) and not BIG_STREET_DONE:
                if 1 in Liste and 2 in Liste and 3  in Liste and 4 in Liste and 5 in Liste or 2 in Liste and 3 in Liste and  4 in Liste and 5 in Liste and 6 in Liste:
                    AMOUNT_BIG_STREET = 40
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    AMOUNT_BIG_STREET = 0
                    color_ONE = BLACK
                    choice_made = True
            elif KNIFFEL.collidepoint(event.pos) and not KNIFFEL_DONE:
                if Liste.count(1) == 5 or Liste.count(2) == 5 or Liste.count(3) == 5 or Liste.count(4) == 5 or Liste.count(5) == 5 or Liste.count(6) == 5:
                    AMOUNT_KNIFFEL = 50
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    AMOUNT_KNIFFEL = 0
                    color_ONE = BLACK
                    choice_made = True  
            elif CHANCE.collidepoint(event.pos) and not CHANCE_DONE:
                AMOUNT_CHANCE = sum(Liste)
                color_ONE = BLACK
                choice_made = True


    
            
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                Liste = (5,5,5,5,5) 
                choice_made = False
    

                

    if AMOUNT_ONE != None and AMOUNT_TWO != None and AMOUNT_THREE != None and AMOUNT_FOUR != None and AMOUNT_FIVE != None and AMOUNT_SIX != None:            
        SUM_1 = AMOUNT_ONE + AMOUNT_TWO + AMOUNT_THREE + AMOUNT_FOUR + AMOUNT_FIVE + AMOUNT_SIX
        txt_surface = font.render(str(SUM_1), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_1.x, SUM_BLOCK_1.y))
        if SUM_1 > 63:
           SUM_2 = SUM_1 + 35
           txt_surface = font.render(str(SUM_2), True, color_ONE)
           screen.blit(txt_surface, (SUM_BLOCK_3.x, SUM_BLOCK_3.y))
           txt_surface = font.render(str(35), True, color_ONE)
           screen.blit(txt_surface, (SUM_BLOCK_2.x, SUM_BLOCK_2.y))
        else: 
            SUM_2 = SUM_1
            txt_surface = font.render(str(SUM_2), True, color_ONE)
            screen.blit(txt_surface, (SUM_BLOCK_3.x, SUM_BLOCK_3.y))
            txt_surface = font.render(str(0), True, color_ONE)
            screen.blit(txt_surface, (SUM_BLOCK_2.x, SUM_BLOCK_2.y))
    if AMOUNT_THREE_OF_A_KIND is not None and AMOUNT_FOUR_OF_A_KIND is not None and AMOUNT_FULL_HOUSE is not None and AMOUNT_SMALL_STREET is not None and AMOUNT_BIG_STREET is not None and AMOUNT_KNIFFEL is not None and AMOUNT_CHANCE is not None:
        SUM_4 = (AMOUNT_THREE_OF_A_KIND + AMOUNT_FOUR_OF_A_KIND + AMOUNT_FULL_HOUSE + AMOUNT_SMALL_STREET + AMOUNT_BIG_STREET + AMOUNT_KNIFFEL + AMOUNT_CHANCE)                                                                                          
        txt_surface = font.render(str(SUM_4), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_4.x, SUM_BLOCK_4.y))
    if AMOUNT_ONE != None and AMOUNT_TWO != None and AMOUNT_THREE != None and AMOUNT_FOUR != None and AMOUNT_FIVE != None and AMOUNT_SIX != None and AMOUNT_THREE_OF_A_KIND is not None and AMOUNT_FOUR_OF_A_KIND is not None and AMOUNT_FULL_HOUSE is not None and AMOUNT_SMALL_STREET is not None and AMOUNT_BIG_STREET is not None and AMOUNT_KNIFFEL is not None and AMOUNT_CHANCE is not None:
        txt_surface = font.render(str(SUM_2), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_5.x, SUM_BLOCK_5.y))
        SUM_6= SUM_2 + SUM_4
        txt_surface = font.render(str(SUM_6), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_6.x, SUM_BLOCK_6.y))
        
    
    if AMOUNT_ONE is not None:
        txt_surface = font.render(str(AMOUNT_ONE), True, color_ONE)
        screen.blit(txt_surface, (ONE.x, ONE.y))
        ONE_DONE = True
    if AMOUNT_TWO is not None:
        txt_surface = font.render(str(AMOUNT_TWO), True, color_ONE)
        screen.blit(txt_surface, (TWO.x, TWO.y))
        TWO_DONE = True
    if AMOUNT_THREE is not None:
        txt_surface = font.render(str(AMOUNT_THREE), True, color_ONE)
        screen.blit(txt_surface, (THREE.x, THREE.y))
        THREE_DONE = True
    if AMOUNT_FOUR is not None:
        txt_surface = font.render(str(AMOUNT_FOUR), True, color_ONE)
        screen.blit(txt_surface, (FOUR.x, FOUR.y))
        FOUR_DONE = True
    if AMOUNT_FIVE is not None:
        txt_surface = font.render(str(AMOUNT_FIVE), True, color_ONE)
        screen.blit(txt_surface, (FIVE.x, FIVE.y))
        FIVE_DONE = True
    if AMOUNT_SIX is not None:
        txt_surface = font.render(str(AMOUNT_SIX), True, color_ONE)
        screen.blit(txt_surface, (SIX.x, SIX.y))
        SIX_DONE = True
    if AMOUNT_THREE_OF_A_KIND is not None:
        txt_surface = font.render(str(AMOUNT_THREE_OF_A_KIND), True, color_ONE)
        screen.blit(txt_surface, (THREE_OF_A_KIND.x, THREE_OF_A_KIND.y))
        THREE_OF_A_KIND_DONE = True
    if AMOUNT_FOUR_OF_A_KIND is not None:
        txt_surface = font.render(str(AMOUNT_FOUR_OF_A_KIND), True, color_ONE)
        screen.blit(txt_surface, (FOUR_OF_A_KIND.x, FOUR_OF_A_KIND.y))
        FOUR_OF_A_KIND_DONE = True
    if AMOUNT_FULL_HOUSE is not None:
        txt_surface = font.render(str(AMOUNT_FULL_HOUSE), True, color_ONE)
        screen.blit(txt_surface, (FULL_HOUSE.x, FULL_HOUSE.y))
        FULL_HOUSE_DONE = True
    if AMOUNT_SMALL_STREET is not None:
        txt_surface = font.render(str(AMOUNT_SMALL_STREET), True, color_ONE)
        screen.blit(txt_surface, (SMALL_STREET.x, SMALL_STREET.y))
        SMALL_STREET_DONE = True
    if AMOUNT_BIG_STREET is not None:
        txt_surface = font.render(str(AMOUNT_BIG_STREET), True, color_ONE)
        screen.blit(txt_surface, (BIG_STREET.x, BIG_STREET.y))
        BIG_STREET_DONE = True
    if AMOUNT_KNIFFEL is not None:
        txt_surface = font.render(str(AMOUNT_KNIFFEL), True, color_ONE)
        screen.blit(txt_surface, (KNIFFEL.x, KNIFFEL.y))
        KNIFFEL_DONE = True
    if AMOUNT_CHANCE is not None:
        txt_surface = font.render(str(AMOUNT_CHANCE), True, color_ONE)
        screen.blit(txt_surface, (CHANCE.x, CHANCE.y))
        CHANCE_DONE = True

        
    
     


 

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
