#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Project Name
------------

    synbed -- Synonym Extraction with Word Embeddings

File name
---------

    synbedrun.py


File Description
----------------

    Workspace for synbed project. Do not run module. Copy and paste code to interpreter.
'''

if False:
    # Global variables
    DIR = '/Users/Herman/Documents/jzhang/synbed/'
    dataDir = '/Users/Herman/Documents/jzhang/synbed/'
    outDir = '/Users/Herman/Documents/jzhang/synbed/'

    # Modules
    from importlib import reload, import_module
    try:
        reload(synbed)
    except NameError:
        import synbed
    try:
        reload(synbedaux)
    except NameError:
        import synbedaux
    from synbed import *
    from synbedaux import *

    #
    # Current workspace
    #
    pass

'''
################################################################################
##### Function Prototypes ######################################################
################################################################################
'''
