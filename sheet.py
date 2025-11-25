import sys, pygame

pygame.init()

BOX_WIDTH, BOX_HEIGHT = 65, 38
BOX_X, BOX_Y = 196, 83

font= pygame.font.Font(None, 50)

COLOR = (0, 0, 0)

def draw_score(font, score, rect):
    surface = font.render(str(score), True, COLOR)
    screen.blit(surface, rect.x, rect.y)

def draw_sheet(offset_x, offset_y, scores: dict[str, int]):
    for category in rects.keys():
        draw_score(font, scores[category], rects[category])

def new_box(image_x, image_y, box_x, box_y):
    x = image_x + BOX_X + (box_x * BOX_WIDTH)
    y = image_y + BOX_Y + (box_y * BOX_HEIGHT)
    return pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)

screen = pygame.display.set_mode ((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
WHITE  =(255,255,255)
BLACK =(0,0,0)

rects = {
    "ones": new_box(100, 100, 0, 0),
    "twos": new_box(100, 100, 0, 1),
    "threes": new_box(100, 100, 0, 2),
    "fours": new_box(100, 100, 0, 3),
    "fives": new_box(100, 100, 0, 4),
    "sixes": new_box (100, 100, 0, 5),
    "presum_upper": new_box (100, 100, 0, 6),
    "bonus_upper": new_box (100, 100, 0, 7),
    "sum_upper": new_box (100, 100, 0, 8),
    "three_of_a_kind": new_box (100, 100, 0, 9),
    "four_of_a_kind": new_box (100, 100, 0, 10),
    "full_house": new_box (100, 100, 0, 11),
    "small_straight": new_box (100, 100, 0, 12),
    "large_straight": new_box (100, 100, 0, 13),
    "kniffel": new_box (100, 100, 0, 14),
    "chance": new_box(100, 100, 0, 15),
    "sum_lower": new_box (100, 100, 0, 16),
    "repeat_sum_upper": new_box (100, 100, 0, 17),
    "sum_total": new_box (100, 100, 0, 18),
}

scores = {
    "ones": None,
    "twos": None,
    "threes": None,
    "fours": None,
    "fives": None,
    "sixes": None,
    "presum_upper": None,
    "bonus_upper": None,
    "sum_upper": None,
    "three_of_a_kind": None,
    "four_of_a_kind": None,
    "full_house": None,
    "small_straight": None,
    "large_straight": None,
    "kniffel": None,
    "chance": None,
    "sum_lower": None,
    "repeat_sum_upper": None,
    "sum_total": None,
}

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

draw_sheet(0, 0, [])

while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.MOUSEBUTTONDOWN and not choice_made:
            if rects["ones"].collidepoint(event.pos) and not ONE_DONE:
                color_ONE = BLACK
                scores["ones"] = Liste.count(1)*1
                choice_made = True
            elif rects["twos"].collidepoint(event.pos) and not TWO_DONE:
                color_ONE = BLACK
                scores["twos"] = Liste.count(2)*2
                choice_made = True
            elif rects["threes"].collidepoint(event.pos) and not THREE_DONE:
                color_ONE = BLACK
                scores["threes"] = Liste.count(3)*3
                choice_made = True
            elif rects["fours"].collidepoint(event.pos) and not FOUR_DONE:
                color_ONE = BLACK
                scores["fours"] = Liste.count(4)*4
                choice_made = True
            elif rects["fives"].collidepoint(event.pos) and not FIVE_DONE:
                color_ONE = BLACK
                scores["fives"]  = Liste.count(5)*5
                choice_made = True
            elif rects["sixes"].collidepoint(event.pos) and not SIX_DONE:
                color_ONE = BLACK
                scores["sixes"]  = Liste.count(6)*6
                choice_made = True
            elif rects["three_of_a_kind"].collidepoint(event.pos) and not THREE_OF_A_KIND_DONE:
                if Liste.count(1) > 2 or Liste.count(2) > 2 or Liste.count(3) > 2 or Liste.count(4) >2 or Liste.count(5) >2 or Liste.count(6) >2:
                    scores["three_of_a_kind"]  = sum(Liste)
                    color_ONE = BLACK
                    choice_made = True
                else:
                    scores["three_of_a_kind"]  = 0
                    color_ONE = BLACK
                    choice_made = True
            elif rects["four_of_a_kind"].collidepoint(event.pos) and not FOUR_OF_A_KIND_DONE:
                if Liste.count(1) > 3 or Liste.count(2) > 3 or Liste.count(3) > 3 or Liste.count(4) >3 or Liste.count(5) >3 or Liste.count(6) >3:
                    scores["four_of_a_kind"]  = sum(Liste)
                    color_ONE = BLACK
                    choice_made = True
                else:
                    scores["four_of_a_kind"]  = 0
                    color_ONE = BLACK
                    choice_made = True
            elif rects["full_house"].collidepoint(event.pos) and not FULL_HOUSE_DONE:     
                if (Liste.count(1) == 3 or Liste.count(2) == 3 or Liste.count(3) == 3 or Liste.count(4) == 3 or Liste.count(5) == 3 or Liste.count(6) == 3) and (Liste.count(1) == 2 or Liste.count(2) == 2 or Liste.count(3) == 2 or Liste.count(4) == 2 or Liste.count(5) == 2 or Liste.count(6) == 2):
                    scores["full_house"] = 25
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    scores["full_house"] = 0
                    color_ONE = BLACK
                    choice_made = True
            elif rects["small_straight"].collidepoint(event.pos) and not SMALL_STREET_DONE:
                if 1 in Liste and 2 in Liste and 3  in Liste and 4 in Liste or 2 in Liste and 3 in Liste and  4 in Liste and 5 in Liste or 3 in Liste and 4 in Liste and 5 in Liste and 6 in Liste:
                    scores["small_straight"] = 30
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    scores["small_straight"] = 0
                    color_ONE = BLACK
                    choice_made = True
            elif rects["large_straight"].collidepoint(event.pos) and not BIG_STREET_DONE:
                if 1 in Liste and 2 in Liste and 3  in Liste and 4 in Liste and 5 in Liste or 2 in Liste and 3 in Liste and  4 in Liste and 5 in Liste and 6 in Liste:
                    scores["large_straight"] = 40
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    scores["large_straight"] = 0
                    color_ONE = BLACK
                    choice_made = True
            elif rects["kniffel"].collidepoint(event.pos) and not KNIFFEL_DONE:
                if Liste.count(1) == 5 or Liste.count(2) == 5 or Liste.count(3) == 5 or Liste.count(4) == 5 or Liste.count(5) == 5 or Liste.count(6) == 5:
                    scores["kniffel"] = 50
                    color_ONE = BLACK
                    choice_made = True
                else: 
                    scores["kniffel"] = 0
                    color_ONE = BLACK
                    choice_made = True  
            elif CHANCE.collidepoint(event.pos) and not CHANCE_DONE:
                scores["chance"] = sum(Liste)
                color_ONE = BLACK
                choice_made = True


    
            
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                Liste = (5,5,5,5,5) 
                choice_made = False
    

                

    if scores["ones"] != None and scores["twos"] != None and scores["threes"] != None and scores["fours"] != None and scores["fives"]  != None and scores["sixes"]  != None:            
        SUM_1 = scores["ones"] + scores["twos"] + scores["threes"] + scores["fours"] + scores["fives"]  + scores["sixes"] 
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
    if scores["three_of_a_kind"]  is not None and scores["four_of_a_kind"]  is not None and scores["full_house"] is not None and scores["small_straight"] is not None and scores["large_straight"] is not None and scores["kniffel"] is not None and scores["chance"] is not None:
        SUM_4 = (scores["three_of_a_kind"]  + scores["four_of_a_kind"]  + scores["full_house"] + scores["small_straight"] + scores["large_straight"] + scores["kniffel"] + scores["chance"])                                                                                          
        txt_surface = font.render(str(SUM_4), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_4.x, SUM_BLOCK_4.y))
    if scores["ones"] != None and scores["twos"] != None and scores["threes"] != None and scores["fours"] != None and scores["fives"]  != None and scores["sixes"]  != None and scores["three_of_a_kind"]  is not None and scores["four_of_a_kind"]  is not None and scores["full_house"] is not None and scores["small_straight"] is not None and scores["large_straight"] is not None and scores["kniffel"] is not None and scores["chance"] is not None:
        txt_surface = font.render(str(SUM_2), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_5.x, SUM_BLOCK_5.y))
        SUM_6= SUM_2 + SUM_4
        txt_surface = font.render(str(SUM_6), True, color_ONE)    
        screen.blit(txt_surface, (SUM_BLOCK_6.x, SUM_BLOCK_6.y))
        
    
    if scores["ones"] is not None:
        txt_surface = font.render(str(scores["ones"]), True, color_ONE)
        screen.blit(txt_surface, (ONE.x, ONE.y))
        ONE_DONE = True
    if scores["twos"] is not None:
        txt_surface = font.render(str(scores["twos"]), True, color_ONE)
        screen.blit(txt_surface, (TWO.x, TWO.y))
        TWO_DONE = True
    if scores["threes"] is not None:
        txt_surface = font.render(str(AMOUNT_THREE), True, color_ONE)
        screen.blit(txt_surface, (THREE.x, THREE.y))
        THREE_DONE = True
    if scores["fours"] is not None:
        txt_surface = font.render(str(AMOUNT_FOUR), True, color_ONE)
        screen.blit(txt_surface, (FOUR.x, FOUR.y))
        FOUR_DONE = True
    if scores["fives"]  is not None:
        txt_surface = font.render(str(scores["fives"] ), True, color_ONE)
        screen.blit(txt_surface, (FIVE.x, FIVE.y))
        FIVE_DONE = True
    if scores["sixes"]  is not None:
        txt_surface = font.render(str(scores["sixes"] ), True, color_ONE)
        screen.blit(txt_surface, (SIX.x, SIX.y))
        SIX_DONE = True
    if scores["three_of_a_kind"]  is not None:
        txt_surface = font.render(str(scores["three_of_a_kind"] ), True, color_ONE)
        screen.blit(txt_surface, (THREE_OF_A_KIND.x, THREE_OF_A_KIND.y))
        THREE_OF_A_KIND_DONE = True
    if scores["four_of_a_kind"]  is not None:
        txt_surface = font.render(str(scores["four_of_a_kind"] ), True, color_ONE)
        screen.blit(txt_surface, (FOUR_OF_A_KIND.x, FOUR_OF_A_KIND.y))
        FOUR_OF_A_KIND_DONE = True
    if scores["full_house"] is not None:
        txt_surface = font.render(str(scores["full_house"]), True, color_ONE)
        screen.blit(txt_surface, (FULL_HOUSE.x, FULL_HOUSE.y))
        FULL_HOUSE_DONE = True
    if scores["small_straight"] is not None:
        txt_surface = font.render(str(scores["small_straight"]), True, color_ONE)
        screen.blit(txt_surface, (SMALL_STREET.x, SMALL_STREET.y))
        SMALL_STREET_DONE = True
    if scores["large_straight"] is not None:
        txt_surface = font.render(str(scores["large_straight"]), True, color_ONE)
        screen.blit(txt_surface, (BIG_STREET.x, BIG_STREET.y))
        BIG_STREET_DONE = True
    if scores["kniffel"] is not None:
        txt_surface = font.render(str(scores["kniffel"]), True, color_ONE)
        screen.blit(txt_surface, (KNIFFEL.x, KNIFFEL.y))
        KNIFFEL_DONE = True
    if scores["chance"] is not None:
        txt_surface = font.render(str(scores["chance"]), True, color_ONE)
        screen.blit(txt_surface, (CHANCE.x, CHANCE.y))
        CHANCE_DONE = True

        
    
     


 

    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
