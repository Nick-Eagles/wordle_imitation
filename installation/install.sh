#   Commands initially used to isolate python + dependencies while developing.

#   Create a basic environment with just python
conda create -y -p $PWD/wordle_env python=3.8

#   Add packages we'll need
conda activate $PWD/wordle_env
python -m pip install pandas openpyxl pygame
conda deactivate
