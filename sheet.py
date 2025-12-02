import pygame

class KniffelGame:
    BOX_WIDTH, BOX_HEIGHT = 135 // 2, 80 // 2
    BOX_X, BOX_Y = 414 // 2, 216 // 2
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.font = pygame.font.Font(None, 50)
        self.running = True
        self.choice_made = False
        self.dice = [1, 1, 1, 4, 4]
        
        # Load and scale image
        self.block = pygame.image.load("Kniffel-Block-3.jpg")
        self.block = pygame.transform.scale(self.block, (547, 869))
        
        # Versetzung um die Lücke in dem Block auszugleichen
        self.gap_offset = 20 // 2

        # Create rectangles for clickable areas
        self.boxes = {
            'ONE': self.new_box(100, 50, 0, 0),
            'TWO': self.new_box(100, 50, 0, 1),
            'THREE': self.new_box(100, 50, 0, 2),
            'FOUR': self.new_box(100, 50, 0, 3),
            'FIVE': self.new_box(100, 50, 0, 4),
            'SIX': self.new_box(100, 50, 0, 5),
            'SUM_BLOCK_1': self.new_box(100, 50, 0, 6),
            'SUM_BLOCK_2': self.new_box(100, 50, 0, 7),
            'SUM_BLOCK_3': self.new_box(100, 50, 0, 8),
            'THREE_OF_A_KIND': self.new_box(100, 50 + self.gap_offset, 0, 9),
            'FOUR_OF_A_KIND': self.new_box(100, 50 + self.gap_offset, 0, 10),
            'FULL_HOUSE': self.new_box(100, 50 + self.gap_offset, 0, 11),
            'SMALL_STREET': self.new_box(100, 50 + self.gap_offset, 0, 12),
            'BIG_STREET': self.new_box(100, 50 + self.gap_offset, 0, 13),
            'KNIFFEL': self.new_box(100, 50 + self.gap_offset, 0, 14),
            'CHANCE': self.new_box(100, 50 + self.gap_offset, 0, 15),
            'SUM_BLOCK_4': self.new_box(100, 50 + self.gap_offset, 0, 16),
            'SUM_BLOCK_5': self.new_box(100, 50 + self.gap_offset, 0, 17),
            'SUM_BLOCK_6': self.new_box(100, 50 + self.gap_offset, 0, 18),
        }
        
        # Initialize scores dictionary
        self.scores = {
            'ONE': None, 'TWO': None, 'THREE': None,
            'FOUR': None, 'FIVE': None, 'SIX': None,
            'THREE_OF_A_KIND': None, 'FOUR_OF_A_KIND': None,
            'FULL_HOUSE': None, 'SMALL_STREET': None,
            'BIG_STREET': None, 'KNIFFEL': None, 'CHANCE': None
        }
    
    def new_box(self, image_x: int, image_y: int, box_x: int, box_y: int) -> pygame.Rect:
        x = image_x + self.BOX_X + (box_x * self.BOX_WIDTH)
        y = image_y + self.BOX_Y + (box_y * self.BOX_HEIGHT)
        return pygame.Rect(x, y, self.BOX_WIDTH, self.BOX_HEIGHT)
    
    def calculate_score(self, category: str) -> int:
        """Calculate the score for a given category based on current dice"""
        if category in ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']:
            value = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX'].index(category) + 1
            return self.dice.count(value) * value
        elif category == 'THREE_OF_A_KIND':
            if any(self.dice.count(i) >= 3 for i in range(1, 7)):
                return sum(self.dice)
            return 0
        elif category == 'FOUR_OF_A_KIND':
            if any(self.dice.count(i) >= 4 for i in range(1, 7)):
                return sum(self.dice)
            return 0
        elif category == 'FULL_HOUSE':
            counts = [self.dice.count(i) for i in range(1, 7)]
            if 3 in counts and 2 in counts:
                return 25
            return 0
        elif category == 'SMALL_STREET':
            sorted_dice = sorted(set(self.dice))
            straights = [[1,2,3,4], [2,3,4,5], [3,4,5,6]]
            if any(all(d in sorted_dice for d in straight) for straight in straights):
                return 30
            return 0
        elif category == 'BIG_STREET':
            sorted_dice = sorted(set(self.dice))
            if sorted_dice == [1,2,3,4,5] or sorted_dice == [2,3,4,5,6]:
                return 40
            return 0
        elif category == 'KNIFFEL':
            if any(self.dice.count(i) == 5 for i in range(1, 7)):
                return 50
            return 0
        elif category == 'CHANCE':
            return sum(self.dice)
        return 0
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.choice_made:
                # Check which category was clicked
                for category, box in self.boxes.items():
                    if category.startswith('SUM'):  # Skip sum blocks
                        continue
                    if box.collidepoint(event.pos) and self.scores[category] is None:
                        self.scores[category] = self.calculate_score(category)
                        self.choice_made = True
                        break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.dice = [5, 5, 5, 5, 5]
                    self.choice_made = False
    
    def draw(self):
        """Draw everything on screen"""
        self.screen.fill(self.WHITE)
        self.screen.blit(self.block, (100, 50))
        
        # Draw individual scores
        for category, score in self.scores.items():
            if score is not None:
                txt_surface = self.font.render(str(score), True, self.BLACK)
                box = self.boxes[category]
                self.screen.blit(txt_surface, (box.x, box.y))
        
        # Draw upper section sum
        upper_scores = [self.scores[cat] for cat in ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX']]
        if all(s is not None for s in upper_scores):
            sum_1 = sum(upper_scores)
            txt_surface = self.font.render(str(sum_1), True, self.BLACK)
            self.screen.blit(txt_surface, (self.boxes['SUM_BLOCK_1'].x, self.boxes['SUM_BLOCK_1'].y))
            
            # Bonus
            bonus = 35 if sum_1 >= 63 else 0
            txt_surface = self.font.render(str(bonus), True, self.BLACK)
            self.screen.blit(txt_surface, (self.boxes['SUM_BLOCK_2'].x, self.boxes['SUM_BLOCK_2'].y))
            
            # Upper total with bonus
            sum_2 = sum_1 + bonus
            txt_surface = self.font.render(str(sum_2), True, self.BLACK)
            self.screen.blit(txt_surface, (self.boxes['SUM_BLOCK_3'].x, self.boxes['SUM_BLOCK_3'].y))
            
            # Draw lower section sum
            lower_scores = [self.scores[cat] for cat in ['THREE_OF_A_KIND', 'FOUR_OF_A_KIND', 'FULL_HOUSE', 'SMALL_STREET', 'BIG_STREET', 'KNIFFEL', 'CHANCE']]
            if all(s is not None for s in lower_scores):
                sum_4 = sum(lower_scores)
                txt_surface = self.font.render(str(sum_4), True, self.BLACK)
                self.screen.blit(txt_surface, (self.boxes['SUM_BLOCK_4'].x, self.boxes['SUM_BLOCK_4'].y))
                
                # Upper total (repeated)
                txt_surface = self.font.render(str(sum_2), True, self.BLACK)
                self.screen.blit(txt_surface, (self.boxes['SUM_BLOCK_5'].x, self.boxes['SUM_BLOCK_5'].y))
                
                # Grand total
                sum_6 = sum_2 + sum_4
                txt_surface = self.font.render(str(sum_6), True, self.BLACK)
                self.screen.blit(txt_surface, (self.boxes['SUM_BLOCK_6'].x, self.boxes['SUM_BLOCK_6'].y))
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
