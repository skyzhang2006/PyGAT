#coding=utf-8
'''
Created on 2015-4-7

@author: 张天得
'''


def singleton(cls,*args,**kw):
    instances={}
    def _singleton():
        if cls not in instances:
            instances[cls]=cls(*args,**kw)
        return instances[cls]
    return _singleton




@singleton
class StepValuePool(object):
    '''
    存数Step method中间数据
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.valuepool=dict()
    
    def put_value(self,key,value):
        self.valuepool[key]=value
    
    def get_value(self,key):
        result=None
        try:
            result=self.valuepool[key]
        except Exception,ex:
            pass
        return result
    
    def clear_all(self):
        self.valuepool.clear()
    
    
        