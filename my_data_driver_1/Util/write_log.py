# coding=utf-8
from ProjectVar.var import log_path
from Util.FormatTime import date_time

logpath=log_path()
def writelog(content):
    with open(logpath,"a") as fp:
        fp.write(date_time()+","+content+"\n")

if __name__=="__main__":
    from Util.excel import *
    from ProjectVar.var import *
    logpath = "D:\\test\\test.log"
    userins = Excel_r_w(excel_path(), u"登录账号")
    eins = Excel_r_w(excel_path(), u"联系人")
    print userins.get_value("B2")
    print type(userins.get_value("B2"))
    writelog("，用户"+userins.get_value("B2").encode("utf-8")+"\n")
    #writelog(date_time()+ ",用户" + userins.get_value("B2") + "创建了联系人：" + eins.get_value("B2").decode("utf-8"))
