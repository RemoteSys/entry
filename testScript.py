# -*- coding: utf-8-*-


'''
First script
'''

from pathlib import Path
import sys
import argparse

pathSearch = Path('.').resolve().as_posix()
sys.path.append(pathSearch)


# -----------------------------------------

description='''This is a description of what the script does.
This script:
- is to show how the 'argparse' module works
- displays the given arguments
'''

def parserFunction():
    '''Function parsing command line arguments'''
    parser = argparse.ArgumentParser(description = description)

    # Add arguments to your module: mandatory, i.e. positional and optional i.e.
    parser.add_argument('rows',     type=int,    help=u'''Number of rows''')
    parser.add_argument('cols',     type=int,    help=u'''Number of cols''')
    parser.add_argument('-p','--somePath',     type=str,    help=u'''Path to folder''')


    args = parser.parse_args()
    return args



def main(args):
    if args.somePath:
        args.fullPath = Path(args.somePath).resolve().as_posix()
    
    print(f'Dictionary of command line arguments:')
    for key,val in vars(args).items():
        print(f'key = {key}\tvalues = {val}')
    
    print('\n')

# ------------------------------------------

if __name__ == '__main__':
    
    args = parserFunction()
    print(f'''\nThe 'args' is of the type:\t{type(args)}\nand it looks like this:\n\t\t\t{args}\n''')
    
    main(args)
    
  
