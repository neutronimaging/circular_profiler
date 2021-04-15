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


# Statement of need

Notebook/UI to perform circular profiles in the shape of a ring over a stack of images

This notebook allows to load a set of files (all tiff or fits images from a given folder) and brings a user interface, used to define 
the position and size of a ring. The circular profile of that rings is calculated and integrated over the thickness of the ring. This
calculation is performed for all the images loaded.

The output is an ASCII file with the average counts over the thickness of the ring versus the
angle position, for each of the images loaded.

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
