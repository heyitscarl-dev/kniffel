# scoresheet.py
from typing import Optional, List, Tuple
import pygame

class Category:
    """Represents a single scoring category"""
    def __init__(self, name: str, rect: pygame.Rect):
        self.name = name
        self.rect = rect
        self.score: Optional[int] = None
        self.is_filled = False
    
    def calculate_score(self, dice: List[int]) -> int:
        """Calculate score for this category based on dice values"""
        # Upper section (ones through sixes)
        if self.name in ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]:
            value = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"].index(self.name) + 1
            return dice.count(value) * value
        
        # Three of a kind
        elif self.name == "THREE_OF_A_KIND":
            if any(dice.count(i) >= 3 for i in range(1, 7)):
                return sum(dice)
            return 0
        
        # Four of a kind
        elif self.name == "FOUR_OF_A_KIND":
            if any(dice.count(i) >= 4 for i in range(1, 7)):
                return sum(dice)
            return 0
        
        # Full house
        elif self.name == "FULL_HOUSE":
            has_three = any(dice.count(i) == 3 for i in range(1, 7))
            has_two = any(dice.count(i) == 2 for i in range(1, 7))
            return 25 if (has_three and has_two) else 0
        
        # Small street
        elif self.name == "SMALL_STREET":
            straights = [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}]
            dice_set = set(dice)
            return 30 if any(s.issubset(dice_set) for s in straights) else 0
        
        # Big street
        elif self.name == "BIG_STREET":
            straights = [{1, 2, 3, 4, 5}, {2, 3, 4, 5, 6}]
            dice_set = set(dice)
            return 40 if any(s == dice_set for s in straights) else 0
        
        # Kniffel (Yahtzee)
        elif self.name == "KNIFFEL":
            return 50 if any(dice.count(i) == 5 for i in range(1, 7)) else 0
        
        # Chance
        elif self.name == "CHANCE":
            return sum(dice)
        
        return 0
    
    def fill(self, dice: List[int]) -> None:
        """Fill this category with the calculated score"""
        if not self.is_filled:
            self.score = self.calculate_score(dice)
            self.is_filled = True


class ScoreSheet:
    """Manages one player's score sheet"""
    
    # Layout constants
    BOX_WIDTH = 135 // 2
    BOX_HEIGHT = 80 // 2
    BOX_X = 414 // 2
    BOX_Y = 216 // 2
    SECTION_OFFSET = 20 // 2
    
    def __init__(self, x_offset: int, y_offset: int):
        self.x_offset = x_offset
        self.y_offset = y_offset
        
        self.categories = self._create_categories()
        self.sum_rects = self._create_sum_rects()
        
        self.font = pygame.font.Font(None, 50)
        self.text_color = (0, 0, 0)
    
    def _create_rect(self, box_x: int, box_y: int, offset: int = 0) -> pygame.Rect:
        """Create a rect for a box at given grid position"""
        x = self.x_offset + self.BOX_X + (box_x * self.BOX_WIDTH)
        y = self.y_offset + self.BOX_Y + offset + (box_y * self.BOX_HEIGHT)
        return pygame.Rect(x, y, self.BOX_WIDTH, self.BOX_HEIGHT)
    
    def _create_categories(self) -> dict[str, Category]:
        """Create all scoring categories"""
        categories = {}
        
        # Upper section
        upper_names = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
        for i, name in enumerate(upper_names):
            categories[name] = Category(name, self._create_rect(0, i))
        
        # Lower section
        lower_names = [
            "THREE_OF_A_KIND", "FOUR_OF_A_KIND", "FULL_HOUSE",
            "SMALL_STREET", "BIG_STREET", "KNIFFEL", "CHANCE"
        ]
        for i, name in enumerate(lower_names, start=9):
            categories[name] = Category(name, self._create_rect(0, i, self.SECTION_OFFSET))
        
        return categories
    
    def _create_sum_rects(self) -> dict[str, pygame.Rect]:
        """Create rects for sum display areas"""
        return {
            'upper_sum': self._create_rect(0, 6),
            'bonus': self._create_rect(0, 7),
            'upper_total': self._create_rect(0, 8),
            'lower_sum': self._create_rect(0, 16, self.SECTION_OFFSET),
            'upper_total_repeat': self._create_rect(0, 17, self.SECTION_OFFSET),
            'grand_total': self._create_rect(0, 18, self.SECTION_OFFSET)
        }
    
    def get_upper_sum(self) -> Optional[int]:
        """Calculate upper section sum"""
        upper_names = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
        if all(self.categories[name].is_filled for name in upper_names):
            return sum(self.categories[name].score for name in upper_names)
        return None
    
    def get_bonus(self) -> Optional[int]:
        """Get bonus (35 if upper section >= 63)"""
        upper_sum = self.get_upper_sum()
        return 35 if (upper_sum is not None and upper_sum >= 63) else (0 if upper_sum is not None else None)
    
    def get_upper_total(self) -> Optional[int]:
        """Get upper section total with bonus"""
        upper_sum = self.get_upper_sum()
        bonus = self.get_bonus()
        return upper_sum + bonus if (upper_sum is not None and bonus is not None) else None
    
    def get_lower_sum(self) -> Optional[int]:
        """Calculate lower section sum"""
        lower_names = [
            "THREE_OF_A_KIND", "FOUR_OF_A_KIND", "FULL_HOUSE",
            "SMALL_STREET", "BIG_STREET", "KNIFFEL", "CHANCE"
        ]
        if all(self.categories[name].is_filled for name in lower_names):
            return sum(self.categories[name].score for name in lower_names)
        return None
    
    def get_grand_total(self) -> Optional[int]:
        """Calculate grand total score"""
        upper_total = self.get_upper_total()
        lower_sum = self.get_lower_sum()
        return upper_total + lower_sum if (upper_total is not None and lower_sum is not None) else None
    
    def is_complete(self) -> bool:
        """Check if all categories are filled"""
        return all(cat.is_filled for cat in self.categories.values())
    
    def handle_click(self, pos: Tuple[int, int], dice_values: List[int]) -> bool:
        """Handle click on sheet. Returns True if a category was filled."""
        for category in self.categories.values():
            if category.rect.collidepoint(pos) and not category.is_filled:
                category.fill(dice_values)
                return True
        return False
    
    def get_available_category_at(self, pos: Tuple[int, int]) -> Optional[str]:
        """Get the name of an available category at position, or None"""
        for name, category in self.categories.items():
            if category.rect.collidepoint(pos) and not category.is_filled:
                return name
        return None
    
    def draw(self, surface: pygame.Surface) -> None:
        """Draw all scores on the surface"""
        # Draw category scores
        for category in self.categories.values():
            if category.score is not None:
                text = self.font.render(str(category.score), True, self.text_color)
                surface.blit(text, (category.rect.x, category.rect.y))
        
        # Draw upper section sum
        upper_sum = self.get_upper_sum()
        if upper_sum is not None:
            text = self.font.render(str(upper_sum), True, self.text_color)
            surface.blit(text, self.sum_rects['upper_sum'].topleft)
        
        # Draw bonus
        bonus = self.get_bonus()
        if bonus is not None:
            text = self.font.render(str(bonus), True, self.text_color)
            surface.blit(text, self.sum_rects['bonus'].topleft)
        
        # Draw upper total
        upper_total = self.get_upper_total()
        if upper_total is not None:
            text = self.font.render(str(upper_total), True, self.text_color)
            surface.blit(text, self.sum_rects['upper_total'].topleft)
        
        # Draw lower sum
        lower_sum = self.get_lower_sum()
        if lower_sum is not None:
            text = self.font.render(str(lower_sum), True, self.text_color)
            surface.blit(text, self.sum_rects['lower_sum'].topleft)
        
        # Draw upper total repeat
        if upper_total is not None:
            text = self.font.render(str(upper_total), True, self.text_color)
            surface.blit(text, self.sum_rects['upper_total_repeat'].topleft)
        
        # Draw grand total
        grand_total = self.get_grand_total()
        if grand_total is not None:
            text = self.font.render(str(grand_total), True, self.text_color)
            surface.blit(text, self.sum_rects['grand_total'].topleft)


