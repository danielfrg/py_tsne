# Python-TSNE

[![PyPI](https://badge.fury.io/py/tsne.svg)](https://pypi.org/project/tsne/)
![Testing](http://github.com/danielfrg/tsne/workflows/testing/badge.svg)
[![License](http://img.shields.io/:license-Apache%202-blue.svg)](http://github.com/danielfrg/tsne/blob/master/LICENSE.txt)

Python library containing T-SNE algorithms.

**Note:** [Scikit-learn v0.17](http://scikit-learn.org/stable/whats_new.html#version-0-17)
includes TSNE algorithms and you should probably be using that instead.

## Algorithms

### Barnes-Hut-SNE

A python ([cython](http://www.cython.org)) wrapper for [Barnes-Hut-SNE](http://homepage.tudelft.nl/19j49/t-SNE.html) aka fast-tsne.

I basically took [osdf's code](https://github.com/osdf/py_bh_tsne) and made it pip compliant.

## Requirements

* [numpy](numpy.scipy.org) > =1.7.1
* [scipy](http://www.scipy.org/) >= 0.12.0
* [cython](cython.org) >= 0.19.1
* [cblas](http://www.netlib.org/blas/) or [openblas](https://github.com/xianyi/OpenBLAS). Tested version is v0.2.5 and v0.2.6 (not necessary for OSX).

[Anaconda](http://continuum.io/downloads) is recommended.

## Installation

From PyPI:

```
pip install tsne
```

From conda:

```
conda install -c maxibor tsne
```

## Usage

Basic usage:

```python
from tsne import bh_sne
X_2d = bh_sne(X)
```

### Examples

- [Iris](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/iris.ipynb)
- [MNIST](http://nbviewer.ipython.org/urls/raw.github.com/danielfrg/py_tsne/master/examples/mnist.ipynb)
- [word2vec on presidential speeches](https://github.com/prateekpg2455/U.S-Presidential-Speeches) via [@prateekpg2455](https://github.com/prateekpg2455)

## More Information

See *Barnes-Hut-SNE* (2013), L.J.P. van der Maaten. It is available on [arxiv](http://arxiv.org/abs/1301.3342).
