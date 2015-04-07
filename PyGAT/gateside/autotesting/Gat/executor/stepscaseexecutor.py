#coding=utf-8
'''
Created on 2015-4-2

@author: 张天得
'''
from gateside.autotesting.settings import GlobalConfig
from gateside.autotesting.Gat.manager.testobjectmanagerfactory import TestObjectManagerFactory
from gateside.autotesting.Gat.dataobject.objectmanagertype import ObjectManagerType
from gateside.autotesting.Gat.util.classtracer import ClassTracer
from gateside.autotesting.Gat.util.methodtracer import MethodTracer
from gateside.autotesting.Gat.util.methodinvoker import MethodInvoker
from gateside.autotesting.Gat.util.stepvaluepool import StepValuePool

@ClassTracer
class StepsCaseExecutor(object):
    '''
    classdocs
    '''

    @MethodTracer("StepsCaseExecutor")
    def __init__(self,casefilename,caseid):
        '''
        Constructor
        '''
        GlobalConfig.TestCaseFilePath=GlobalConfig.get_testcase_filepath(casefilename)
        self.testcaseid=caseid
        
    
    @MethodTracer("StepsCaseExecutor")
    def execute(self):
        '''执行测试用例'''
        try:
            self.setup()
            self.execute_setp()
            self.teardown()
        finally:
            self.teardown()
        
        
    @MethodTracer("StepsCaseExecutor")
    def setup(self):
        stepvaluepool=StepValuePool()
    
    @MethodTracer("StepsCaseExecutor")
    def teardown(self):
        stepvaluepool=StepValuePool()
        stepvaluepool.clear_all()
        
    
    @MethodTracer("StepsCaseExecutor")
    def execute_setp(self):
        '''执行测试步骤'''
        testcase=self.get_testobject()
        for teststep in testcase.TestSteps:
            self.call_step_method(teststep)
    
    
    @MethodTracer("StepsCaseExecutor")
    def get_testobject(self):
        testcasemanager=TestObjectManagerFactory.get_object_manager(ObjectManagerType.ISTEPCASEMANAGER)
        testcase=testcasemanager.get_item(self.testcaseid)
        return testcase
    
    
    @MethodTracer("StepsCaseExecutor")
    def call_step_method(self,teststep):
        GlobalConfig.StepParameterFilePath=GlobalConfig.get_parameter_filepath(teststep.StepParametersFilePath)
        instance=MethodInvoker.get_instance(teststep.StepPackage,teststep.StepGroup,teststep.StepPackage.split('.'))
        method=MethodInvoker.get_method(instance,teststep.StepName)
        arglist=list()
        arglist.append(teststep.StepParameterID)
        method(arglist)
        
        
        
        