class ScoreManager:
    """Manages score sheets for multiple players"""
    
    BLOCK_WIDTH = 547
    BLOCK_HEIGHT = 869
    BLOCK_MARGIN = 100
    
    def __init__(self, num_players: int, block_image_path: str, screen_width: int):
        self.num_players = num_players
        self.current_player = 0
        
        # Load and scale block image
        self.block_image = pygame.image.load(block_image_path)
        self.block_image = pygame.transform.scale(
            self.block_image,
            (self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
        )
        
        # Create score sheets
        self.sheets: List[ScoreSheet] = []
        self._create_sheets(screen_width)
    
    def _create_sheets(self, screen_width: int) -> None:
        """Create score sheets positioned for each player"""
        if self.num_players == 1:
            x_offset = self.BLOCK_MARGIN
            self.sheets.append(ScoreSheet(x_offset, 50))
        elif self.num_players == 2:
            # Player 1 on left
            self.sheets.append(ScoreSheet(self.BLOCK_MARGIN, 50))
            # Player 2 on right
            x_offset = screen_width - (self.BLOCK_MARGIN + self.BLOCK_WIDTH)
            self.sheets.append(ScoreSheet(x_offset, 50))
    
    def handle_click(self, pos: Tuple[int, int], dice_values: List[int]) -> bool:
        """Handle click. Returns True if current player filled a category."""
        current_sheet = self.sheets[self.current_player]
        if current_sheet.handle_click(pos, dice_values):
            self.next_player()
            return True
        return False
    
    def get_category_at_click(self, pos: Tuple[int, int]) -> Optional[str]:
        """Get category name at click position for current player"""
        return self.sheets[self.current_player].get_available_category_at(pos)
    
    def next_player(self) -> None:
        """Move to next player"""
        self.current_player = (self.current_player + 1) % self.num_players
    
    def is_game_over(self) -> bool:
        """Check if all sheets are complete"""
        return all(sheet.is_complete() for sheet in self.sheets)

    def get_winner(self) -> Optional[int]:
        """Get player index with highest score, or None if game not over or tied"""
        if not self.is_game_over():
            return None
        
        # Get scores with their indices
        score_pairs = [(i, sheet.get_grand_total()) for i, sheet in enumerate(self.sheets)]
        
        # Filter out any None scores (shouldn't happen if game is complete)
        valid_pairs = [(i, score) for i, score in score_pairs if score is not None]
        
        if not valid_pairs:
            return None
        
        # Find maximum score
        max_score = max(score for _, score in valid_pairs)
        
        # Find all players with max score
        winners = [i for i, score in valid_pairs if score == max_score]
        
        return winners[0] if len(winners) == 1 else None
    
    def draw_backgrounds(self, surface: pygame.Surface) -> None:
        """Draw score sheet background images"""
        if self.num_players == 1:
            surface.blit(self.block_image, (self.BLOCK_MARGIN, 50))
        elif self.num_players == 2:
            surface.blit(self.block_image, (self.BLOCK_MARGIN, 50))
            x_pos = surface.get_width() - (self.BLOCK_MARGIN + self.BLOCK_WIDTH)
            surface.blit(self.block_image, (x_pos, 50))
    
    def draw(self, surface: pygame.Surface) -> None:
        """Draw all score sheets"""
        for sheet in self.sheets:
            sheet.draw(surface)
