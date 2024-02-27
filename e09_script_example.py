# -*- coding: utf-8-*-

"""
First script.

Dunder variable - Double Under (Underscores):
    - __file__: contains the path to the module
    - __name__: "__main__" or module name

If the module is imported, the python interpreter sets the value of the
__name__ variable to the name of the module.

If the module is run as a script, the __name__ variable becomes __main__.
"""

from pathlib import Path
import sys
import argparse

# temporary module search path can be set
# suppose that the modules to be imported are in the subdirectory 'src'
current_dir = str(Path(".").resolve())
module_dir = Path(__file__).parent.resolve()
module_dir = str(module_dir.joinpath("src"))

sys.path.append(current_dir)
sys.path.insert(0, module_dir)


# --

description = """This is a description of what the script does.
This script:
- is to show how the 'argparse' module works
- displays the given arguments
"""


def parser_function():
    """Function parsing command line arguments"""
    parser = argparse.ArgumentParser(description=description)

    # Add arguments to your script: mandatory (positional) and optional
    parser.add_argument("rows", type=int, help="Number of rows")
    parser.add_argument("cols", type=int, help="Number of cols")
    parser.add_argument("-p", "--user_path", type=str, help="Path to folder")

    args = parser.parse_args()
    return args


def main(args):
    """The code below the condition 'if __main __...' is executed when the
    module is run as a script. All this code can (optionally) be grouped into
    a single function, commonly called 'main ()'.
    """
    print(f"The 'main ()' function:\n{'---'*10}\n")
    msg1 = "  The variable 'args' is of the type:"
    msg2 = "  and it looks like this:"
    print(f"{msg1:<46}{type(args)}\n{msg2:<46}{args}\n")

    if args.user_path:
        args.user_path = str(Path(args.user_path).resolve())

    print("  Dictionary of command line arguments:")
    for key, val in vars(args).items():
        print(f"  {'key = ':>10}{key:<10}\tvalues = {val}")

    print("\n")


# --

if __name__ == "__main__":

    args = parser_function()

    print(f"\n{'Current folder path (working directory):':<46}{current_dir}")
    print(f"{'Module folder path (__file__):':<46}{module_dir}\n")
    print(f"{'Value of the variable __name__:':<46}{__name__}\n")

    main(args)
