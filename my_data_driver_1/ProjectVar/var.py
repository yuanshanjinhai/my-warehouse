#coding=utf-8
import os
from selenium import webdriver
import platform

# ini配置文件路径：
ini_path=os.path.dirname(os.path.dirname(__file__))+"conf\\locationEelement.ini"

# excel路径：
def excel_path():
    excel_path=os.path.dirname(os.path.dirname(__file__))+"\\TestData\\data.xlsx"
    return excel_path

# browser_path路径
def ini_path():
    if platform.system() == "Windows":
        locationEelement_path = os.path.dirname(os.path.dirname(__file__)) + "\\conf\\locationEelement.ini"
    else:
        locationEelement_path = os.path.dirname(os.path.dirname(__file__)) + "//conf//locationEelement.ini"
    return locationEelement_path

def log_path():
    return os.path.dirname(os.path.dirname(__file__)) +"//test_log//test_log.log"