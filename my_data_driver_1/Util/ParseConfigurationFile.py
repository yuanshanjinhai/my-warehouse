import ConfigParser
from ProjectVar.var import *
from selenium import webdriver

class Parse_conf():
    def __init__(self):
        self.cf= ConfigParser.ConfigParser()
        self.cf.read(ini_path())

    def getxpath(self,section,key):
        thisxpath=self.cf.get(section,key)
        return thisxpath

if __name__=="__main__":
    ins=Parse_conf()
    print ins.bowser_path()
    driver=webdriver.Ie(executable_path=r"D:\Program Files\webdriver\IEDriverServer.exe")
    print ins.getxpath("login","login_frame")