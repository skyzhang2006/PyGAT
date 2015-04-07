#coding=utf-8
'''
Created on 2015-3-31

@author: 张天得
'''
from gateside.autotesting.Gat.dataobject.testcase.teststep import TestStep

class WebUITestStep(TestStep):
    '''
    WebUI TestStep基类
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.UIElementsFilePath=None
        