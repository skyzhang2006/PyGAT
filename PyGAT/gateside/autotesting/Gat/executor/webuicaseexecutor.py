#coding=utf-8
'''
Created on 2015-4-7

@author: 张天得
'''

from gateside.autotesting.Gat.executor.stepscaseexecutor import StepsCaseExecutor

class WebUICaseExecutor(StepsCaseExecutor):
    '''
    classdocs
    '''


    def __init__(self,casefilename,caseid):
        '''
        Constructor
        '''
        StepsCaseExecutor.__init__(self,casefilename,caseid)
        
        