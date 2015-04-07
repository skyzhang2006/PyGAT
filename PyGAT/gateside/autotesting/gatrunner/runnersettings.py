#coding=utf-8
'''
Created on 2015-4-7

@author: 张天得
'''
import os
from gateside.autotesting.settings import GlobalConfig

class RunnerSettings(object):
    '''
    classdocs
    '''
    ROOTDIR=None
    TESTPROJECTNAME="iat_testproject"
    
    @staticmethod
    def get_rootdir():
        if RunnerSettings.ROOTDIR==None:
            return os.path.abspath("..")
        else:
            return RunnerSettings.ROOTDIR
    
    @staticmethod
    def get_template_folder():
        if RunnerSettings.ROOTDIR==None:
            return RunnerSettings.get_rootdir()+GlobalConfig.get_slash()+"gatrunner"+GlobalConfig.get_slash()+"templates"
        else:
            return RunnerSettings.ROOTDIR
    
    @staticmethod
    def get_xml_folder():
        return RunnerSettings.get_rootdir()+GlobalConfig.get_slash()+"datafiles"+GlobalConfig.get_slash()+"xmls"
    
    @staticmethod
    def get_method_tempatepath():
        return RunnerSettings.get_template_folder()+GlobalConfig.get_slash()+"testmethod.txt"
    
    @staticmethod
    def get_testclass_tempatepath():
        return RunnerSettings.get_template_folder()+GlobalConfig.get_slash()+"testclass.txt"
    
    
        
        