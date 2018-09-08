# coding=utf-8
from Util.ParseConfigurationFile import Parse_conf
import time

ins=Parse_conf()

def get_element(driver,section,key):
    return driver.find_element("xpath",ins.getxpath(section,key).strip())
    # thiselement

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Ie(executable_path=r"D:\Program Files\webdriver\IEDriverServer.exe")
    driver.get("https://www.126.com/")
    time.sleep(2)
    print get_element(driver,"login","login_frame")