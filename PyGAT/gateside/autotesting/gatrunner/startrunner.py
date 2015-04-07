'''
Created on 2015-4-7

@author: Devuser
'''

from gateside.autotesting.gatrunner.runnersettings import RunnerSettings
from gateside.autotesting.settings import GlobalConfig
from gateside.autotesting.Gat.manager.stepscasemanager import StepsCaseManager
from gateside.autotesting.Gat.util.parseXML2element import ParseXMLToElement
import os
import shutil

def create_testproject():
    projectpath=RunnerSettings.get_rootdir()+GlobalConfig.get_slash()+RunnerSettings.TESTPROJECTNAME
    if os.path.exists(projectpath):
        shutil.rmtree(projectpath)
    os.makedirs(projectpath)
    package_init_file=file(projectpath+GlobalConfig.get_slash()+"__init__.py","w")
    package_init_file.close()
    os.makedirs(projectpath+GlobalConfig.get_slash()+"generation")
    package_init_file=file(projectpath+GlobalConfig.get_slash()+"generation"+GlobalConfig.get_slash()+"__init__.py","w")
    package_init_file.close()


def genreate_testcase():
    testcasefilefolder=RunnerSettings.get_rootdir()+GlobalConfig.get_slash()+RunnerSettings.TESTPROJECTNAME+GlobalConfig.get_slash()+"generation"
    print(testcasefilefolder)
    for xmlfile in os.listdir(RunnerSettings.get_xml_folder()):
        if xmlfile.endswith("testcase.xml"):
            testcaselist=get_testcaselist(RunnerSettings.get_xml_folder()+GlobalConfig.get_slash()+xmlfile)
            testmethodcontent=""
            print(len(testcaselist))
            for testcase in testcaselist:
                print(create_testmethod_content(testcase,xmlfile))
                testmethodcontent=testmethodcontent+create_testmethod_content(testcase,xmlfile)+"\n"
            print(testmethodcontent)
            testclass_content=create_testclass_content(testcase.StepGroup,testmethodcontent)
            testcasefile=file(testcasefilefolder+GlobalConfig.get_slash()+xmlfile.split(".")[0]+".py","w")
            testcasefile.write(testclass_content)
            testcasefile.close()

def create_testmethod_content(testcase,xmlfile):
    testmethod_template=open(RunnerSettings.get_method_tempatepath(),'r')
    testmethod_content=testmethod_template.read()
    testmethod_content=testmethod_content.replace('{TESTMETHOD}',testcase.Name)
    testmethod_content=testmethod_content.replace('{CASEFILENAME}',xmlfile)
    testmethod_content=testmethod_content.replace('{CASEID}',testcase.ID)  
    testmethod_template.close()
    return  testmethod_content

def create_testclass_content(classname,classcontent):
    testclass_template=open(RunnerSettings.get_testclass_tempatepath(),'r')
    testclass_content=testclass_template.read()
    testclass_content=testclass_content.replace('{CLASSNAME}',classname)
    testclass_content=testclass_content.replace('{TESTMETHODS}',classcontent)
    testclass_template.close()
    return  testclass_content

def get_testcaselist(xmlFilepath):
    GlobalConfig.TestCaseFilePath=xmlFilepath
    root=ParseXMLToElement.get_root(xmlFilepath)
    elementlist=ParseXMLToElement.get_children_by_tag(root,"TestCase")
    testcaselist=list()
    casemanager=StepsCaseManager()
    for element in elementlist:
        testcase=casemanager.initialize_testcase(element)
        testcaselist.append(testcase)
    return testcaselist
        
        


if __name__ == '__main__':
    create_testproject()
    genreate_testcase()
    
    