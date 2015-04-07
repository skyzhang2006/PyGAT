'''
Created on 2015-3-31

@author: Devuser
'''
import unittest
from gateside.autotesting.Gat.dataobject.testcase.iteststep import InterfaceTestStep


class Test(unittest.TestCase):


    def testName(self):
        teststep=InterfaceTestStep()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()