#coding=utf-8
from ProjectVar.var import *
import ConfigParser
import requests
from Util.excel import *
from Util.md5_password import *
from tem_write_read import *
from general_judg import *
from getBlogsOfUser_judg import *
from getBlogContent_judg import *
from getBlogsContent_judg import *
from delete_judg import *
from getBlogContent_url import *
from getBlogsContent_url import *
import sys
import json
import re

class return_dict():
    def __init__(self,ex,row):
        self.ex = ex
        self.row=row

    def join_url(self): # 拼接requests方法的url参数
        if self.ex.get_value("E"+str(self.row))=="post":
            if self.ex.get_value("F"+str(self.row)).strip()=="register_normal" or self.ex.get_value("F"+str(self.row)).strip()=="register_error":
                thisurl=url+"/"+"register"+"/"
            else:
                thisurl=url+"/"+self.ex.get_value("F"+str(self.row)).strip()+"/"
            return thisurl
        if self.ex.get_value("E"+str(self.row))=="get":
            if self.ex.get_value("F"+str(self.row)).strip()=="getBlogContent":
                value_articleId = getBlogContenturl()
                thisurl = url + "/" + str(self.ex.get_value("F" + str(self.row))).strip() + "/" + value_articleId
            elif self.ex.get_value("F"+str(self.row)).strip()=="getBlogsContent":
                value_articleId = getBlogsContenturl().strip()
                thisurl = url + "/" + str(self.ex.get_value("F" + str(self.row))).strip() + "/articleIds"+ "=" + value_articleId
            else:
                thisurl=url+"/"+str(self.ex.get_value("F"+str(self.row))).strip()+"/"+str(self.ex.get_value("G"+str(self.row))).strip()
            return thisurl

    def get_json(self): # 拼接requests方法的json串参数
        thisjson = self.ex.get_value("G" + str(self.row)).encode("utf-8").strip()
        if self.ex.get_value("F"+str(self.row))=="login": # 如果用例的F列是login，则证明该用例为登录，需要对密码进行md5加密
            thisdict=json.loads(thisjson) # 先把json转化成字典
            thispassword=md5ps(thisdict["password"])
            thisdict["password"]=thispassword
            thisjson=json.dumps(thisdict)

        if self.ex.get_value("F" + str(self.row)) == "create":  # 如果用例的F列是create，则为创建博文，则需要从临时文件里取token
            thisdict = json.loads(thisjson)
            utca_list=tem_read_last()
            if utca_list==0:
                print "临时存储文件tem_login_info.txt为空"
                sys.exit()
            thisdict["token"]=utca_list[1]
            thisdict["userid"]=utca_list[0]
            thisjson = json.dumps(thisdict)

        if self.ex.get_value("F" + str(self.row)) == "getBlogsOfUser":  # 如果用例的F列是getBlogsOfUser，则为查询用户博文，则需要从临时文件里取token
            thisdict = json.loads(thisjson)
            utca_list=tem_read_last()
            if utca_list==0:
                print "临时存储文件tem_store.txt为空"
                sys.exit()
            thisdict["token"]=utca_list[1]
            thisdict["userid"]=int(utca_list[0])
            thisjson = json.dumps(thisdict)

        if self.ex.get_value("F" + str(self.row)) == "delete":  # 如果用例的F列是delete，则为删除用户博文，则需要从临时文件里取userid，token和博文id
            thisdict = json.loads(thisjson)
            file_list=tem_read_all()
            if file_list==0:
                print "临时存储文件tem_store.txt为空"
                sys.exit()
            thisdict["userid"]=int(file_list[0].split("||")[0])
            thisdict["token"]=str(file_list[0].split("||")[1])
            articleId_list=[]
            for ifl in file_list:
                articleId_list.append(ifl.split("||")[-1])
            thisdict["articleId"] = str(articleId_list)
            thisjson = json.dumps(thisdict)

        return thisjson

    def getresult(self): # 获得post或get方法的结果
        if self.ex.get_value("E" + str(self.row)).strip() == "post":  # 如果调用方法为post
            result_json = requests.post(self.join_url(),self.get_json())  # 通过parameter_join.py里的拼接url函数和拼接json函数来获得url和json，并使用post方法
            if result_json.status_code <> 200:
                return result_json.status_code
            result_dict = result_json.json() # 把返回的json串转化为字典
            tem_write(self.ex,self.row,result_dict) # 调用tem_wirte函数，把userid,token,articleI，articleId四个值存入tem_store.txt
            return result_dict
        if self.ex.get_value("E" + str(self.row)).strip() == "get":  # 如果调用方法为get
            result_json = requests.get(self.join_url().strip())
            if result_json.status_code <> 200:
                return result_json.status_code
            result_dict = result_json.json() # 将返回的json转化为字典
            return result_dict

    def judge(self): # 判断post或get方法的执行结果是否正确
        result_dict=self.getresult()
        if isinstance(result_dict,int):
            return result_dict
        if self.ex.get_value("F" + str(self.row)).strip()=="getBlogsOfUser":
            result_dict=getBlogsOfUserjudg(self.ex,self.row,result_dict)
            return result_dict
        elif self.ex.get_value("F" + str(self.row)).strip()=="getBlogContent":
            result_dict=getBlogContentjudg(self.ex,self.row,result_dict)
            return result_dict
        elif self.ex.get_value("F" + str(self.row)).strip()=="getBlogsContent":
            result_dict=getBlogsContentjudg(self.ex,self.row,result_dict)
            return result_dict
        elif self.ex.get_value("F" + str(self.row)).strip()=="delete":
            result_dict=deletejudg(result_dict)
            return result_dict
        else:
            result_dict=generaljudg(self.ex, self.row, result_dict)
            return result_dict


if __name__=="__main__":
    ex = Excel_r_w(excel_path, u"用例")
    row=2
    ins=return_dict(ex,row)
    print ins.judge()