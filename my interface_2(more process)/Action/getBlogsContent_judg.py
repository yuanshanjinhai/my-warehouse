# coding=utf-8
from ProjectVar.var import *
import ConfigParser
from Util.md5_password import *
from tem_write_read import *
import json
import re

def getBlogsContentjudg(ex,row,result_dict):
    cf = ConfigParser.ConfigParser()
    cf.read(check_url)
    section_list = cf.sections()  # 获取所有section的列表
    error_str = ""  # 创建一个记录错误信息的字符串，出现了错误信息就累加到它里面
    result_digit = 0  # 设置一个结果数字，如果出现匹配不成功，则给数字赋值1，最终，如果改数字为0，则证明w未出错，如果为1，则证明有出错
    for isc in section_list: # 取出配置文件中getBlogsContent下的所有options
        if isc == ex.get_value("F" + str(row)).strip():
            option_list = cf.options(isc)  # 取到这个section下的所有option，存在列表中
            break
    tem_store_list=tem_read_all() # 取到临时存储文件里的所有行
    if len(tem_store_list)<>len(result_dict["data"]): # 如果临时存储文件里的数据数量不等于返回的博文数量，则写入错误信息，返回结果
        error_str="输入的博文数量为%s，但返回的博文数量为%d"%((len(tem_store_list)),(len(result_dict["data"])))
        return result_dict, error_str
    for item_store in tem_store_list: # 遍历临时存储文件里的所有行
        index=0
        for ird in result_dict["data"]: # 遍历返回的json串包含的博文数据列表
            if item_store.strip().split("||")[-1]==ird["articleId"]: # 如果临时存储文件里的articleId和返回的json串里的articleId相等，则证明他们是同一条博文，可以进行比较
                for iopt in option_list:  # 遍历option列表
                    option_value_str = cf.get("getBlogsContent", iopt)  # 取出此option的值

                    if option_str[0] <> "!": # 如果这个option的第一个值不是！，则需要直接用服务器返回json里的值与ini文件里的正则表达式进行对比
                        option_value_str = option_value_str.replace("%", str(index))  # 把%替换为记录博文所在列表位置用的index
                        option_value_list = option_value_str.split("~")
                        if re.findall(eval(option_value_list[1]), str(eval('result_dict' + option_value_list[0]))) <> []:  # 用option_value_list[1]的正则表达式判断用option_value_list[0]拼接起来的层级结构下的值是否可匹配成功
                            pass
                        else:
                            result_digit = 1
                            error_str += str(option_value_list[0]) + ":" + "未匹配出结果；"

                    if option_str[0] == "!":  # 如果配置文件值的第一个字符为！，则表示这个值是创建博文时写入的，此时已写入到临时文件，判断其对错需要从临时文件中获取数据来对比
                        option_str = option_str.replace("%", str(index))  # 把%替换为记录博文所在列表位置用的index
                        option_value_list = option_str[1::].split("~")
                        if iopt == "title":
                            if eval('result_dict'+option_value_list[0])==item_store[2]:
                                pass
                            else:
                                result_digit = 1
                                error_str += "title值返回错误；"
                        if iopt == "owner":
                            if eval('result_dict'+option_value_list[0])==item_store[-1]:
                                pass
                            else:
                                result_digit = 1
                                error_str += "owner值返回错误；"
                        if iopt == "content":
                            if eval('result_dict'+option_value_list[0])==item_store[3]:
                                pass
                            else:
                                result_digit = 1
                                error_str += "content值返回错误；"
                        if iopt == "articleId":
                            if eval('result_dict'+option_value_list[0])==item_store[-1]:
                                pass
                            else:
                                result_digit = 1
                                error_str += "articleId值返回错误；"
            index += 1

    if result_digit==0:
        return result_dict
    else:
        return result_dict,error_str
