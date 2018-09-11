# coding=utf-8
import ConfigParser
from tem_write_read import *
from ProjectVar.var import *
import json
import re
import requests

def deletejudg(result_dict):
    cf = ConfigParser.ConfigParser()
    cf.read(check_url)
    result_digit = 0
    error_str="" # 创建一个记录错误信息的字符串，出现了错误信息就累加到它里面
    file_list=tem_read_all()
    for iopt in cf.options("delete"):
        if iopt=="code":
            option_value_list = cf.get("delete",iopt).split("~")
            if re.findall(eval(option_value_list[1]), str(eval('result_dict' + option_value_list[0]))) <> []:  # 用option_value_list[1]的正则表达式判断用option_value_list[0]拼接起来的层级结构下的值是否可匹配成功
                pass
            else:
                result_digit = 1
                error_str += "code" + "未匹配出结果；"

        if iopt=="userid":
            option_value_list = cf.get("delete",iopt)[1::].split("~")
            if str(eval('result_dict' + option_value_list[0]))==file_list[0].split("||")[0]:
                pass
            else:
                result_dict=1
                error_str = "userid" + "返回值与输入值不符；"
                #write_tem_error_str(error_str)

        if iopt=="articleId":
            option_value_list = cf.get("delete",iopt)[1::].split("~")
            if str(eval('result_dict' + option_value_list[0]))==file_list[0].split("||")[-1]:
                pass
            else:
                result_dict=1
                error_str += "articleId" + "返回值与输入值不符；"

    # 执行一下批量删除博文接口，查询已删除的博文，如果返回结果里的code为00，则证已删除的博文还在，删除失败
    tem_store_list=tem_read_all()
    articleId_str=""
    for item in tem_store_list:
        articleId_str += item.split("||")[-1].strip()+","
    result_dict=requests.get(url+"/getBlogsContent/articleIds="+str(articleId_str[0:-1])).json()
    if result_dict["code"]<>"00":
        pass
    else:
        error_str += "数据未删除"

    clear_file()

    if result_digit==0:
        return result_dict
    else:
        return result_dict,error_str