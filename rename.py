#!/usr/bin/python
'''
meant to rename a list of files based on strings in the filename
daniel soto
Tue Dec 11 02:58:17 PST 2007
'''

import re
import os
import glob

def renameFile ( searchString, replacementString ):
    regExp = re.compile( searchString )
    # get list of files containing search string
    globString = '*' + searchString + '*'
    fileNameList = glob.glob(globString)
    # iterate over list renaming files
    for fname in fileNameList:
        foutName = regExp.sub( replacementString, fname )
        os.rename( fname, foutName )
        print fname,
        print '\tchanged to\t',
        print foutName

searchString = 'r1'
replacementString = 'S1'
renameFile( searchString, replacementString )

searchString = 'r2'
replacementString = 'S2'
renameFile( searchString, replacementString )