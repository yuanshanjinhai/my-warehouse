# coding=utf-8
from ProjectVar.var import *
from Util.excel import *
from Util.FormatTime import date_time

class write_runlog():
    def __init__(self,fp,ex,row):
        self.ex=ex
        self.fp=fp
        self.row=row

    def general_method(self,value):
        if str(self.ex.get_value("F"+str(self.row)))=="register_error" or str(self.ex.get_value("F"+str(self.row)))=="register_normal":
            url_split="register"
        else:
            url_split=str(self.ex.get_value("F"+str(self.row)))
        self.fp.write(date_time()+", "+self.ex.get_value("M"+str(self.row)).encode("utf-8")+", "+"调用了"+url_split+"接口，"+value+"\n")

    def write_rl(self,result):
        if isinstance(result,int)==1:
            self.general_method("失败，返回值："+str(result))
        else:
            self.general_method("成功，返回值："+str(result))
