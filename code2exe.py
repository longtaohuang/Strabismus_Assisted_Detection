# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:10:31 2018

@author: STU
"""

import os 
import sys

sys.setrecursionlimit(1000000)

if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts = ['UI.spec', '-w', '-F']
    run(opts)