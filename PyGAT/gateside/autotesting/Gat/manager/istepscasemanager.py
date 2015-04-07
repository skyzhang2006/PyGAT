#coding=utf-8
'''
Created on 2015-4-1

@author: 张天得
'''

from gateside.autotesting.Gat.manager.stepscasemanager import StepsCaseManager
from gateside.autotesting.Gat.util.classtracer import ClassTracer
from gateside.autotesting.Gat.util.methodtracer import MethodTracer

@ClassTracer
class IStepsCaseManager(StepsCaseManager):
    '''
    classdocs
    '''

    @MethodTracer("IStepsCaseManager")
    def __init__(self):
        '''
        Constructor
        '''
        StepsCaseManager.__init__(self)
    
    
        