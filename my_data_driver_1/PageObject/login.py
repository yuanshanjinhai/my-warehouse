# coding=utf-8
from Util.ParseConfigurationFile import Parse_conf
from Util.all_display_style_wait import *
import sys
from ProjectVar.var import *
from Util.excel import *
from Util.ObjectMap import *
from Util.FormatTime import date_time
from Util.write_log import *
import time

class login_page():
    def __init__(self,driver):
        self.driver=driver
        self.ins=Parse_conf()
        self.eins=Excel_r_w(excel_path(),u"登录账号")
        for ir in range(2,self.eins.get_max_row()+1):
            if self.eins.get_value("D"+str(ir))=="y":
                self.i=str(ir)
                break

    def username(self):
        return self.eins.get_value("B"+self.i)

    def opeeurl(self):
        self.driver.get("https://www.126.com/")

    def inframe(self):
        frame_isusabled(self.driver, 10, 0.2, (By.ID,self.ins.getxpath("login","login_frame_id").strip()))

    def input_username(self):
        thisusername=get_element(self.driver,"login","username")
        thisusername.click()
        thisusername.clear()
        thisusername.send_keys(self.eins.get_value("B"+self.i))

    def input_pasword(self):
        thispassword=get_element(self.driver,"login","password")
        thispassword.click()
        thispassword.clear()
        thispassword.send_keys(self.eins.get_value("C"+self.i))

    def loginsubmit(self):
        thissubmit=get_element(self.driver,"login","login_submit")
        thissubmit.click()
        print title_contains(self.driver, 15, 0.2,self.ins.getxpath("login","home_title").strip().decode("utf-8"))
        if title_contains(self.driver, 15, 0.2,self.ins.getxpath("login","home_title").strip().decode("utf-8"))==1:
            self.eins.write_content("E"+self.i,"通过")
            self.eins.write_content("F" + self.i,date_time())
            writelog("用户"+self.eins.get_value("B"+str(self.i)).encode("utf-8")+"登录成功")
        else:
            self.eins.write_content("E" + self.i, "未通过")
            self.eins.write_content("F" + self.i, date_time())
            print u"无法找到邮箱首页的title"
            sys.exit()
        self.driver.switch_to.default_content()

if __name__=="__main__":
    from selenium import webdriver
    driver = webdriver.Ie(executable_path=r"D:\Program Files\webdriver\IEDriverServer.exe")
    ins=login_page(driver)
    ins.opeeurl()
    time.sleep(2)
    ins.inframe()
    ins.input_username()
    ins.input_pasword()
    ins.loginsubmit()
    time.sleep(10)