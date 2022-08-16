import pygame
import numpy as np

KEYBOARD = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

#   Given display settings, return (screen, board)
def start(display_settings):
    keyboard_width = max([len(x) for x in KEYBOARD]) / 2
    width = (display_settings['board_dimensions'][1] + keyboard_width) * display_settings['square_size'] + display_settings['keyboard_gap']

    #   Initialize the display
    pygame.init()
    screen = pygame.display.set_mode(
        (
            width,
            (display_settings['board_dimensions'][0] + 1.5) * display_settings['square_size']
        )
    )
    
    return (screen, np.full(display_settings['board_dimensions'], ''))

#   Update the display given the current game board
def display_board(game_board, screen, display_settings, word, empty_row):
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
            draw_square(
                screen,
                (
                    col * display_settings['square_size'],
                    row * display_settings['square_size']
                ),
                display_settings['square_size'], color, game_board[row, col],
                display_settings['font_size'], display_settings['font_color']
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

    for r, row in enumerate(KEYBOARD):
        for c, letter in enumerate(row):
            #   Color this square appropriately based on Wordle rules
            if empty_row == 0:
                color = display_settings['empty_color']
            elif any([(game_board[empty_row - 1, x] == letter) and (game_board[empty_row - 1, x] == word[x]) for x in range(game_board.shape[1])]):
                color = display_settings['hit_color']
            elif any([(game_board[empty_row - 1, x] == letter) and (game_board[empty_row - 1, x] in word) for x in range(game_board.shape[1])]):
                color = display_settings['misplace_color']
            elif letter in game_board:
                color = display_settings['miss_color']
            else:
                color = display_settings['empty_color']

            draw_square(
                screen,
                (
                    c * display_settings['square_size'] / 2 + display_settings['square_size'] * display_settings['board_dimensions'][1] + display_settings['keyboard_gap'],
                    r * display_settings['square_size'] / 2
                ),
                display_settings['square_size'] / 2,
                color, letter,
                display_settings['font_size'] / 2, display_settings['font_color']
            )

    pygame.display.update()

def draw_square(screen, start, square_size, square_color, letter, font_size, font_color):
    #   Draw this square
    pygame.draw.rect(
        screen,
        square_color,
        pygame.Rect(start[0], start[1], square_size, square_size)
    )
    
    #   Add the letter in the center of the square
    text = pygame.font.SysFont(None, int(font_size)).render(
        letter.upper(), True, font_color
    )
    if text != '':
        screen.blit(
            text, 
            (
                start[0] + 0.5 * square_size - font_size / 4,
                start[1] + 0.5 * square_size - font_size / 4
            )
        )
