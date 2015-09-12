def run():
    from .helper import initLogging,transFiles
    initLogging()
    transFiles()

def see():

    from .monitor import initMonitor
    run()
    initMonitor()

if __name__ == "__main__":
    run()


