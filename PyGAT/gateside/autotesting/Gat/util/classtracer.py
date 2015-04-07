# coding=utf-8
'''
Created on 2013-7-8

@author: tiande.zhang
'''
from gateside.autotesting.Gat.util.logger4py.logger import Logger
from gateside.autotesting.settings import GlobalConfig

def ClassTracer(klass):
    class Tracer(klass):
        tracemessage(klass)
    return Tracer
    


def tracemessage(klass):
    '''信息记录入日志'''
    if GlobalConfig.IsDebug:
        logger=Logger()
        logger.tracelog(klass.__dict__['__module__'])
    