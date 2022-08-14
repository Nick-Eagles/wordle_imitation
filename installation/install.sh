#   Commands initially used to isolate python + dependencies while developing.
#   When the project is further along, we'll provide an 'environment.yml' file
#   and recommend creation of a conda environment.

#   Create a basic environment with just python
conda create -y -p $PWD/wordle_env python=3.8

#   Add packages we'll need
conda activate $PWD/wordle_env
python -m pip install pandas
python -m pip install openpyxl
conda deactivate
