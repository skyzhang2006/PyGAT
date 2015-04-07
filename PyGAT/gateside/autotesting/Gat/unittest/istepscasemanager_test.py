'''
Created on 2015-4-1

@author: Devuser
'''
import unittest
from gateside.autotesting.Gat.manager.istepscasemanager import IStepsCaseManager
from gateside.autotesting.settings import GlobalConfig


class Test(unittest.TestCase):


    def testName(self):
        print(GlobalConfig.get_rootdir())
#         GlobalConfig.TestCaseFilePath=r"E:\\Git\\OpenPySource\\PySelenium\\Content\\TestCase.xml"
#         istepscasemanager=IStepsCaseManager()
#         testCase=istepscasemanager.get_item("WebSite.InlandHotel.HotelListPageCheck")
#         print(testCase.ID)
#         testComponet=testCase.TestSteps[0]
#         print(testComponet.StepPackage)
  
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()