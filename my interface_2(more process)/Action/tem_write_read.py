# coding=utf-8
import re
from Util.excel import *
from ProjectVar.var import *

def tem_write(ex,row,result_dict):
    # 如果F列的值为login，且预期的返回code和实际的返回code都是00，则证明是登录且成功，则需存储userid和token
    if ex.get_value("F" + str(row)).strip() == "login" and str(ex.get_value("H" + str(row)).strip()) == "00" and str(result_dict["code"]) == "00":
        with open(tem_login_info_path,"a") as fp:
            fp.write(str(result_dict["userid"])+"||"+str(result_dict["token"])+"||")
    # 如果F列的值为create，且预期的返回code和实际的返回code都是00，则证明是创建博文且成功，则需存储title和content
    if str(ex.get_value("F" + str(row))).strip() == "create" and str(ex.get_value("H" + str(row)).strip()) == "00" and str(result_dict["code"]) == "00":
        with open(tem_login_info_path,"r") as fp:
            login_info_str=fp.readlines()[0]
        with open(tem_store_path,"a") as fp2:
            fp2.write(login_info_str+str(result_dict["data"][0]["title"]) + "||")
            fp2.write(str(result_dict["data"][0]["content"]) + "||")
    # 如果F列的值为getBlogsOfUser，且预期的返回code和实际的返回code都是00，则证明是查询用户博文且成功，则需存储articleId
    if ex.get_value("F" + str(row)).strip() == "getBlogsOfUser" and str(ex.get_value("H" + str(row)).strip()) == "00" and str(result_dict["code"]) == "00":
        fp = open(tem_store_path, "r")
        tem_list=fp.readlines()[-1].strip().split("||")
        fp.close()
        fp = open(tem_store_path, "a")
        for ird in result_dict["data"]:
            for k,v in ird.items():
                if k=="content" and v==tem_list[3]:
                    fp.write(str(ird["articleId"])+"\n")
                    fp.close()
                    return

def tem_read_last():
    fp=open(tem_login_info_path, "r") # 从tem_store中读取userid,token.title,content,articleI几个值
    tem_file_list=fp.readlines()
    if tem_file_list<>[]:
        uttca_str = tem_file_list[-1].strip()
    else:
        fp.close()
        return 0
    fp.close()
    uttca_list = uttca_str.split("||")  # 把userid,token.title,content,articleI存入一个列表,uttca即userid,token.title,content,articleI几个值的首字母组合
    return uttca_list

def tem_read_all():
    fp = open(tem_store_path, "r")  # 从tem_store中读取userid,token.title,content,articleI几个值
    file_list = fp.readlines()
    if file_list<>[]:
        return file_list
    else:
        return 0

def clear_file():
    fp0 = open(tem_store_path, "w")
    fp0.write("")
    fp0.close()

    fp1 = open(tem_login_info_path, "w")
    fp1.write("")
    fp1.close()
