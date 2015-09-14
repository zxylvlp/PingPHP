# encoding: utf-8
'''
PingPHP main functions
'''
from .helper import *


def run():
    initLogging()
    transFiles()


def see():
    run()
    initMonitor()


def init():
    initStr = '''{
    "destDir": "",
    "destDir": "",
    "transFiles": [
        ""
    ],
    "ignoreFiles": [
        ""
    ]
}'''
    write('./PingPHP.conf.json', initStr)
    print('Init Done!')
