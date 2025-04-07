[![DOI](https://zenodo.org/badge/761710489.svg)](https://zenodo.org/doi/42.4242/zenodo.42424242)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# Differentiable Simulations Cheetah Tutorial MaLAPA 2025

_"Differentiable Simulations"_ tutorial presented at the _5th MaLAPA workshop_ at CERN in April 2025.

## Disclaimer &#x2757;

This repository contains advanced Python tutorials developed with care and dedication to foster learning and collaboration. The code and materials provided here are the result of significant effort, including state-of-the-art research and unpublished or pre-peer-reviewed work.

We share these resources in good faith, aiming to contribute to the community and advance knowledge in our field. If you use or build upon any part of this tutorial, whether in research, software, or educational materials, proper citation is required. Please cite the tutorial as indicated in the repository or its associated Zenodo entry.

While we encourage reuse and adaptation of our work, uncredited use or plagiarism is unacceptable. We actively monitor citations and expect users to engage in responsible scholarly practice. Failure to properly attribute this work may lead to formal actions.

By using this repository, you acknowledge and respect the effort behind it. We appreciate your support in maintaining academic integrity and fostering an open, collaborative environment.

Happy coding, and thank you for citing responsibly! 😊

## Getting Started

- You will require about **3 GB of free disk space** &#x2757;
- Make sure you have Git installed in your terminal &#x2757;

Start by cloning locally the repository of the challenge by running this command in your terminal:

```bash
git clone https://github.com/MALAPA-Collab/cheetah-tutorial-2025
```

Then enter the downloaded repository:

```bash
cd cheetah-tutorial-2025
```

### Installing virtual environment

#### Using conda-forge

- If you don't have conda installed already, you can install the `miniforge` as described in the [GitHub repository](https://github.com/conda-forge/miniforge) or download from the [conda-forge site](https://conda-forge.org/download/). Once `miniforge` is installed, you can use the `conda` commands as usual.
- We recommend installing `miniforge` the day beforehand to avoid network overload during the challenge &#x2757; &#x2757;

Once `miniforge` is installed run this command in your terminal:

```bash
conda env create -f environment.yaml
```

Afterwards, activate the environment with `conda activate malapa-cheetah-tutorial-2025`

Now you should be able to run the provided notebook.

## Running the tutorial

After installing the package

You can start the jupyter notebook in the terminal, and it will start a browser automatically

```bash
python -m jupyter notebook
```

Alternatively, you can use supported Editor to run the jupyter notebooks, e.g. with VS Code.

---

## Citing the tutorial

This tutorial is uploaded to [Zenodo](https://zenodo.org/doi/42.4242/zenodo.42424242).
Please use the following DOI when citing this code:

```bibtex
@software{kaiser2025differentiable,
    title        = {Differentiable Simulations {Cheetah} Tutorial {MaLAPA} 2025},
    author       = {Kaiser, Jan and Xu, Chenran and {Santamaria Garcia}, Andrea and {Gonzalez Aguilera}, Juan Pablo},
    year         = 2025,
    month        = {04},
    publisher    = {Zenodo},
    doi          = {42.4242/zenodo.42424242},
    url          = {https://doi.org/42.4242/zenodo.42424242},
    version      = {v1.0.0}
}
```

## Acknowledgement

This tutorial is developed by [Jan Kaiser](https://github.com/jank324), [Chenran Xu](https://github.com/cr-xu), [Andrea Santamaria Garcia](https://github.com/ansantam), and [Juan Pablo Gonzalez Aguilera](https://github.com/jp-ga).

The content is based on the [official Cheetah documentation](https://cheetah-accelerator.readthedocs.io/en/latest/), [Cheetah PRAB paper](https://doi.org/10.1103/PhysRevAccelBeams.27.054601), the [Cheetah Demos repository](https://github.com/desy-ml/cheetah-demos), and the [GPSR (generative phase space reconstruction) package](https://github.com/roussel-ryan/gpsr).
