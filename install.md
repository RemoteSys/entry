<style>
r { color: red }
</style>


# Preparing the computer for the laboratory
---

1. Install Anaconda distribution - see section [Installing](#installing).
2. Install text editor (python syntax support function is helpful). Sample open source editors:
- [notepad++](https://notepad-plus-plus.org/).
- [atom](https://atom.io/).
- [spyder](https://www.spyder-ide.org/) - available after installing Anaconda distribution.

---

# I. General remarks

### Paths to directories / files
In Windows, the addresses (paths) of files / folders can be entered in various ways:
 >- `c:\someFolder` - with a single `\` character
 >- `c:\\someFolder` - using the double `\ \`
 >- `c:/someFolder` - with a single character `/`

Check which method works for your computer.


### Folder location

Folders with software, data, scripts etc. should be located directly on the comupter's disk - examples for the Windows system:
 >- `c:\Anaconda` - Anaconda installation folder
 >- `c:\someName` - working directory where data, scripts, etc. will be placed, e.g. `c:\myPython`

A directory  structure should be created in the working directory, e.g .:
 >- c:\myPython\data
 >- c:\myPython\images
 >- c:\myPython\notebooks

### File and directory names

Directory and file names should:
 >- be as short as possible
 >- do not contain special characters, e.g. `*,.,?, $` or 'empty' characters such as `spaces` or `tabs`
 >- do not contain diacritical signs such as `ę, ó,...` and the like
 >- start with letters, not numbers 
---

# II. Anaconda 


1. What is Anaconda?  
  > It is generally speaking platform for scientific calculations - see [here](https://www.anaconda.com/what-is-anaconda/)
    
2. What is conda?  
  >It is a system for package and environment management open source licenseded - see [here](https://conda.io/docs/)
  
3. Anaconda Didtribution:  see [here](https://www.anaconda.com/distribution/)

4. User guide: see [guide](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html)



## Installing

1. Download the chosen installation [package](https://www.anaconda.com/products/individual):

    >- select your operation system ie. Windows:


2. Run the installation and follow the appearing tips:
   >- for Windows: [install](http://docs.anaconda.com/anaconda/install/windows/)  
   >- for Linux: [install](https://docs.anaconda.com/anaconda/install/linux/)  
   >- for macOS: [install](https://docs.anaconda.com/anaconda/install/mac-os/)    
   

3. After installing Anaconda:
   >- run Anaconda terminal on Windows:
   >- run terminal on Linux
   >- check conda version:  `conda --version`
   >- update conda manager:  `conda update conda`
   >- update of Anaconde:  `conda update anaconda`


4. Install conda extension

In order to be able to operate virtual environments and collaborate with the *conda* manager from the *Jupyter Notebook* level, an additional package must be installed:

  >- run terminal
  >- in (base) environment run: `conda install nb_conda`
or or if you get any errors try to use conda-forge:
  >- `conda install -c conda-forge nb_conda`
  >- in (base) environment run: `conda install -c conda-forge jupyter_contrib_nbextensions`

---
# III. Conda environments and packages management

## 1 . Management of environments

For each project we advice to create separate environment with installed needed packages. Basic commands [help]( https://conda.io/docs/user-guide/tasks/manage-environments.html):

   >- `conda create  -n name_of_environment` - create an environment called name_of_environment
   >- `conda create -n name_of_environment python=3.6.6` - create an environment called name_of_environment, with the indicated Python version
  
   >- `conda remove -n name_of_environment --all` environment remove
   >- `activate name_of_environment*` - activating the environment on Windows
   >- `conda activate name_of_environment` - activating the environment on Linux
   >- `deactivate deactivating`- the environment on Windows
   >- `conda deactivate deactivating` - the environment on Linux
   >- `conda info --envs / conda info -e` - displaying a list of available environments
       

## 2. Packages management

Basic commands [help](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html):

   >- `conda list` - check the list installed packages in current environment sprawdzenie  
   >- `conda list | findstr package_name` - search for packages installed in the current environment using the stream | and console command **findstr** - on Windows  
   >- `conda list | grep package_name` - search for packages installed in the current environment using the stream | and console command **grep** - on Linux  
   >- `conda install package_name` - installs package in current environment  
   >- `conda remove package_name` - remove package from current environment  


## 3. `yaml` file 

To create or update the environment, you can use a text file with a list of necessary modules. This file is saved in the `yaml` format. Let's assume that the file `myModules.yaml` contains a list of modules:

   >- `conda env create -f myModules.yaml` - creates a new environment [see here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
   >- `conda env update -f myModules.yaml` - updates the environment

### Example of `yaml` file

```yaml
name: stats2
channels:
   - conda-forge
dependencies:  
   - python=3.6
   - numpy
   - pandas
```

About [yaml](https://en.wikipedia.org/wiki/YAML) file.


## 4. First virtual environment

1. Run terminal (`Anaconda prompt`)
2. Create new environment: `conda create -n lab1`
3. Activate environment: `conda activate lab1`
3. Install pakages:

  >- **ipython**: to work with *ipython* terminal
    `conda install -c anaconda ipython`

 >- **ipython and ipykernel** - to work with *jupyter notebook*
    `conda install -c anaconda ipython  ipykernel` 



## <r>Technical note:</r>

 - Date: 2021.03.15
 - Topic: Problems have been found with ipython 7.18 / 7.19 and jedi. These packages should be installed in versions:
    - <r>ipython=7.21</r>
    - <r>jedi=0.17.2 </r>


---
# IV. Tools

Ipython:
   >In simple terms, it is a modern, interactive Python interpreter console. In fact, Ipython is something much bigger - [here](https://ipython.org/ipython-doc/stable/overview.html) you can read about it.  

Jupyter Notebook:  
   >formerly known as *Ipython Notebok*, it is an interactive computational environment, in which you can combine code execution, rich text, mathematics, plots and rich media. 


## Jupyter notebook

1. First steps: [DataCamp tutorials](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)
2. Jupiter uses markdown: [Some tutorial](https://commonmark.org/help/)


---
# V. Miscellaneous

## 1. Dark theme for Jupyter Notebook
> Details see [GitHub](https://github.com/dunovank/jupyter-themes)  project  
>and [Anaconda Cloud](https://anaconda.org/conda-forge/jupyterthemes) how to install

1. Run terminal (`base` environment)
2. Install: `conda install -c conda-forge jupyterthemes`
3. Use: 

    - `jt -l` - list themes   
    - `jt -t theme_name` - select theme
    - `jupyter notebook` - run jupyter
    - `jt -r` - restore default theme

4. Requirements: the `Stylish` browser extension (available for Chrome, Firefox).




