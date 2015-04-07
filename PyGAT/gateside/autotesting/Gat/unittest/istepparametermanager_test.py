'''
Created on 2015-4-2

@author: Devuser
'''
import unittest

from gateside.autotesting.Gat.manager.istepparametermanager import IStepParameterManager
from gateside.autotesting.settings import GlobalConfig

class Test(unittest.TestCase):


    def testName(self):
        GlobalConfig.StepParameterFilePath=r"E:\Git\OpenPySource\PySelenium\Content\ComponetParameters.xml"
        istepparametermanager=IStepParameterManager()
        parameter=istepparametermanager.get_item("InlandHotelListHotelFilterCheck")
        print(parameter.Parameters["locationFilter"])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()