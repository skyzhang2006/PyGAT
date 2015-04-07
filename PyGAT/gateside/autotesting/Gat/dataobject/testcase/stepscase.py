#coding=utf-8
'''
Created on 2015-3-31

@author: 张天得
'''
from gateside.autotesting.Gat.dataobject.testobject import TestObject

class StepsCase(TestObject):
    '''
    多步奏用例模型基类
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.StepPackage=None
        self.StepGroup=None
        self.StepParametersFilePath=None
        self.Name=None
        self.ID=None
        self.TestSteps=[]
        