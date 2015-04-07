#coding=utf-8
'''
Created on 2015-3-31

@author: 张天得
'''

class StepParameter(object):
    '''
    所有参数数据对象的基类
    '''


    def __init__(self):
        '''
        构造函数
        '''
        self.ConnectionString=None
        self.CommandText=None
        self.Parameters={}
        