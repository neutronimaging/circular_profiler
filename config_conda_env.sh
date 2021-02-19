#!/bin/bash

# update base conda
conda update -y -n base -c defaults conda

# install dependencies from main channel
conda install -y      \
    numpy             \
    scipy             \
    pandas            \
    scikit-image      \
    matplotlib        \
    jupyter           \
    jupyterlab        \
    nodejs            \
    qtpy              \
    pyqtgraph         \
    astropy

# install dependencies from conda-forge
conda install -y -c conda-forge \
    ipywe

# install additional from pip
pip install \
    NeuNorm \
    inflect \
    ipywidgets \
    $PYONCAT_LOCATION

# build Jupyter lab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter nbextension enable --py widgetsnbextension
jupyter lab build
