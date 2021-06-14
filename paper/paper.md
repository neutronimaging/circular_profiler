---
title: 'Application to perform circular profiles of stack of radiographs'
tags:
  - image processing
  - neutron imaging
authors:
 - name: Jean Bilheux
   orcid: 0000-0003-2172-6487
   affiliation: 1
affiliations:
 - name: Oak Ridge National Laboratory
   index: 1
date: 15 April 2021
bibliography: paper.bib
---

# Summary

Notebook/UI to perform circular profiles in the shape of a ring over a stack of images

This notebook loads a set of files (all tiff or fits images from a given folder). An interface allows the
users to define the position and the size of a ring. Then the circular profile of that rings is calculated and 
integrated over the thickness of the ring. This calculation is repeated over the entire stack of images.

The output is an ASCII file with the average counts over the thickness of the ring versus the
angle position, for each of the images loaded.

# Statement of need

X-ray and neutron community work with TIFF or FITS data files. In some experiment, users need to get a computed
tomography (CT) measurement of their sample. 3D volume of the sample is reconstructed via the use of various
algorithms and software. The analysis of such large volume of data is very time-consuming if done manually. In some
cases the symmetry of the sample allows to automate the analysis and visualization of each slice of the reconstructed
data. For example, the High Flux Isotope Reactor (HFIR) at Oak Ridge National Laboratory (ORNL) uses nuclear cell to 
produce the neutron dedicated to research. Over-heated behavior of the reactor lead to a shutdown of the reactor for
one year. Issues were found to be coming from the welding of the cells. CT of those cells did not shown any obvious 
defects but the visualization of the entire stack of images was done manually. The notebook presented here permitted
to automate the comparisons of each layers and clearly highlight the defects of some of the cells.

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
