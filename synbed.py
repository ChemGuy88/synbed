#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime, json, os, pickle, re, requests, sys, traceback
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
from IPython import get_ipython
from mlFunctions import tic, toc, beep, ts, alarm1, run_from_ipython, getNumLines
from progress.bar import ChargingBar
from progress.spinner import Spinner

'''
Project Name
------------

    synbed -- Synonym Extraction with Word Embeddings

File name
---------

    synbed.py

File Description
----------------

    Main module for this project.

'''

'''
Meta Global Variables
'''

ipython = get_ipython()
# ipython.magic("matplotlib") # Same as %matplotlib, turn on interactive plotting in IPython

# Determine if running on Saturn server (Linux OS) or my personal machine (Darwin OS)
OS = sys.platform

# Relative path setup
DIR0 = os.getcwd() +'/'
if OS == 'darwin':
    DIR = '/Users/Herman/Documents/jzhang/synbed/'
elif OS == 'linux':
    DIR = '/home/herman/synbed/'

# Use latex in matplotlib
# plt.rc('text', usetex=True) # False by default

'''
Notes
'''

'''
################################################################################
##### Functions ################################################################
################################################################################
'''
def function():
    pass


'''
################################################################################
##### Workspace ################################################################
################################################################################
'''

# see synbedrun.py for workspace

'''
################################################################################
##### Define command line arguments ############################################
################################################################################
'''

def main():
    # Can add DIR option to overwrite default DIR value
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        msg = 'You have run synbed.py with no arguments. Synbed.py is a module under development, and does not need arguments at this time.'
        print(msg)

        # Temporary, until bug resolved
        if run_from_ipython():
            sys.exit(0)
        else:
            url = 'https://stackoverflow.com/questions/48571212/why-is-sys-exit-causing-a-traceback'
            print('Traceback is printed on exit when using \'python -i\'. This is a Python bug that has already been reported. Note this does not happen with \'IPython -i\'. Refer to %s.\n' % url)
            sys.exit(0)

    # Work sequence
    print('synbed.py is not implemented yet to be run.')
    # for arg in args:
        # pass

# Boilerplate
if __name__ == '__main__':
  main()
