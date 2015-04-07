'''
Created on 2015-4-1

@author: Devuser
'''
import unittest
from gateside.autotesting.Gat.manager.webuielementmanager import WebUIElementManager
from gateside.autotesting.Gat.util.globalconfig import GlobalConfig


class Test(unittest.TestCase):


    def testName(self):
        GlobalConfig.UIElementFilePath=r"E:\Git\OpenPySource\PySelenium\Content\UIElements.xml"
        istepscasemanager=WebUIElementManager()
        testCase=istepscasemanager.get_item("WebSite.InlandHotel.HotelList.CityTextBox")
        print(testCase.ControllType)
    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()