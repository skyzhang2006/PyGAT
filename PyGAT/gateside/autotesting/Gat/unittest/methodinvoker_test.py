'''
Created on 2015-4-3

@author: Devuser
'''
import unittest

from gateside.autotesting.Gat.util.methodinvoker import MethodInvoker
from gateside.autotesting.settings import GlobalConfig


class Test(unittest.TestCase):


    def testName(self):
        GlobalConfig.StepParameterFilePath=GlobalConfig.get_parameter_filepath("ComponetParameters.xml")
        instance=MethodInvoker.get_instance("gateside.autotesting.iat_stepgroups.teststep","TestStep","gateside.autotesting.iat_stepgroups.teststep".split("."))
        method=MethodInvoker.get_method(instance,"setpmethod")
        args=list()
        MethodInvoker.invoke_method(method,args)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()