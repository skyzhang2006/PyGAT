#coding=utf-8

'''
Created on 2015-4-1

@author: Devuser
'''


from gateside.autotesting.Gat.manager.stepparametermanager import StepParameterManager
from gateside.autotesting.Gat.util.classtracer import ClassTracer
from gateside.autotesting.Gat.util.methodtracer import MethodTracer

@ClassTracer
class IStepParameterManager(StepParameterManager):
    '''
    classdocs
    '''

    @MethodTracer("IStepParameterManager")
    def __init__(self):
        '''
        Constructor
        '''
        StepParameterManager.__init__(self)
        