---
Scripts and modules
---

Scripts and modules in `Python` are text files with the `.py` extension.  Generally speaking, modules contain function/class definitions and scripts use these functions/classes.

The scripts are run like programs. They contain program code, but can also contain function and class definition code - especially if they were only defined for a specific script. 

A clear division will be maintained for classes:

  - the functions will be placed in separate files - modules
  - scripts are files that run as command line programs



# 1. Script creation rules.

The script will be created in stages:

  - in the first step, individual lines of code will be tested interactively from the `ipython` text console or `jupyter notebook`. Working code will be saved to the module file as functions.  
  - in the second step the created functions will be checked by importing them to the `ipython` text console or `jupyter notebook` 
  - the third step is to build the script from working, already checked, fragments of code and functions


# 2. Launching the script

The script will be launched from a text console or `Anaconda` terminal (in Windows system):

1. Run the text console
1. Activate a virtual environment containing the necessary modules e.g.

    > `conda activate your_environment`.
  
2. Run the script by typing:

    >`python script_name arg1 arg2 ...`   

    or

    >`python3 script_name arg1 arg2 ...`    

depending on the computer configuration.


# 3. Basic script architecture

```python
# -*- coding: utf-8-*-

#--------------------------------------------------------------------------------------------
# modules / functions import section and temporary modules search path settings
# examples:

import sys
sys.path.append('some path')

import codecs


#--------------------------------------------------------------------------------------------
#script description and constants creation section

description = '''
Create a description of how your script works
'''

#--------------------------------------------------------------------------------------------
# function definition section

def parserFunction():
	'''Function parsing command line arguments'''
	parser = argparse.ArgumentParser(description = description)

	# Add arguments to your module: mandatory, i.e. positional and optional i.e.
	# parser.add_argument('someArg, 	type=str,	help=u'''help text''')


	args = parser.parse_args()
	return args

#--------------------------------------------------------------------------------------------

def fun1():
	pass


def fun2():
	pass


def fun2():
	pass



#--------------------------------------------------------------------------------------------
#code execution section after running the script as a program

if __name__ == '__main__':

	#... load command line arguments .............
	args = parserFunction()

	# next steps of the program

```

### 1.1. First line

```python
# -*- coding: utf-8-*
```

Different operating systems use different character encodings. In order to read the file correctly, it is recommended to put information about the encoding used in the first line.

>Note:
>The character `#` indicates that the line is a comment
---

Good practice is also:

  >- setting the editor to encode `utf-8`
  >- not to use diacritical marks, especially in file names, directories, variables
  >- not use white characters (spaces, tabs) or special characters (e.g. `!`) in file names, directories, variables


### 1.2. Function `parserFunction()`

The recommended module to get script arguments from the command line is the `argparse`:

>,,This tutorial is intended to be a gentle introduction to argparse, the recommended command-line parsing module in the Python standard library.''

(from *https://docs.python.org/3/howto/argparse.html*)

The use of the module can be reduced to creating a function that will handle the arguments of the script:

```python
def parserFunction():
```

Inside the function:

  -  a parser object is created:  ```parser = argparse.ArgumentParser()```
  - further arguments are added: ```parser.add_argument("someArg")```

An example showing how the script works can be found at [GitHub](https://github.com/RemoteSys/entry/blob/master/testScript.py). Download this file `testScript.py` and run it in the console:

  - `python testScript.py -h` to display help
  - `python testScript.py 5 2 someFolderName` - to see how the script works, where the arguments are arbitrary, consistent with the script's help text



### 1.3. Variable `__name__` 

`if __name__ == '__main__':`

When the Python interpreter reads a file, it sets the value of a special variable `__name__` by assigning it:

  - the file name if it is run as a module e.g.: `import  myImProc` then  `__name__ == 'myImProc'`
  - `'__main__'` if it is run as a program: `__name__ == '__main__'`

In practice, if a script is run as a program, the code below this line is executed.







