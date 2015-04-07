#coding=utf-8
'''
Created on 2015-4-1

@author: 张天得
'''

from gateside.autotesting.Gat.manager.testobjectmanager import TestObjectManager
from gateside.autotesting.Gat.util.methodtracer import MethodTracer
from gateside.autotesting.Gat.dataobject.testcase.stepscase import StepsCase
from gateside.autotesting.Gat.util.parseXML2element import ParseXMLToElement
from gateside.autotesting.Gat.dataobject.testcase.teststep import TestStep
from gateside.autotesting.Gat.util.classtracer import ClassTracer
from gateside.autotesting.settings import GlobalConfig

@ClassTracer
class StepsCaseManager(TestObjectManager):
    '''
    classdocs
    '''
    @MethodTracer("StepsCaseManager")
    def __init__(self):
        '''初始化管理器
        '''
        self.root=self.root=ParseXMLToElement.get_root(GlobalConfig.TestCaseFilePath)
        
    
    @MethodTracer("StepsCaseManager")
    def get_item(self,testobjectid):
        stepsCaseElement=self.get_xml_element(testobjectid,self.root)
        return self.initialize_testcase(stepsCaseElement)

    
    @MethodTracer("StepsCaseManager")
    def initialize_testcase(self,stepsCaseElement):
        '''实例化testcase类'''
        stepsCase=StepsCase()
        stepsCase=self.xmlelement_to_testbject(stepsCaseElement, stepsCase)
        stepsCase.TestSteps=self.xmlelement_to_teststeps(stepsCaseElement,stepsCase)
        return stepsCase
    
    @MethodTracer("StepsCaseManager")
    def get_test_step_elements(self,stepsCaseElement):
        '''获取TestStepsElement list'''
        parentElement=ParseXMLToElement.get_element_by_tag(stepsCaseElement,"TestSteps")
        return ParseXMLToElement.get_children_by_tag(parentElement,"Step")
    
    @MethodTracer("StepsCaseManager")
    def xmlelement_to_teststeps(self,stepsCaseElement,parentcase):
        '''将teststeps从xml转换为实例'''
        teststepelements=self.get_test_step_elements(stepsCaseElement)
        teststeplist=[]
        for step in teststepelements:
            teststep=TestStep()
            if step!=None:
                for key in teststep.__dict__.keys():
                    teststep.__dict__[key]=self.get_propertyvalue_4_step(step, parentcase, key)
            teststeplist.append(teststep)
        return teststeplist
    
    @MethodTracer("StepsCaseManager")
    def get_propertyvalue_4_step(self,stepelement,parentcase,propertyName):
        '''实例化step'''
        if propertyName in stepelement.attrib.keys():
            return stepelement.get(propertyName)
        elif propertyName in parentcase.__dict__.keys():
            if parentcase.__dict__[propertyName]!=None:
                return parentcase.__dict__[propertyName]
        else:
            return None
        