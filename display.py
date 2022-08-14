import pygame
import numpy as np

#   Given display settings, return (screen, board)
def start(display_settings):
    #   Initialize the display
    pygame.init()
    screen = pygame.display.set_mode((
        display_settings['board_dimensions'][1] * display_settings['square_size'],
        display_settings['board_dimensions'][0] * display_settings['square_size']
    ))
    
    return (screen, np.full(display_settings['board_dimensions'], ''))

#   Update the display given the current game board
def display_board(game_board, screen, display_settings, word):
    assert len(word) == game_board.shape[1], "Incorrect word length for board."
    
    #   Draw the squares containing each letter
    for row in range(display_settings['board_dimensions'][0]):
        for col in range(display_settings['board_dimensions'][1]):
            #   Color this square appropriately based on Wordle rules
            if game_board[row, col] == '':
                color = display_settings['empty_color']
            elif game_board[row, col] == word[col]:
                color = display_settings['hit_color']
            elif game_board[row, col] in word:
                color = display_settings['misplace_color']
            else:
                color = display_settings['miss_color']
            
            #   Draw this square
            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    col * display_settings['square_size'],
                    row * display_settings['square_size'],
                    display_settings['square_size'], 
                    display_settings['square_size']
                )
            )
            
            #   Add the letter in the center of the square
            if game_board[row, col] != '':
                text = display_settings['font'].render(
                    game_board[row, col], True, display_settings['font_color']
                )
                screen.blit(
                    text, 
                    (
                        (col + 0.5) * display_settings['square_size'],
                        (row + 0.5) * display_settings['square_size']
                    )
                )
    
    #   Draw horizontal lines to divide the squares visually
    for row in range(1, display_settings['board_dimensions'][0]):
        pygame.draw.line(
            screen,
            display_settings['border_color'],
            (0, row * display_settings['square_size']),
            (
                display_settings['board_dimensions'][1] * display_settings['square_size'],
                row * display_settings['square_size']
            )
        )
    
    #   Draw vertical lines to divide the squares visually
    for col in range(1, display_settings['board_dimensions'][1]):
        pygame.draw.line(
            screen,
            display_settings['border_color'],
            (col * display_settings['square_size'], 0),
            (
                col * display_settings['square_size'],
                display_settings['square_size'] * display_settings['board_dimensions'][0]
            )
        )
    pygame.display.update()
