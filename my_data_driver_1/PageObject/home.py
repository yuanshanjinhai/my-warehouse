# coding=utf-8
from Util.ParseConfigurationFile import Parse_conf
from Util.all_display_style_wait import *
import sys
from ProjectVar.var import *
from Util.excel import *
from Util.ObjectMap import *
from Util.FormatTime import date_time
from Util.write_log import *
from login import login_page

class home_page():
    def __init__(self,driver,i):
        self.driver=driver
        self.i=str(i)
        self.pins = Parse_conf()
        self.userins=Excel_r_w(excel_path(), u"登录账号")
        self.eins = Excel_r_w(excel_path(), u"联系人")
        loginins=login_page(driver)
        self.user=loginins.username()

    def maillistsubmit(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("home","maillist_submit"))==0:
            print u"通讯录按钮点击失败"
            sys.exit()
        get_element(self.driver, "home", "maillist_submit").click()

    def newbuild(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","new_build"))==0:
            print u"新建联系人按钮点击失败"
            sys.exit()
        get_element(self.driver, "maillist_page", "new_build").click()

    def inputname(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","name"))==0:
            print u"姓名输入框点击失败"
            sys.exit()
        thiselement=get_element(self.driver, "maillist_page", "name")
        thiselement.clear()
        thiselement.click()
        thiselement.send_keys(self.eins.get_value("B"+self.i))

    def inputemail(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","email"))==0:
            print u"email输入框点击失败"
            sys.exit()
        thiselement=get_element(self.driver, "maillist_page", "email")
        thiselement.clear()
        thiselement.click()
        thiselement.send_keys(self.eins.get_value("C"+self.i))

    def starlevel(self):
        if self.eins.get_value("D"+self.i)=="y":
            if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","star_level"))==0:
                print u"星级会员点击失败"
                sys.exit()
            else:
                get_element(self.driver, "maillist_page", "star_level").click()

    def mphone(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","m_phone"))==0:
            print u"手机号码输入框点击失败"
            sys.exit()
        thiselement = get_element(self.driver, "maillist_page", "m_phone")
        thiselement.clear()
        thiselement.click()
        thiselement.send_keys(str(self.eins.get_value("E" + self.i)))

    def inputremarks(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","remarks"))==0:
            print u"备注入框点击失败"
            sys.exit()
        thiselement = get_element(self.driver, "maillist_page", "remarks")
        thiselement.clear()
        thiselement.click()
        thiselement.send_keys(self.eins.get_value("F" + self.i))

    def inputsubmit(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","input_submit"))==0:
            print u"新建联系人确定按钮点击失败"
            sys.exit()
        get_element(self.driver, "maillist_page", "input_submit").click()
        self.eins.write_content("H" + self.i, "通过")
        self.eins.write_content("I" + self.i, date_time())
        writelog("用户" + self.user.encode("utf-8") + "创建了联系人 " + self.eins.get_value("B" + self.i).encode("utf-8"))

    def logoutdef(self):
        if visible_clicked(self.driver, 10, 0.2, self.pins.getxpath("maillist_page","logout"))==0:
            print u"退出按钮点击失败"
            sys.exit()
        get_element(self.driver, "maillist_page", "logout").click()
        if title_contains(self.driver, 15, 0.2, self.pins.getxpath("maillist_page", "logout_title").strip().decode("utf-8")) == 1:
            writelog("用户" +self.user.encode("utf-8") + "退出了系统"+"\n"+"-"*60+"\n")
            pass
        else:
            print u"退出邮箱失败或退出后的页面不正确"

if __name__=="__main__":
    userins = Excel_r_w(excel_path(), u"登录账号")
    eins = Excel_r_w(excel_path(), u"联系人")
    writelog(userins.get_value("B2").encode("utf-8")+ "创建了联系人" + eins.get_value("B2").encode("utf-8"))


