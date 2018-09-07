# coding=utf-8
from ProjectVar.var import excel_path
import re

class CheckCIN():
    def __init__(self,ex):
        self.ex=ex

    def check(self):
        count = 0
        for ir in range(2, self.ex.get_max_row() + 1):
            if self.ex.get_value("A"+str(ir))==None:
                print "第"+str(ir)+"行"+"无id"
                count=1
        countid = 1
        for ir in range(2, self.ex.get_max_row() + 1):
            if count==1:
                break
            if re.findall(r"(?<!\D)\d+(?!\D+)",str(self.ex.get_value("A"+str(ir))))==[]:
                print "第%d行，用例id只能是数字"%(ir)
                count=1
                break
            if int(self.ex.get_value("A"+str(ir)))<>countid:
                count=1
                print "用例id不连续，行数：%d"%(ir)
            countid+=1

        for ir in range(2,self.ex.get_max_row()+1):
            if self.ex.get_value("I"+str(ir))==None:
                print "第"+str(ir)+"行"+"I列为空"
                count=1
            if self.ex.get_value("E"+str(ir))==None and self.ex.get_value("I"+str(ir))=="y":
                print "第"+str(ir)+"行"+"E列为空"
                count=1
            if self.ex.get_value("F"+str(ir))==None and self.ex.get_value("I"+str(ir))=="y":
                print "第"+str(ir)+"行"+"F列为空"
                count = 1
            if self.ex.get_value("G"+str(ir))==None and self.ex.get_value("I"+str(ir))=="y":
                print "第"+str(ir)+"行"+"G列为空"
                count = 1
            if self.ex.get_value("H"+str(ir))==None and self.ex.get_value("I"+str(ir))=="y":
                print "第"+str(ir)+"行"+"H列为空"
                count = 1
            if self.ex.get_value("M"+str(ir))==None and self.ex.get_value("I"+str(ir))=="y":
                print "第"+str(ir)+"行"+"M列为空"
                count = 1
        return count

if __name__=="__main__":
    from Util.excel import *
    from ProjectVar.var import *
    ex=Excel_r_w(excel_path,u"用例")
    eins=CheckCIN(ex)
    eins.check()