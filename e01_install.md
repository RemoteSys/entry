<style>
r { color: red }
</style>


# Preparing the computer for the laboratory
---

1. Install Anaconda or Miniconda distribution - see section [Installing](#installing).
2. Install text editor (python syntax support function is helpful). Sample open source editors:
 - [notepad++](https://notepad-plus-plus.org/).
 - [atom](https://atom.io/).
 - [spyder](https://www.spyder-ide.org/)

---

# Install Anaconda / Miniconda

## Folder location

Folders with software, data, scripts etc. should be located directly on the comupter's disk - examples for the Windows system:
  >- `c:\Anaconda` - Anaconda installation folder
  >- `c:\Miniconda` - Miniconda installation folder

## Distribution installation

1. Choose versions:
  >- Anaconda page: [package](https://www.anaconda.com/products/distribution)
  >- Miniconda page: [package](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links)
  >- select your operation system ie. Windows:
  >- download the chosen installation 


2. Run the installation and follow the appearing tips:
  >- for Windows: [install](http://docs.anaconda.com/anaconda/install/windows/)  
  >- for Linux: [install](https://docs.anaconda.com/anaconda/install/linux/)  
  >- for macOS: [install](https://docs.anaconda.com/anaconda/install/mac-os/)    
   

## Distribution update
After installing Anaconda:
  >- run Anaconda terminal on Windows:
  >- run terminal on Linux
  >- check conda version:  `conda --version`
  >- update conda manager:  `conda update conda`
  >- update of Anaconde:  `conda update anaconda`


## Install extension

In order to be able to operate virtual environments and collaborate with the *conda* manager from the *Jupyter Notebook* level, an additional package must be installed:

1. `nb extensions`
  >- run terminal
  >- in (base) environment run: `conda install nb_conda`
or or if you get any errors try to use conda-forge:
  >- `conda install -c conda-forge nb_conda`

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
