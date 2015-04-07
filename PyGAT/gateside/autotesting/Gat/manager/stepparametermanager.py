#coding=utf-8
'''
Created on 2015-4-1

@author: 张天得
'''
from gateside.autotesting.settings import GlobalConfig
from gateside.autotesting.Gat.util.parseXML2element import ParseXMLToElement
from gateside.autotesting.Gat.manager.testobjectmanager import TestObjectManager
from gateside.autotesting.Gat.dataobject.stepparameter.stepparameter import StepParameter
from gateside.autotesting.Gat.util.classtracer import ClassTracer
from gateside.autotesting.Gat.util.methodtracer import MethodTracer


@ClassTracer
class StepParameterManager(TestObjectManager):
    '''
    classdocs
    '''

    @MethodTracer("StepParameterManager")
    def __init__(self):
        '''
        Constructor
        '''
        self.root=self.root=ParseXMLToElement.get_root(GlobalConfig.StepParameterFilePath)
    
    @MethodTracer("StepParameterManager")
    def get_item(self,stepparameterid):
        stepparameterelement=self.get_xml_element(stepparameterid,self.root)
        return self.initialize_steparameter(stepparameterelement)
    
    @MethodTracer("StepParameterManager")
    def initialize_steparameter(self,stepparameterelement):
        '''实例化stepParameter类'''
        stepparameter=self.xmlelement_to_stepparameter(stepparameterelement)
        return stepparameter
        
    @MethodTracer("StepParameterManager")
    def get_property_value_4_stepparameter(self,stepparameterelement,propertyName):
        '''获取属性值'''
        if ParseXMLToElement.get_element_by_tag(stepparameterelement,propertyName).text!=None:
            return ParseXMLToElement.get_element_by_tag(stepparameterelement,propertyName).text
        elif propertyName!="CommandText":
            return ParseXMLToElement.get_element_by_tag(self.root,propertyName).text

    @MethodTracer("StepParameterManager")
    def xmlelement_to_stepparameter(self,stepparameterelement):
        '''获取实例属性'''
        stepparameter=StepParameter()
        for key in stepparameter.__dict__.keys():
            if key !="Parameters":
                stepparameter.__dict__[key]=self.get_property_value_4_stepparameter(stepparameterelement,key)
            else:
                stepparameter.Parameters=self.get_parameters(stepparameterelement)
        return stepparameter
    
    @MethodTracer("StepParameterManager")
    def get_parameters(self,stepparameterelement):
        '''获取TestStepElement list'''
        parentElement=ParseXMLToElement.get_element_by_tag(stepparameterelement,"Parameters")
        keys=[]
        values=[]
        for child in parentElement:
            keys.append(child.tag)
            values.append(child.text)
        parameters=dict(zip(keys,values))
        return parameters