# coding=utf-8
'''
Created on 2013-7-2

@author: tiande.zhang
'''
import logging.config
import os
import inspect
from gateside.autotesting.Gat.util.logger4py.loggerenum import LoggerEnum
from gateside.autotesting.settings import GlobalConfig
from gateside.autotesting.Gat.util.objectinfo import ObjectInfo


class Logger(object):
    '''
    所有logger的基类
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.create_log_dir()
        logging.config.fileConfig(GlobalConfig.LoggerConigPath)
    
    def info(self,msg):
        '''将信息记录为到Trace.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileInfoLogger)
        logger.info(self.get_invoker_info()+msg)
    
    def error(self,msg):
        '''将信息记录为到Error.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileErrorLogger)
        logger.error(self.get_invoker_info()+msg)
    
    def critical(self,msg):
        '''将信息记录为到Critical.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileCriticalLogger)
        logger.critical(self.get_invoker_info()+msg)
    
    def log_to_console(self,msg):
        '''将信息记录为到Critical.log文件中'''
        logger=logging.getLogger(LoggerEnum.StreamLogger)
        logger.debug(self.get_invoker_info()+msg)
    
    def tracelog(self,msg):
        '''将信息记录为到trace.log文件中'''
        logger=logging.getLogger(LoggerEnum.FileTraceLogger)
        logger.debug(self.get_invoker_info()+msg)
    
    def create_log_dir(self):
        if not os.path.exists(GlobalConfig.LoggerFilePath):
            os.mkdir(GlobalConfig.LoggerFilePath)
    
    def get_current_frame(self):
        return inspect.currentframe()
    
    def get_invoker_info(self):
        currentFrame=ObjectInfo(self.get_current_frame())
        return currentFrame.getModule()+"    "+currentFrame.getMethod()+"    "+str(currentFrame.getLineNumber())+"    "
    
        

        
    

    
        
        