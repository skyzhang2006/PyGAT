#coding=utf-8
'''
Created on 2015-4-3

@author: Devuser
'''

from gateside.autotesting.settings import GlobalConfig
from gateside.autotesting.Gat.manager.istepparametermanager import IStepParameterManager
from gateside.autotesting.Gat.util.stepvaluepool import StepValuePool

class TestStep(object):
    '''
    测试Stepmethod
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def setpmethod1(self,parameterID):
        istepparametermanager=IStepParameterManager()
        parameter=istepparametermanager.get_item("InlandHotelListHotelFilterCheck")
        print(parameter.Parameters["locationFilter"])
        valuepool=StepValuePool()
        valuepool.put_value("demo","12345678")
        
    
    def setpmethod2(self,parameterID):
        valuepool=StepValuePool()
        print(valuepool.get_value("demo"))
        
        