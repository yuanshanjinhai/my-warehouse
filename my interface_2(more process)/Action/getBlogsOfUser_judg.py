# coding=utf-8
from ProjectVar.var import *
import ConfigParser
from Util.md5_password import *
from tem_write_read import *
import json
import re

def getBlogsOfUserjudg(ex,row,result_dict):
    error_str = ""  # 创建一个记录错误信息的字符串，出现了错误信息就累加到它里面
    tem_list=[] # 创建一个临时列表，用于存储该用户所添加的所有博文的博文id，即articleId
    for ird in result_dict["data"]: # 传入的字典里有一个列表，遍历这个列表
        tem_list.append(int(ird["articleId"])) # 由于里边里的值是字典，所以取出这个字典里的博文id值，依次存储到tem_list里
    max_articleid=max(tem_list) # 取临时列表中最大的值，即最近创建的博文
    index=0 # 创建一个用于计数的变量，每循环一次+1，用来找出列表里的第几个值是最近创建的博文
    for ird in result_dict["data"]: # 再次遍历这个列表
        if int(ird["articleId"])==max_articleid: # 如果博文id值为最大，则证明这条博文就是最近创建的
            break
        index+=1

    cf = ConfigParser.ConfigParser()
    cf.read(check_url)
    section_list = cf.sections()  # 获取所有section的列表
    result_digit = 0 # 设置一个结果数字，如果出现匹配不成功，则给改数字赋值1，最终，如果改数字为0，则证明为出错，如果为1，则证明有出错
    for isc in section_list:
        if isc==ex.get_value("F"+str(row)).strip():
            option_list = cf.options(isc)  # 取到这个section下的所有option，存在列表中
            for iopt in option_list:  # 遍历option列表
                option_value_str = cf.get(isc, iopt) # 取出此option的值

                if option_value_str[0] <> "!":
                    option_value_str = option_value_str.replace("%", str(index))  # 把%替换为记录博文所在列表位置用的index
                    option_list = option_value_str.split("~")
                    if re.findall(eval(option_list[1]),str(eval('result_dict'+ option_list[0]))) <> []: # 用option_list[1]的正则表达式判断用option_list[0]拼接起来的层级结构下的值是否可匹配成功
                        pass
                    else:
                        result_digit=1
                        error_str += str(option_list[0])+":"+"未匹配出结果；"

                if option_value_str[0]=="!": # 如果配置文件值的第一个字符为！，则表示这个值是创建博文时写入的，此时已写入到临时文件，判断其对错需要从临时文件中获取数据来对比
                    option_value_str=option_value_str.replace("%",str(index)) # 把%替换为记录博文所在列表位置用的index
                    option_list=option_value_str[1::].split("~")
                    temfile_list=tem_read_last()
                    if iopt=="title":
                        temfile_str=temfile_list[2]
                    if iopt=="owner":
                        temfile_str=temfile_list[0]
                    if str(eval('result_dict'+option_list[0]))==temfile_str:
                        pass
                    else:
                        result_digit = 1
                        error_str += str(option_list[0]) + ":" + "返回值与输入值不符；"
    if result_digit==0:
        return result_dict
    else:
        return result_dict,error_str
