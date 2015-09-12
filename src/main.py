def run():
    from .helper import initLogging
    from .helper import transFiles
    initLogging()
    transFiles()

def see():

    from .monitor import initMonitor
    run()
    initMonitor()


