#!/usr/bin/env bash

# Launching Jupyter Notebook App
jupyter notebook

# INSTALL IPYTHON:
# https://www.codecademy.com/articles/how-to-use-ipython

# HOW I INSTALLED ANACONDA:
# wget https://repo.anaconda.com/archive/Anaconda3-2020.02-MacOSX-x86_64.sh
# chmod 755 Anaconda3-2020.02-MacOSX-x86_64.sh 
# ./Anaconda3-2020.02-MacOSX-x86_64.sh 

wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
chmod 755 Anaconda3-2020.02-Linux-x86_64.sh
./Anaconda3-2020.02-Linux-x86_64.sh
ls anaconda3/
cat .conda/environments.txt 

# CREATE AN ENVIRONMENT
conda create --name cov-41
conda activate cov-41
conda install -c conda-forge vertica-python
conda update -n base -c defaults conda  # update conda
conda deactivate

# https://anaconda.org
