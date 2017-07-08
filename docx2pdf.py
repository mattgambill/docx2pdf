'''
File: doc(x)2pdf.py
Created by; Matt Gambill
Created on: July 8th, 2017
Synopsis:
Script descends into directories and converts all .doc and .docx into pdf
'''
import os
from subprocess import call

# The top argument for walk
topdir = os.getcwd()

# The extension to search for
exten_1 = '.docx'
exten_2 = '.doc'

# The main function
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten_1):
            docx_path = os.path.join(dirpath, name)
            os.chdir(dirpath)
            call(['libreoffice', '--headless', '--invisible', '--convert-to','pdf', docx_path])
        elif name.lower().endswith(exten_2):
            doc_path = os.path.join(dirpath, name)
            os.chdir(dirpath)
            call(['libreoffice', '--headless', '--invisible', '--convert-to','pdf', doc_path])
print("\nDone!\n")