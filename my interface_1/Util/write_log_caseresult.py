# coding=utf-8
from Action.parameter_join import *
from Util.FormatTime import date_time

class Writelog():
    def __init__(self,log_path):
        self.log_path=log_path
        self.fp=open(log_path,"a")

    def writelog(self,*args):
        for i in args:
            self.fp.write(i)
            self.fp.write(", ")
        self.fp.write("\n")

    def closefp(self):
        self.fp.close()

def writelogexcel(ex,wl,scode,tcode,ir):
    if scode<>"200" and tcode<>str(ex.get_value("O"+str(ir))):
        print u"用例%d测试未通过，错误信息：%d" % (ir - 1, scode)
        wl.writelog(date_time(), ex.get_value("S" + str(ir)).encode("utf-8").strip(),"调用了方法:" + ex.get_value("E" + str(ir)).encode("utf-8").strip(), joinurl(ir), joinjson(ir), "失败")
        ex.write_content("Q"+str(ir),"未通过")
        ex.write_content("R" + str(ir),scode)
    if scode=="200" and tcode<>str(ex.get_value("O"+str(ir))):
        print u"用例%d测试未通过，错误信息：%s" % (ir - 1, tcode)
        wl.writelog(date_time(), ex.get_value("S" + str(ir)).encode("utf-8").strip(),"调用了方法:" + ex.get_value("E" + str(ir)).encode("utf-8").strip(), joinurl(ir), joinjson(ir), "失败")
        ex.write_content("Q" + str(ir), "未通过")
        ex.write_content("R" + str(ir), tcode)
    if scode=="200" and tcode==str(ex.get_value("O"+str(ir))):
        print u"用例%d测试通过"%(ir - 1)
        wl.writelog(date_time(), ex.get_value("S" + str(ir)).encode("utf-8").strip(),"调用了方法:" + ex.get_value("E" + str(ir)).encode("utf-8").strip(), joinurl(ir), joinjson(ir), "成功")
        ex.write_content("Q" + str(ir), "通过")
        ex.write_content("R" + str(ir),tcode)

if __name__=="__main__":
    ex = Excel_r_w(excel_path, u"用例")
    print str(ex.get_value("F" + str(9)))
    print str(ex.get_value("O" + str(9)))
    print bool(str(ex.get_value("F" + str(9)))=="register")
    print bool(str(ex.get_value("O" + str(9)))=="00")
    print str(ex.get_value("O" + str(9)))
    print bool(str(ex.get_value("F" + str(8)))=="register" and str(ex.get_value("O" + str(9)))=="00")
