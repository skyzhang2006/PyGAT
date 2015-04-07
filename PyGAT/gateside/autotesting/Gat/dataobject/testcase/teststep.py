#coding=utf-8
'''
Created on 2015-3-31

@author: 张思睿
'''
from gateside.autotesting.Gat.dataobject.testobject import TestObject

class TestStep(TestObject):
    '''
    TestStep 基类
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.StepPackage=None
        self.StepGroup=None
        self.StepName=None
        self.StepParameterID=None
        self.StepParametersFilePath=None
        