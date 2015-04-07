#coding=utf-8
'''
Created on 2015-3-31

@author: 张天得
'''

from gateside.autotesting.Gat.util.parseXML2element import ParseXMLToElement
from gateside.autotesting.Gat.user_exceptions.userexception import XMLElementNoneException
from gateside.autotesting.Gat.util.classtracer import ClassTracer
from gateside.autotesting.Gat.util.methodtracer import MethodTracer

@ClassTracer
class TestObjectManager(object):
    '''
    classdocs
    '''

    @MethodTracer("TestObjectManager")
    def __init__(self):
        
        '''
                           初始化实例属性
        '''
    
    @MethodTracer("TestObjectManager")
    def getitem(self,ID):
        raise Exception("功能尚未事项。")
    
    @MethodTracer("TestObjectManager")
    def get_xml_element(self,testobjectid,rootelement):
        '''获取TestcaseElement by case id'''
        result=ParseXMLToElement.get_element_by_attr(rootelement,"ID",testobjectid)
        if result==None:
            raise XMLElementNoneException(testobjectid)
        return result
    
    @MethodTracer("TestObjectManager")
    def get_testobject_property(self,testobjectelement,propertyName):
        '''获取属性值'''
        if propertyName in testobjectelement.attrib.keys():
            return testobjectelement.get(propertyName)
        elif ParseXMLToElement.get_element_by_tag(self.root, propertyName)!=None:
            return ParseXMLToElement.get_element_by_tag(self.root, propertyName).text
        else:
            return None
    
    @MethodTracer("TestObjectManager")
    def xmlelement_to_testbject(self,test_object_element,dest_object):
        '''通用测试对象初始化方法
        '''
        for key in dest_object.__dict__.keys():
            dest_object.__dict__[key]=self.get_testobject_property(test_object_element,key)
        return dest_object
    