[![Build Status](https://travis-ci.com/neutronimaging/circular_profiler.svg?branch=main)](https://travis-ci.com/neutronimaging/circular_profiler)

Abstract
--------

Notebook/UI to perform circular profile in the shape of a ring over a stack of images

This notebook will allows you to load a set of files (all tiff or fits images from a given folder) and will
bring a user interface to allow you to define a ring. The circular profile will then be calculated along the
ring and integrated over the thickness of the ring, on all the images loaded. 

<img src="/static/demo_of_notebook.gif" />

The output will be an ASCII file with the average counts over the thickness of the ring versus the
angle position, for each of the images loaded.

<img src='/static/preview_of_output.png' />

[Full documentation and step by step tutorial can be found here.](https://neutronimaging.pages.ornl.gov/tutorial/notebooks/circular_profile_of_a_ring/)

# Installation Instructions

We strongly recommend to use conda and create a local environment. To do so, here are the steps

* Install [`Anaconda3`](https://www.anaconda.com/products/individual) or [`miniconda3`](https://docs.conda.io/en/latest/miniconda.html).
  > If one of the two is already installed, skip this step.

## for Mac and Linux

* open a terminal window

* Create a virtual environment for this repo, e.g.
  ```bash
  conda create -n circular_profiler python=3.7
  ```
* Activate the virtual environment with
  ```bash
  conda activate circular_profiler
  ```
* Clone this repository to your local computer with
  ```bash
  git clone https://github.com/neutronimaging/circular_profiler.git
  ```

* Inside the repository, you should be able to find a bash script, `config_conda_env.sh`.  Use it to install required packages with
  ```bash
  bash config_conda_env.sh
  ```
  > NOTE: technically you can run this script in any environment, but it is __highly recommended__ to run it in a virual environment.

* Fire up your terminal, go to the root of this repo, and start the Jupyter notebook server with
  ```bash
  jupyter notebook
  ```
  You will see something similar to the following
  ```bash
    [I 14:00:13.183 NotebookApp] The port 8888 is already in use, trying another port.
    [I 14:00:14.061 NotebookApp] JupyterLab extension loaded from A_REALL_LONG_PATH
    [I 14:00:14.061 NotebookApp] JupyterLab application directory is ANOTHER_LONG_PATH
    [I 14:00:14.063 NotebookApp] Serving notebooks from local directory: CURRNT_DIR
    [I 14:00:14.063 NotebookApp] Jupyter Notebook 6.1.1 is running at:
    [I 14:00:14.063 NotebookApp] http://localhost:8889/?token=1e612467cf5e1e4f91cf074f483010ea7c8de989745eba96
    [I 14:00:14.063 NotebookApp]  or http://127.0.0.1:8889/?token=1e612467cf5e1e4f91cf074f483010ea7c8de989745eba96
    [I 14:00:14.063 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [C 14:00:14.068 NotebookApp] 

    To access the notebook, open this file in a browser:
        file:///home/user/.local/share/jupyter/runtime/nbserver-2560206-open.html
    Or copy and paste one of these URLs:
        http://localhost:8889/?token=1e612467cf5e1e4f91cf074f483010ea7c8de989745eba96
        or http://127.0.0.1:8889/?token=1e612467cf5e1e4f91cf074f483010ea7c8de989745eba96

  ```
  At that point, your favorite browser should show up with the jupyter environment ready to go. 
  If it does not, copy and paste the 6th line of the output to your browser
  ```bash
  http://localhost:8889/?token=1e612467cf5e1e4f91cf074f483010ea7c8de989745eba96
  ```
  and you are ready to use the notebooks.
  > NOTE: For most terminals, you can also `Ctrl+click` or `CMD+click` on the link to open it in your default browser. 

## for Windows



# Meta

Jean Bilheux - bilheuxjm@ornl.gov

Distributed under the BSD license. See LICENSE.txt for more information


# Acknowledgements

This work is sponsored by the Laboratory Directed Research and
Development Program of Oak Ridge National Laboratory, managed by
UT-Battelle LLC, under Contract No. DE-AC05-00OR22725 with the U.S.
Department of Energy. The United States Government retains and the
publisher, by accepting the article for publication, acknowledges
that the United States Government retains a non-exclusive, paid-up,
irrevocable, worldwide license to publish or reproduce the published
form of this manuscript, or allow others to do so, for United States
Government purposes. The Department of Energy will provide public
access to these results of federally sponsored research in accordance
with the DOE Public Access Plan(http://energy.gov/downloads/doe-public-access-plan).

