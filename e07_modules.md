# Using `Python` modules

Generally speaking, python code is divided into parts called `modules`. The modules are text files
with the `.py` extension . By default, only base modules are loaded. Using other modules, e.g. to
perform scientific calculations, charts, etc. requires:

 - installing them on the system
 - each time loading modules into the computer’s memory called `import`.  

Because the modules are files saved on your computer, Python must `know` where to look for these files.
By default, Python searches the disk in the order:  
 - in current folder
 - in folder specified in the system variable `PYTHONPATH`
 - in folders given during `Python` installation
 - in folders secified in variable `sys.path`, which is oridinaly list. This path can be edited while
   the interpreter is running, the path configuration is lost after ending interpreter.


### Possible solutions:

 - created modules will be placed in the working directory
 - add a temporary path to `sys.path`
 - creating a directory structure treated as packages using `__init__.py` files


# Temporary path

 - `import sys` - imports the `sys` module
 - `sys.path.insert` or `sys.path.append` - adds the path to the directory with modules:
   * insert: at the indicated position on the list
   * append: at the end of the list

Egzample:

 >`sys.path.insert(0, 'c:\my_modules')`

