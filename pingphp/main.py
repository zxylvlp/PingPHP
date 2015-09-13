def run():
    from .helper import initLogging
    from .helper import transFiles
    initLogging()
    transFiles()

def see():

    from .monitor import initMonitor
    run()
    initMonitor()


def init():
    initStr = '''{
    "destDir": "",
    "transFiles": [
        ""
    ],
    "ignoreFiles": [
        ""
    ]
}'''
    from .helper import write
    write('./PingPHP.conf.json', initStr)
    print('Init Done!')

