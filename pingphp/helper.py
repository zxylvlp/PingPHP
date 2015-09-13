# codeing: utf8
'''
helper functions
'''
import json
import os
import os.path
import glob2
import logging
from ply import yacc
from .lexer import PingLexer
from .grammar import *
import traceback

configObj = None
filesSet = None
fileStrCache = ''

def projectName():
    return "PingPHP"

def printStack(e):
    if not configObj['debug']:
        return
    print(traceback.format_exc())

def read(path):
    result = ''
    try:
        file_ = open(path, 'rU')
        result = file_.read()
    except:
        logging.error('Read file: '+path+' fail')
    finally:
        file_.close()
    return result


def write(path, str_):
    pathAndName = os.path.split(path)
    if len(pathAndName[0]) > 0 and not os.path.exists(pathAndName[0]):
        os.makedirs(pathAndName[0])
    try:
        file_ = open(path, 'w')
        file_.write(str_)
    except:
        logging.error('Write file: '+path+' fail')

    finally:
        file_.close()


def loadJson(path):
    jsonStr = read(path)
    return json.loads(jsonStr)


def obj2Json(obj):
    if type(obj) == type(object()):
        return obj.__dict__
    return obj


def json2Str(obj):
    return json.dumps(obj, default=obj2Json, indent=4)


def printObj(obj):
    print(json2Str(obj))


def getConfigPath():
    return projectName() + '.conf.json'


def getConfig():
    global configObj
    if not configObj:
        path = getConfigPath()
        configObj = loadJson(path)
        saveJson(path, configObj)
        if 'debug' in configObj:
            configObj['debug'] = bool(configObj['debug'])
        else:
            configObj['debug'] = False
        if not (('destDir' in configObj) and isinstance(configObj['destDir'], str)):
            logging.error('Config File: destDir field error')
            exit(1)
        if not (('transFiles' in configObj) and isinstance(configObj['transFiles'], list)):
            logging.error('Config File: transFiles field error')
            exit(1)
        if not ('ignoreFiles' in configObj): 
            config['ignoreFiles'] = []
        if not isinstance(configObj['ignoreFiles'], list):
            logging.error('Config File: ignoreFiles field error')
            exit(1)

    return configObj


def saveJson(path, obj):
    write(path, json2Str(obj))


def isString(obj):
    return isinstance(obj, str)


def filesMatch(patternList):
    set_ = set()
    for patternStr in patternList:
        list_ = glob2.glob(patternStr)
        set_.update(list_)
    return set_


def filesNoCache():
    global filesSet
    conf = getConfig()
    filesSet = filesMatch(conf["transFiles"]).difference(filesMatch(conf["ignoreFiles"]))
    getConfigPath() in filesSet and filesSet.remove(getConfigPath())
    filesSet = list(filesSet)
    filesSet.sort()
    return filesSet


def files():
    global filesSet
    if filesSet:
        return filesSet
    filesNoCache()
    return filesSet


def destDir():
    return getConfig()["destDir"]


def mapSrcToDest(src):
    lastDot = src.rfind('.')
    src = src[:(lastDot + 1)] + 'php'
    return os.path.join(destDir(), src)


def initLogging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

def errorMsg(errorType, t):
    lineStart = fileStrCache[:t.lexpos].rfind('\n') + 1
    linePos = t.lexpos - lineStart
    errorContent = fileStrCache[lineStart:t.lexpos] + '`ERROR`' + fileStrCache[t.lexpos:t.lexpos+len(t.value)]
    logging.error(errorType + " error in %d,%d \n%s\a", t.lineno, linePos+1 , errorContent)
    raise Exception


def transFiles():
    try:
        for file_ in files():
            doTrans(file_)
    except Exception as e:
        printStack(e)
        exit(1)

def transFilesNoExit():
    try:
        for file_ in files():
            doTrans(file_)
    except Exception as e:
        printStack(e)

def doTrans(path):
    dest = mapSrcToDest(path)
    logging.info("Translating %s: %s to %s", 'file', path, dest)
    global fileStrCache
    fileStrCache = read(path)
    pLexer = PingLexer(fileStrCache)
    # print pLexer.token()
    # print pLexer.tokList
    parser = yacc.yacc(optimize=True)
    res = parser.parse(lexer=pLexer)
    strRes = res.gen()
    write(dest, strRes)
