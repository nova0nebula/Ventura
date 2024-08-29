# constant_variables.py

#!/usr/bin/env python3


# Python Import
import os
import sys
import random
import shutil
import time
import inspect
import pickle
import itertools
from collections import Counter
from colorama import Fore


# Constant Variables

# Setup Color Options
def red(skk): sys.stdout.write("\033[91m {}\033[00m" .format(skk))
def green(skk): sys.stdout.write("\033[92m {}\033[00m" .format(skk))
def yellow(skk): sys.stdout.write("\033[93m {}\033[00m" .format(skk))
def lightpurple(skk): sys.stdout.write("\033[94m {}\033[00m" .format(skk))
def purple(skk): sys.stdout.write("\033[95m {}\033[00m" .format(skk))
def cyan(skk): sys.stdout.write("\033[96m {}\033[00m" .format(skk))
def lightgray(skk): sys.stdout.write("\033[97m {}\033[00m" .format(skk))

# Setup formatting options
def bold(type): sys.stdout.write("\033[1m" + type + "\033[0m")
def italic(type): sys.stdout.write("\033[3m" + type + "\033[0m")
def underline(type): sys.stdout.write("\033[4m" + type + "\033[0m")
def highlight(type): sys.stdout.write("\033[7m" + type + "\033[0m")
def crossout(type): sys.stdout.write("\033[9m" + type + "\033[0m")
def invisible(type): sys.stdout.write("\033[8m" + type + "\033[0m")


# Variables
dash = "-" * 50


# Function: clear_screen()
def clear_screen():
    print("\n" * 1000)


# Function: define_variable(text)
def define_variable():
    frame = inspect.currentframe()
    line_number = frame.f_back.f_lineno
    return int(line_number)


# Function: generate_variations(input_str)
def generate_variations(input_str):
    # Generate all permutations of the string
    permutations = [''.join(p) for p in itertools.permutations(input_str)]

    # Generate all case variations
    def case_variations(s):
        return list(map(''.join, itertools.product(*([letter.lower(), letter.upper()] for letter in s))))

    case_variants = case_variations(input_str)

    # Combine both variations
    variations = set(permutations + case_variants)

    return list(variations)


# End of program