#coding=utf-8
'''
Created on 2015-4-1

@author: 张天得
'''

from gateside.autotesting.Gat.manager.testobjectmanager import TestObjectManager
from gateside.autotesting.Gat.util.methodtracer import MethodTracer
from gateside.autotesting.Gat.dataobject.uielement.uielement import UIElement
from gateside.autotesting.Gat.util.parseXML2element import ParseXMLToElement
from gateside.autotesting.Gat.user_exceptions.userexception import XMLElementNoneException
from gateside.autotesting.settings import GlobalConfig
from gateside.autotesting.Gat.util.classtracer import ClassTracer

@ClassTracer
class WebUIElementManager(TestObjectManager):
    '''
    classdocs
    '''
    
    @MethodTracer("WebUIElementManager")
    def __init__(self):
        '''初始化管理器
        '''
        self.root=self.root=ParseXMLToElement.get_root(GlobalConfig.UIElementFilePath)
    
    @MethodTracer("WebUIElementManager")
    def get_item(self,testobjectid):
        uielement=self.get_xml_element(testobjectid,self.root)
        return self.initialize_uielement(uielement)
    
    
    @MethodTracer("WebUIElementManager")
    def initialize_uielement(self,uiElementNode):
        '''实例化UIElements类'''
        uielementobject=UIElement()
        uielementobject=self.xmlelement_to_testbject(uiElementNode, uielementobject)
        return uielementobject
    
    @MethodTracer("WebUIElementManager")
    def get_xml_element(self,testobjectid,rootelement):
        '''获取TestcaseElement by case id'''
        result=ParseXMLToElement.get_element_by_attr(rootelement,"NodeID",testobjectid)
        if result==None:
            raise XMLElementNoneException(testobjectid)
        return result
        