#!/usr/bin/env python

import pingphp 
import os
import glob2
import logging

os.chdir('./test')
pingphp.run()

files = glob2.glob('dest/test/**/*.php')

from pingphp.helper import read

for filePath in files:
    stdFilePath = 'std-' + filePath
    fileContent = read(filePath)
    fileContentStd = read(stdFilePath)
    if fileContent != fileContentStd:
        logging.error('Compare file: %s to %s not same\a', filePath, stdFilePath)
        exit(1)
    logging.info('Compare file: %s to %s same', filePath, stdFilePath)
