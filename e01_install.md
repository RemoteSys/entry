# Introduction

Preparing your computer for the lab requires installing:

1. Python interpreter, one of the methods:
 - download the official [distribution](Python.org)
 - using a package manager for a given system, e.g. apt (Debian), the Microsoft Store (Windows), etc.
 - special distribution such as Miniconda/Anaconda
2. Install text editor (python syntax support function is helpful). Sample open source editors:
 - notepad++ ([url](https://notepad-plus-plus.org/))
 - atom ([url](https://atom.io/))
 - spyder ([url](https://www.spyder-ide.org/))
3. Optional (but recommended):
 - git --fast-version-control ([url](https://git-scm.com/))
---


# Install the official distribution

### Folder location

Folders with software, data, scripts etc. should be located directly on the comupter's disk - examples for the Windows system:
  >- `c:\Program Files\python_no`
  >- where no is Python version number, e.g. `3.12` --> `c:\Program Files\python312`


### Distribution installation

1. Download the latest source [release](https://www.python.org/downloads/) or look for a specific release.
2. Run the installation and follow the appearing tips.
3. For Windows user:
  - select a custom location
  - enter location e.g. `c:\Program Files\python312`
  - do not check the box: `Add python.exe to PATH`
---


# Install Anaconda / Miniconda

### Folder location

Folders with software, data, scripts etc. should be located directly on the comupter's disk - examples for the Windows system:
  >- `c:\Anaconda` - Anaconda installation folder
  >- `c:\Miniconda` - Miniconda installation folder


### Distribution installation

1. Choose versions:
  >- Anaconda page: [package](https://www.anaconda.com/products/distribution)
  >- Miniconda page: [package](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links)
  >- select your operation system ie. Windows:
  >- download the chosen installation 


2. Run the installation and follow the appearing tips:
  >- for Windows: [install](http://docs.anaconda.com/anaconda/install/windows/)  
  >- for Linux: [install](https://docs.anaconda.com/anaconda/install/linux/)  
  >- for macOS: [install](https://docs.anaconda.com/anaconda/install/mac-os/)    
   

### Distribution update
After installing Anaconda:
  >- run Anaconda terminal on Windows:
  >- run terminal on Linux
  >- check conda version:  `conda --version`
  >- update conda manager:  `conda update conda`


### Install extension

In order to be able to operate virtual environments and collaborate with the *conda* manager from the *Jupyter Notebook* level, an additional package must be installed:

I. For notebook >= 7 and jupyterlab >= 4:
1. `nb_conda_kernels`
  >- run terminal: `Anaconda Powershell`
  >- in (base) environment run: `conda install -c conda-forge nb_conda_kernels`

II. For older versions:
1. `nb_extensions`
  >- run terminal
  >- in (base) environment run: `conda install -c conda-forge nb_conda`

2. `jupyter extensions`

In terminal (base) environment run:
  >- `conda install -c conda-forge jupyter_contrib_nbextensions`
  >- `jupyter contrib nbextension install --user`

---

# II. Anaconda / Miniconda


1. What is Anaconda?  
  > It is generally speaking platform for scientific calculations - see [here](https://www.anaconda.com/)

2. What is Miniconda?
  > This is a minimal version of "Anaconda" containing only the "conda" manager - see[here](https://docs.conda.io/en/latest/miniconda.html)
    
2. What is conda?  
  > It is a system for package and environment management open source licenseded - see [here](https://conda.io/docs/)
  
3. Anaconda Didtribution:  see [here](https://www.anaconda.com/distribution/)

4. User guide: see [guide](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)

---
