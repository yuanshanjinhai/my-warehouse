# coding=utf-8
from Util.FormatTime import date_time
from Util.excel import *
from Util.write_log import *
from ProjectVar.var import *
from selenium import webdriver
from Action.action import *
from Util.all_display_style_wait import *
import time

driver=bowser_driver()
driver.get("https://www.126.com")
driver.maximize_window()
time.sleep(3)

ec=Excel_r_w(excel_path,u"用例")
wl=Writelog(log_path)
for ir in range(2,ec.get_max_row()+1):
    if ec.get_value("L" + str(ir))=="n":
        ec.write_content("M" + str(ir), "")
        continue
    if ec.get_value("E" + str(ir))=="y":
        action="inputtextkb"+"(driver,"
    else:
        action=ec.get_value("G" + str(ir))+"(driver,"
    if ec.get_value("G" + str(ir))=="outframe":
        action="driver.switch_to.default_content()"
        print "action=", action
        try:
            exec (action)
            ec.write_content("M" + str(ir), "通过")
            ec.write_datetime("N"+str(ir))
            wl.writelog(date_time(), ec.get_value("O" + str(ir)).encode("utf-8"), "调用了函数",ec.get_value('G' + str(ir)).encode("utf-8"), ec.get_value('M' + str(ir)).encode("utf-8"))
            time.sleep(int(ec.get_value("K" + str(ir))))
        except:
            print u"用例" + str(ir - 1).decode("utf-8") + u"未通过"
            ec.write_content("M" + str(ir), "未通过")
            ec.write_datetime("N" + str(ir))
            wl.writelog(date_time(),ec.get_value("O" + str(ir)).encode("utf-8"),"调用了函数",ec.get_value('G' + str(ir)).encode("utf-8"),ec.get_value('M' + str(ir)).encode("utf-8"))
            time.sleep(int(ec.get_value("K" + str(ir))))
        continue
    if ec.get_value("G" + str(ir)) == "getintoframe":
        action = action + "(" + "By.XPATH," + "\"" + ec.get_value("H" + str(ir)) + "\"" + ")" + ")"
        print "action1=", action
    else:
        for ighi in "HIJ":
            if ec.get_value(ighi+str(ir))==None:
                continue
            if ighi=="J":
                action = action + "u"+"\"" + ec.get_value(ighi + str(ir)) + "\"" + ","
            else:
                action=action+"\""+ec.get_value(ighi+str(ir))+"\""+","
        action=action[0:-1]+")"
    print "action=", action
    print "----------"
    try:
        exec(action)
        ec.write_content("M" + str(ir), "通过")
        ec.write_datetime("N" + str(ir))
        wl.writelog(date_time(),ec.get_value("O" + str(ir)).encode("utf-8"),"调用了函数",ec.get_value('G' + str(ir)).encode("utf-8"),ec.get_value('M' + str(ir)).encode("utf-8"))
        time.sleep(int(ec.get_value("K" + str(ir))))
    except:
        print u"用例"+str(ir-1).decode("utf-8")+u"未通过"
        ec.write_content("M" + str(ir), "未通过")
        ec.write_datetime("N" + str(ir))
        wl.writelog(date_time(),ec.get_value("O" + str(ir)).encode("utf-8"),"调用了函数",ec.get_value('G' + str(ir)).encode("utf-8"),ec.get_value('M' + str(ir)).encode("utf-8"))
        time.sleep(int(ec.get_value("K" + str(ir))))

wl.writelog("-"*100+"\n")
ec.save_content()
wl.closefp()
driver.quit()

if __name__=="__main__":
    pass