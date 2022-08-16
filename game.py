import pygame
import pandas as pd
import random
import time

import display

word_path = 'data/cleaned_word_list.csv'

global_settings = {
    'num_guesses': 5,
    'num_letters': 6,
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
    'font_size': 80,
    'font_color': (50, 50, 50),
    'keyboard_gap': 10
}

#   Modify the board given the current guess. Return the game status: see
#   'board_status'
def next_guess(board, guess, word):
    empty_row = get_empty_row(board)
    if empty_row < board.shape[0]:
        for i, x in enumerate(guess):
            board[empty_row, i] = guess[i]
        
    return board_status(board, word)

#   Return the index of the first empty row of board, or board.shape[0] if all
#   rows are full
def get_empty_row(board):
    row = 0
    while row < board.shape[0] and board[row, 0] != '':
        row += 1

    return row

#   Given the board and correct (hidden) word, return -1 if all guesses have
#   been exhausted without success, return 0 if the game is in progress, and
#   return 1 if the player has correctly guessed the word
def board_status(board, word):
    empty_row = get_empty_row(board)

    if empty_row == 0:
        #   Totally empty board indicates game is in progress
        return 0
    elif ''.join(board[empty_row - 1, :].tolist()) == word:
        #   If the last row contains the correct word, the player won
        return 1
    elif empty_row == board.shape[0]:
        #   Otherwise if the board is full, the player lost
        return -1
    else:
        #   In all other situations, the game is still going
        return 0


#   Initialize the screen
screen, board = display.start(display_settings)

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
    status = next_guess(board, guess, hidden_word)
    display.display_board(board, screen, display_settings, hidden_word, get_empty_row(board))

#   Show the final screen for a few seconds
time.sleep(5)
