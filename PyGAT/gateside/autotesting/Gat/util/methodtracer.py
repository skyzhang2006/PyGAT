# coding=utf-8
'''
Created on 2013-7-8

@author: tiande.zhang
'''
from gateside.autotesting.Gat.util.logger4py.logger import Logger
from gateside.autotesting.settings import GlobalConfig

def MethodTracer(modulename):
    def MethodInvokeTracer(method):
        def tracer(*args):
            traceMessage(method,args,modulename)
            return method(*args)
        return tracer
    return MethodInvokeTracer


def traceMessage(method,args,modulename):
    '''信息记录入日志'''
    if GlobalConfig.IsDebug:
        logger=Logger()
        logger.tracelog(modulename+"."+method.__name__+" was invoked and parameters are "+str(args))
    