import pygame
import display

display_settings = {
    'square_size' : 100,
    'empty_color' : (255, 255, 255),
    'miss_color' : (140, 140, 140),
    'hit_color' : (0, 255, 0),
    'misplace_color' : (255, 255, 0),
    'border_color': (20, 20, 20),
    'board_dimensions': (5, 7),
    'font': pygame.font.SysFont(None, 25),
    'font_color': (50, 50, 50)
}

screen, board = start(display_settings)
display_board(board, screen, display_settings, 'aaadfgr')
