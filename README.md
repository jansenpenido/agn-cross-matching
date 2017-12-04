# AGN Cross-matching
This application was developed for Coursera's [Data-driven Astronomy](https://www.coursera.org/learn/data-driven-astronomy) course.


## Overview
When investigating astronomical objects, like [active galactic nuclei (AGN)](https://en.wikipedia.org/wiki/Active_galactic_nucleus), astronomers compare data about those objects from different telescopes at different wavelengths.

This repository demonstrates how to use Python to cross-match AGN readings from two catalogues: one from a radio survey, the [AT20G Bright Source Sample (BSS) catalogue](http://cdsarc.u-strasbg.fr/viz-bin/Cat?J/MNRAS/384/775) and one from an optical survey, the [SuperCOSMOS all-sky galaxy catalogue](http://ssa.roe.ac.uk/allSky).

## Usage
The `crossmatch()` function returns a list of matches and non-matches for the first catalogue against the second. The list of matches contains tuples of the first and second catalogue object IDs and their distance. The list of non-matches contains the unmatched object IDs from the first catalogue only. 

## Requirements
* [Numpy](http://www.numpy.org/)


## Author
[Jansen Penido](https://about.me/jansen.penido)
