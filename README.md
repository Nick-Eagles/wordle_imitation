# wordle_imitation

An imitation of the [Wordle game](https://www.nytimes.com/games/wordle/index.html) with greater customization and no daily play limit.

## Installation

`wordle_imitation` is a collection of python scripts; it is recommended to build a conda environment (or python virtual environment) in which to install dependencies and execute the program. An `environment.yml` is provided in this repository for this purpose.

```
conda env create -f environment.yml
conda activate wordle_env
```

## Usage

A single game of "Wordle" can be played by executing `game.py` (i.e. `python game.py`).

## Configuration

A few gameplay-related settings can be configured, for now by directly modifying [the `global_settings` variable in `game.py`](https://github.com/Nick-Eagles/wordle_imitation/blob/e734b141ac9e6f9e8a6b703b3c76895be3eee084/game.py#L15-L19).

* `num_guesses`: the number of total guesses allowed (default: 6, as in the original Wordle)
* `num_letters`: the number of letters in the hidden word (default: 5, as in the original Wordle). Setting this too high can break the program, if there are no sufficiently long words available.
* `freq_cutoff`: an integer representing the minimum number of times a word must've appeared in the dataset (see "How it works" below) to be acceptable as a hidden word. Acceptable/meaningful values range from 41 to 50M, but the default of 200 seems to result in the broadest set of words that are almost always familiar. This is of course subjective, so raise the value if the hidden words are sometimes unfamiliar, and consider lowering it to allow rare words.

Display settings affecting board coloring and positioning can be similarly changed by editing the [`display_settings` variable in `game.py`](https://github.com/Nick-Eagles/wordle_imitation/blob/e734b141ac9e6f9e8a6b703b3c76895be3eee084/game.py#L21-L34), but this is experimental and defaults should work well.

## How it works

The set of possible hidden words is based on a small set of the [COCA dataset](https://www.english-corpora.org/coca/), made available [here](https://www.wordfrequency.info/samples.asp). The publicly available words from the top 60,000 lemmas, retrieved [here](https://github.com/Nick-Eagles/wordle_imitation/blob/e734b141ac9e6f9e8a6b703b3c76895be3eee084/data/download.sh) are gathered and pre-processed to yield 9,430 potential hidden words. This is further filtered down depending on the user settings `global_settings['num_letters']` and `global_settings['freq_cutoff']`  (see "Configuration") to yield a smaller set of sufficiently common words of the desired length.

The game board is made possible by [`pygame`](https://www.pygame.org).
