# app.py
from enum import Enum
from kniffel import dice, ui, sheet

import pygame

FRAMERATE = 60

class Phase(Enum):
    ROLL = 1
    NOTE = 2
    WAIT = 3

def main() -> None:
    interface = ui.Interface()
    die_group = dice.Dice(5)
    score_manager = sheet.ScoreManager(
        num_players=2,
        block_image_path="scoresheet.jpg",
        screen_width=interface.dimensions.x.__floor__()
    )
    
    phase = Phase.ROLL
    rolls_remaining = 3
    has_rolled = False  # Track if player has rolled at least once
    running = True
    clock = pygame.time.Clock()

    while running:
        dt = clock.tick(FRAMERATE)

        for e in pygame.event.get():
            if (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE
                or e.type == pygame.QUIT):
                running = False
            
            if phase == Phase.ROLL:
                # Can't interact while dice are rolling
                if die_group.is_rolling():
                    continue
                    
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    if rolls_remaining > 0:
                        die_group.roll()
                        rolls_remaining -= 1
                        has_rolled = True
                # Only allow keeping dice if player has rolled at least once
                elif has_rolled:
                    if e.type == pygame.KEYDOWN and e.key == pygame.K_1:
                        die_group.toggle_keep(0)
                    elif e.type == pygame.KEYDOWN and e.key == pygame.K_2:
                        die_group.toggle_keep(1)
                    elif e.type == pygame.KEYDOWN and e.key == pygame.K_3:
                        die_group.toggle_keep(2)
                    elif e.type == pygame.KEYDOWN and e.key == pygame.K_4:
                        die_group.toggle_keep(3)
                    elif e.type == pygame.KEYDOWN and e.key == pygame.K_5:
                        die_group.toggle_keep(4)
                    elif e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                        # Move to scoring phase
                        phase = Phase.NOTE
                    
            elif phase == Phase.NOTE:
                if e.type == pygame.MOUSEBUTTONDOWN:
                    dice_values = die_group.get_values()
                    if score_manager.handle_click(e.pos, dice_values):
                        # Category was filled, check if game is over
                        if score_manager.is_game_over():
                            winner = score_manager.get_winner()
                            if winner is not None:
                                print(f"Player {winner + 1} wins!")
                            else:
                                print("It's a tie!")
                            running = False
                        else:
                            # Move to next player's turn
                            phase = Phase.WAIT
                        
            elif phase == Phase.WAIT:
                if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                    # Start next player's turn
                    phase = Phase.ROLL
                    rolls_remaining = 3
                    has_rolled = False  # Reset for next player
                    die_group.reset()

        die_group.tick(dt)

        interface.prepare()
        
        # Draw score sheet backgrounds
        score_manager.draw_backgrounds(interface.surface)
        
        # Draw score sheets
        score_manager.draw(interface.surface)

        # Draw dice
        interface.surface.blit(die_group.draw(), pygame.Vector2(
            interface.dimensions.x // 2 - dice.DIE_GROUP_WIDTH // 2,
            interface.dimensions.y // 2 - dice.DIE_SIZE // 2
        ))
        
        # Draw centered status text
        font = pygame.font.Font(None, 36)
        center_x = interface.dimensions.x // 2
        
        # Phase and rolls text
        phase_text = font.render(f"Phase: {phase.name} | Rolls: {rolls_remaining}", True, (0, 0, 0))
        phase_rect = phase_text.get_rect(center=(center_x, 30))
        interface.surface.blit(phase_text, phase_rect)
        
        # Player turn text
        player_text = font.render(f"Player {score_manager.current_player + 1}'s turn", True, (0, 0, 0))
        player_rect = player_text.get_rect(center=(center_x, 70))
        interface.surface.blit(player_text, player_rect)
        
        # Show appropriate hint based on game state
        if phase == Phase.ROLL and not has_rolled:
            hint_text = font.render("Press SPACE to roll!", True, (255, 0, 0))
            hint_rect = hint_text.get_rect(center=(center_x, 110))
            interface.surface.blit(hint_text, hint_rect)
        elif phase == Phase.ROLL and has_rolled:
            hint_text = font.render("Press ENTER to complete turn", True, (0, 150, 0))
            hint_rect = hint_text.get_rect(center=(center_x, 110))
            interface.surface.blit(hint_text, hint_rect)
        elif phase == Phase.NOTE:
            hint_text = font.render("Click a category to score", True, (0, 0, 255))
            hint_rect = hint_text.get_rect(center=(center_x, 110))
            interface.surface.blit(hint_text, hint_rect)
        elif phase == Phase.WAIT:
            hint_text = font.render("Press ENTER for next player", True, (150, 0, 150))
            hint_rect = hint_text.get_rect(center=(center_x, 110))
            interface.surface.blit(hint_text, hint_rect)

        interface.finish()

    pygame.quit()

if __name__ == "__main__":
    main()
