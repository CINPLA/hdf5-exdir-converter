[![Build Status](https://travis-ci.org/CINPLA/hdf5-exdir-converter.svg?branch=dev)](https://travis-ci.org/CINPLA/hdf5-exdir-converter)
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](http://www.repostatus.org/badges/latest/wip.svg)](http://www.repostatus.org/#wip)
[![Anaconda-Server Badge](https://anaconda.org/cinpla/hdf5_exdir_converter/badges/installer/conda.svg)](https://anaconda.org/cinpla/hdf5_exdir_converter)
[![codecov](https://codecov.io/gh/CINPLA/hdf5-exdir-converter/branch/dev/graph/badge.svg)](https://codecov.io/gh/CINPLA/hdf5-exdir-converter)

*Important*: The reference implementation contained in this repository is intended for
feedback and as a basis for future library implementations.
It is not ready for production use. Data might be lost.

# hdf5-exdir-converter

A simple hdf5-exdir converter.  

## Installation
```bash
conda install -c cinpla hdf5_exdir_converter
```

## Usage
```bash
hdf2exdir "filename.hdf5" # creates "filename.exdir"
```
or

```bash
exdir2hdf "filename.exdir" # creates "filename.hdf5"
```

The optional argument `--target` can be used to set the target filename.
