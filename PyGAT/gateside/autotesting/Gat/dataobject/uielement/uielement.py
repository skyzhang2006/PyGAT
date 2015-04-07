#coding=utf-8
'''
Created on 2015-3-31

@author: 张天得
'''
from gateside.autotesting.Gat.dataobject.testobject import TestObject

class UIElement(TestObject):
    '''
    WebUI 页面元素模型
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.NodeID=None
        self.ControllType=None
        self.FrameType=None
        self.FrameIndex=None
        self.FrameName=None
        self.ID=None
        self.Name=None
        self.XPath=None
        self.Class=None
        self.LinkText=None
        self.Tag=None
        self.InnerText=None
        self.OtherProperty=None
        self.OtherPropertyValue=None
        