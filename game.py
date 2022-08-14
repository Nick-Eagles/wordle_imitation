import pygame
import pandas as pd
import random

import display

word_path = 'data/cleaned_word_list.csv'

global_settings = {
    'num_guesses': 4,
    'num_letters': 5,
    'freq_cutoff': 200
}

display_settings = {
    'square_size' : 100,
    'empty_color' : (255, 255, 255),
    'miss_color' : (140, 140, 140),
    'hit_color' : (0, 255, 0),
    'misplace_color' : (255, 255, 0),
    'border_color': (20, 20, 20),
    'board_dimensions': (
        global_settings['num_guesses'], global_settings['num_letters']
    ),
    'font_size': 25,
    'font_color': (50, 50, 50)
}

#   Modify the board given the current guess. Return 1 if there are no guesses
#   left and 0 otherwise
def next_guess(board, guess):
    row = 0
    while row < board.shape[0] and board[row, 0] != '':
        row += 1
    
    if row < board.shape[0]:
        for i, x in enumerate(guess):
            board[row, i] = guess[i]
    
        return 0
    else:
        return 1

#   Initialize the screen
screen, board = display.start(display_settings)
display_settings['font'] = pygame.font.SysFont(None, display_settings['font_size'])

#   Read in word list and filter according to global settings
words = pd.read_csv(word_path)
words['lemma'] = words['lemma'].astype(str)
words = words[
    (words['lemma'].apply(len) == global_settings['num_letters']) & \
    (words['freq'] > global_settings['freq_cutoff'])
]

#   Randomly pick a word
hidden_word = words.iloc[random.randint(0, words.shape[0] - 1)]['lemma']

#   Play wordle
status = 0
while status == 0:
    guess = input('Next guess:')
    status = next_guess(board, guess)
    display.display_board(board, screen, display_settings, hidden_word)
