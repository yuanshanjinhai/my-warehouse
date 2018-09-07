# coding=utf-8
import time
import sys
from Util.excel import *
from ProjectVar.var import *
from Util.all_display_style_wait import *
from Util.keyboard import *
from selenium import webdriver

def bowser_driver():
    ed=Excel_r_w(excel_path,u"驱动地址")
    for ir in range(2,5):
        if ed.get_value("C"+str(ir)).encode("utf-8").strip()=="y":
            if ed.get_value("A"+str(ir)).encode("utf-8").strip()=="IE":
                driver=webdriver.Ie(executable_path=ed.get_value("B" + str(ir)).encode("utf-8"))
            if ed.get_value("A"+str(ir)).encode("utf-8").strip()=="Firefox":
                driver=webdriver.Firefox(executable_path=ed.get_value("B" + str(ir)).encode("utf-8"))
            if ed.get_value("A"+str(ir)).encode("utf-8").strip()=="Chrom":
                driver = webdriver.Chrome(executable_path=ed.get_value("B" + str(ir)).encode("utf-8"))
    return driver

# 获取并进入frame
def getintoframe(driver,tuple1):
    frame_isusabled(driver, 10, 0.2, tuple1)

# 退出frame
def outframe(driver):
    driver.switch_to.default_content()

# 向输入框输入内容，用clear()清空
def inputtext(driver,thisxpath,content):
    thistext=driver.find_element("xpath",thisxpath)
    thistext.click()
    thistext.clear()
    thistext.send_keys(content)

# 向输入框输入内容，用键盘清空
def inputtextkb(driver,thisxpath,content):
    thistext = driver.find_element("xpath", thisxpath)
    thistext.click()
    keyDown("ctrl")
    keyDown("a")
    keyUp("a")
    keyUp("ctrl")
    keyDown("del")
    keyUp("del")
    thistext.send_keys(content)

# 点击按钮（含显示等待）
def clicksth(driver,thisxpath,vcxpath):
    driver.find_element("xpath", thisxpath).click()
    if isvisible(driver, 10, 0.2, vcxpath)==1:
        pass
    else:
        print u"有元素未找到"

# 点击按钮（不含显示等待）
def clicksth_nodw(driver,thisxpath):
    driver.find_element("xpath", thisxpath).click()

# 显示等待
def display_wait(driver,vcxpath):
    if isvisible(driver, 10, 0.2, vcxpath)==1:
        pass
    else:
        print u"元素未找到"
        sys.exit()

# 退出frame
def outframe():
    driver.switch_to.default_content()

if __name__=="__main__":
    from selenium import webdriver
    driver=webdriver.Ie(executable_path=r"D:\Program Files\webdriver\IEDriverServer.exe")
    driver.get("https://www.baidu.com/")
    clicksth(driver, "//a[@href='http://news.baidu.com' and .='新闻']", "//a[.='举报']", 2)