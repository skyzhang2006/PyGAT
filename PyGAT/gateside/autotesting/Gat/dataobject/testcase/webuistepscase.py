#coding=utf-8
'''
Created on 2015-3-31

@author: 张天得
'''
from gateside.autotesting.Gat.dataobject.testcase.stepscase import StepsCase

class WebUIStepsCase(StepsCase):
    '''
    WebUI 用例数据模型
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.UIElementsFilePath=None
        