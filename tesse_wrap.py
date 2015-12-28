#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

# a tiny wrapper for experimenting through different languages of tesseract.

# NB! You can get list of supported languages via
# tesseract --list-langs

import subprocess
import sys
from optparse import OptionParser

# Assumes that tesseract has these languages available
potential_langs = ['deu_frak','fin','dan_frak']

filename =""
parser = OptionParser()
parser.add_option("-i", "--inputfile", type="string", dest="filename", metavar='filename',
                  help="File to be OCRd")


(options, args) = parser.parse_args()
filename        = options.filename

if not filename:
    sys.exit("Please give a input file with parameter -i.")


for lang in potential_langs:

    try:
        result = subprocess.check_output(['tesseract',filename,'-l',lang,'stdout'])

    except subprocess.CalledProcessError, e:
        print "ERRR!! output:\n", e.output
        result = e.output


    print "-------- Outcome of language : " , lang , "-------- \n", result , "\n"


## Example of a run:
## python tesse_wrap.py -i sortavala_10568340.jpg
