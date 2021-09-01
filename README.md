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
  ./config_conda_env.sh
  ```
  > NOTE: technically you can run this script in any environment, but it is __highly recommended__ to run it in a virual environment.

* Fire up your terminal, go to the root of this repo, and start the Jupyter notebook server with
  ```bash
  ./launch_notebook.sh
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

# Unit Tests

To run the unit tests, first installed the library

```buildoutcfg
pip install .
```

and then run the tests using **pytest**

```buildoutcfg
pytest
```

# Demonstration

## Demo data used

To illustrate how to use this notebook, we are going to load some fake data from the *test/data/demo* folder.
The fake data are reconstructed, horizontal slices, images of a commercial airplane engine showing the front 
part of the engine where the blades can be found. The **red arrow** shows the location of the 4 slices used here.

<img src='/static/engine_view.png' />

## First step into the notebook

After starting the notebook, you see a first widget **Do not know how to run this notebook? Click Me!** that
will take you to another web page with a detail step by step instruction on how to use this notebook. This
web page will also detail the math behind the various calculations used.

The second widget list the **Notebook rules** in case you are not familiar with the **Jupyter notebooks**. Those
are self-explanatory.

## Setup notebook

Run, (SHIFT + ENTER or click the Run button at the top of the notebook), the cell below **Setup notebook** to 
import the necesary librairies.
The next cell is necessary to be able to bring the user interface to life later on.

## Select folder containing data

Run this cell to select the folder containing the data to use. Detail tutorial of how to use the file
dialog can be found [here](https://neutronimaging.pages.ornl.gov/tutorial/notebooks/file_selector).
By default the file selector takes you from the tests/demo folder. Simply click **Select** to load the folder.

<img src='/static/select_data.png' />

## Launch User Interface

A user interface (UI) will show up, check behind the browser as sometimes the UI stays
behind the current active window.

<img src='/static/user_interface_with_demo_data.png' />

### Selection of rings

A detail tutorial of the UI can be found 
[here](https://neutronimaging.pages.ornl.gov/tutorial/notebooks/circular_profile_of_a_ring/), 
but for the sake of this demo, define a ring center with the cells and having a 
thickness roughly below the lenght of the cells (see next animation).

<img src='/static/selection_of_rings.gif' />

### Calculation of rings profiles

Click the **Calculate Profiles** button to calculate the circular profile of the ring
you just defined. The right part of the UI will expand and will allow you to select the
profile of any of the images loaded. One can then quickly find out that one of the 
blade on image 3 is out of position. Of course this was obvious by just visualizing
the images loaded, but for some cases such as reactor blades, thousands of slices are 
acquired when each slice contains hundreds of blades. Manual visualization of such
a stack of images can take hours or days.

<img src='/static/calculate_profiles.gif' />

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

