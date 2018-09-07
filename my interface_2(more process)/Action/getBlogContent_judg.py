# coding=utf-8
from ProjectVar.var import *
import ConfigParser
from Util.md5_password import *
from tem_write_read import *
import json
import re

def getBlogContentjudg(ex,row,result_dict):
    cf = ConfigParser.ConfigParser()
    cf.read(check_url)
    section_list = cf.sections()  # 获取所有section的列表
    error_str="" # 创建一个记录错误信息的字符串，出现了错误信息就累加到它里面
    result_digit = 0  # 设置一个结果数字，如果出现匹配不成功，则给改数字赋值1，最终，如果改数字为0，则证明为出错，如果为1，则证明有出错
    for isc in section_list:
        if isc == ex.get_value("F" + str(row)).strip():
            option_list = cf.options(isc)  # 取到这个section下的所有option，存在列表中
            for iopt in option_list:  # 遍历option列表
                option_str = cf.get(isc, iopt)  # 取出此option的值

                if option_str[0] <> "!":
                    tem_list = option_str.split("~")
                    if re.findall(eval(tem_list[1]), str(eval('result_dict' + tem_list[0]))) <> []:  # 用tem_list[1]的正则表达式判断用tem_list[0]拼接起来的层级结构下的值是否可匹配成功
                        pass
                    else:
                        result_digit = 1
                        error_str += str(tem_list[0]) + ":" + "未匹配出结果；"
                    if result_digit == 0:
                        return result_dict
                    else:
                        return result_dict, error_str

                if option_str[0] == "!":  # 如果配置文件值的第一个字符为！，则表示这个值是创建博文时写入的，此时已写入到临时文件，判断其对错需要从临时文件中获取数据来对比
                    tem_list = option_str[1::].split("~")
                    temfile_list = tem_read_last()
                if iopt == "title":
                    temfile_str = temfile_list[2]
                if iopt == "owner":
                    temfile_str = temfile_list[0]
                if iopt == "content":
                    temfile_str = temfile_list[3]
                if iopt == "articleId":
                    temfile_str = temfile_list[4]
                if eval(result_dict + tem_list[0]) == temfile_str:
                    pass
                else:
                    result_digit = 1
                    error_str += str(tem_list[0]) + ":" + "返回值与输入值不符；"

    if result_digit==0:
        return result_dict
    else:
        return result_dict,error_str