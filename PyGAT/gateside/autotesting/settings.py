# coding=utf-8
'''
Created on 2013-7-1

@author: tiande.zhang
'''

import sys
import os

class GlobalConfig(object):
    '''
    全局静态变量
    '''
    TestCaseFilePath=None
    UIElementFilePath=None
    StepParameterFilePath=None
    LoggerConigPath=r"D:\Work\AptanaWorkSpace\PyGAT\gateside\autotesting\logger.conf"
    LoggerFilePath=r"C:\PySeleniumLog"
    IsDebug=True
    ROOTDIR=None
    AUTOPROJECTFOLDER="iat_testproject"
    STEPMETHODGROUPNAME="gateside.autotesting.iat_testgroups."
    
    
    @staticmethod
    def get_rootdir():
        if GlobalConfig.ROOTDIR==None:
            return os.path.dirname(os.path.abspath(".."))
        else:
            return GlobalConfig.ROOTDIR
    
    @staticmethod
    def get_slash():
        if sys.platform=="win32":
            return "\\"
        else:
            return "/" 
    @staticmethod
    def get_autoproject(self):
        return GlobalConfig.AUTOPROJECTFOLDER
    
    @staticmethod
    def get_stepmethod_pagepath(self):
        return GlobalConfig.STEPMETHODGROUPNAME
    
    @staticmethod
    def get_testcase_filepath(filename):
        result=""
        if GlobalConfig.TestCaseFilePath==None:
            result=GlobalConfig.get_rootdir()+GlobalConfig.get_slash()+"datafiles"+GlobalConfig.get_slash()+"xmls"+GlobalConfig.get_slash()+filename
        else:
            result=GlobalConfig.TestCaseFilePath
        return result
    
    @staticmethod
    def get_parameter_filepath(filename):
        result=""
        if GlobalConfig.StepParameterFilePath==None:
            result=GlobalConfig.get_rootdir()+GlobalConfig.get_slash()+"datafiles"+GlobalConfig.get_slash()+"xmls"+GlobalConfig.get_slash()+filename
        else:
            result=GlobalConfig.StepParameterFilePath
        return result
            
            
        
    
        
    
    
    
    
    
    
    
    