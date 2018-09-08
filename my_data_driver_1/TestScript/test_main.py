# coding=utf-8
from PageObject.login import *
from PageObject.home import *
from Util.excel import *
from ProjectVar.var import *
import time

driver = webdriver.Ie(executable_path=r"D:\Program Files\webdriver\IEDriverServer.exe")
loginins=login_page(driver)
loginins.opeeurl()
time.sleep(2)
loginins.inframe()
loginins.input_username()
loginins.input_pasword()
loginins.loginsubmit()
time.sleep(2)

excelpath=excel_path()
eins=Excel_r_w(excelpath,u"联系人")

for ir in range(2,eins.get_max_row()+1):
    if eins.get_value("G"+str(ir))=="y":
        homeins = home_page(driver, ir)
        homeins.maillistsubmit()
        time.sleep(3)
        homeins.newbuild()
        time.sleep(2)
        homeins.inputname()
        homeins.inputemail()
        homeins.starlevel()
        time.sleep(2)
        homeins.mphone()
        homeins.inputremarks()
        homeins.inputsubmit()
        time.sleep(2)

homeins.logoutdef()
