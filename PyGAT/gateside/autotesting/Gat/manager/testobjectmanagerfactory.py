#coding=utf-8
'''
Created on 2015-4-3

@author: 张天得
'''
from gateside.autotesting.Gat.dataobject.objectmanagertype import ObjectManagerType
from gateside.autotesting.Gat.manager.istepparametermanager import IStepParameterManager
from gateside.autotesting.Gat.manager.istepscasemanager import IStepsCaseManager
from gateside.autotesting.Gat.manager.webuielementmanager import WebUIElementManager
from gateside.autotesting.Gat.manager.webuistepparametermanager import WebUIStepParameterManager
from gateside.autotesting.Gat.manager.webuistepscasemanager import WebUIStepsCaseManager

class TestObjectManagerFactory(object):
    '''
    测试对象管理器工厂
    '''
    
    @staticmethod
    def get_object_manager(managertype):
        
        '''根据managertype,返回管理器实例'''
        result=None
        if managertype==ObjectManagerType.ISTEPCASEMANAGER:
            result=IStepsCaseManager()
        
        if managertype==ObjectManagerType.ISTEPPARAMETERMANAGER:
            result=IStepParameterManager()
            
        if managertype==ObjectManagerType.WEBUIELEMENTMANAGER:
            result=WebUIElementManager()
        
        if managertype==ObjectManagerType.WEBUIPARAMETERMANAGER:
            result=WebUIStepParameterManager()
        
        if managertype==ObjectManagerType.WEBUICASEMANAGER:
            result=WebUIStepsCaseManager()
        
        return result
        
        
            
        