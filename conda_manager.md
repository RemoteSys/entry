<style>
r { color: red }
</style>


# Conda environments and packages management

## Management of environments

For each project we advice to create separate environment with installed needed packages. Basic commands [help]( https://conda.io/docs/user-guide/tasks/manage-environments.html):

  >- `conda create  -n name_of_environment` - create an environment called name_of_environment
  >- `conda create -n name_of_environment python=3.6.6` - create an environment called name_of_environment, with the indicated Python version
  
  >- `conda remove -n name_of_environment --all` environment remove
  >- `activate name_of_environment*` - activating the environment on Windows
  >- `conda activate name_of_environment` - activating the environment on Linux
  >- `deactivate deactivating`- the environment on Windows
  >- `conda deactivate deactivating` - the environment on Linux
  >- `conda info --envs / conda info -e` - displaying a list of available environments
       

## Packages management

Basic commands [help](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html):

  >- `conda list` - check the list installed packages in current environment sprawdzenie  
  >- `conda list | findstr package_name` - search for packages installed in the current environment using the stream | and console command **findstr** - on Windows  
  >- `conda list | grep package_name` - search for packages installed in the current environment using the stream | and console command **grep** - on Linux  
  >- `conda install package_name` - installs package in current environment  
  >- `conda remove package_name` - remove package from current environment  

---

# `yaml` file 

To create or update the environment, you can use a text file with a list of necessary modules. This file is saved in the `yaml` format. Let's assume that the file `myModules.yaml` contains a list of modules:

  >- `conda env create -f myModules.yaml` - creates a new environment [see here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file)
  >- `conda env update -f myModules.yaml` - updates the environment

## Example of `yaml` file

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

