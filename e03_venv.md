# Virtual environments

The scripts will be run (installed) in two types of virtual environments:
 - `venv` environment. Documentation for the `venv` module can be found [here](https://docs.python.org/3/library/venv.html).
 - `conda` environmentis

The basic commands for managing virtual environments are listed below.
---


### Venv commands
1. Creating environments
 - `python -m venv environment_name`
 - environment activation:
   + Windows: `environment_name/Scripts/activate`
   + Linux: `source environment_name/bin/activate`
 - `deactivate`

2. Installing the modules:
 - `python -m pip install module_1 module_2 ...`

3. Installed modules
 - `requirements.txt` - file containing a list of modules installed in the environment in
   [pip txt format](https://pip.pypa.io/en/stable/reference/requirements-file-format/#requirements-file-format)
 - `python -m pip install -r requirements.txt` - installs the modules listed in the file
 - `python -m pip freeze > requirements.txt` - creates a list of modules installed in the virtual environment
---


### Conda commands
1. Creating environments:
 - `conda create -n environment_name`
 - `conda activate environment_name`
 - `conda deactivate`

2. Installing the modules
 - `conda install module_1 module_2 ... `


3. Installed modules
 - a file containing a list of modules installed in the environment in [yaml format](https://yaml.org/spec/1.2.2/).
 - `conda env export --from-history > environment.yml`
 - `conda env create -f environment.yml`
---


# Basic differences

1. Conda:
 - an existing installation of the `Anconda/Miniconda` distribution is required
 - all virtual environments are saved in one main directory (default)
 - there is one program for managing environments and modules - `conda`


2. Venv
 - `Python` must be installed (in any form: system installation, installed by another program, some
   distribution, e.g. Anaconda)
 - the environment directory is created in the main projects directory - each project has its own environment
 - python module `venv` is used to manage virtual environments
 - the `pip` program is used to manage modules


# When to use

### Conda
During interactive work, i.e.:
 - while testing the code,
 - when no script is created

  it is convenient to work in `Conda` environment. You can work with different projects in one
  environment and you don't have to create and activate a new environment every time.


### Venv
When we decide to create a script from the tested code, it seems more convenient to use the `vnev`
module. We then obtain a closed project whose root directory contains everything needed to:
 - run the script
 - installing the script in its virtual environment
 - script distribution
