#coding=utf-8
'''
Created on 2015-4-7

@author: gat runner
'''
import unittest
from gateside.autotesting.Gat.executor.istepscaseexecutor import IStepsCaseExecutor


class TestStep(unittest.TestCase):

    def testDemoTest(self):
        executor=IStepsCaseExecutor("demotestcase.xml","testmethod")
        executor.execute()
        
    
        

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()