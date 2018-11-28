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

    synbedaux.py

File Description
----------------

    Holds auxiliary files used in debugging and developing synbed.py
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
