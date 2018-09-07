# coding=utf-8
import re

class write_userlog():
    def __init__(self,fp,ex,row):
        self.fp=fp
        self.ex=ex
        self.row=row

    def write_ul(self,result):
        if isinstance(result,int)==1:
            return
        if self.ex.get_value("F"+str(self.row))=="register_normal" and result["code"]=="00":
            self.fp.write("username:"+re.findall(r"(?<=\"username\":\")\S+(?=\",\"password)",str(self.ex.get_value("G"+str(self.row))))[0]+","+"userid:"+str(result["userid"])+"\n")