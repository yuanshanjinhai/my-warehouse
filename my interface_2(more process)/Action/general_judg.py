# coding=utf-8
from ProjectVar.var import *
import ConfigParser
from Util.md5_password import *
from tem_write_read import *
import json
import re
import sys

def generaljudg(ex,row,result_dict):
    cf = ConfigParser.ConfigParser()
    cf.read(check_url)
    section_list=cf.sections() # 获取所有section的列表
    error_str="" # 创建一个记录错误信息的字符串，出现了错误信息就累加到它里面
    result_digit=0
    for isc in section_list:
        if isc==ex.get_value("F"+str(row)).strip():
            option_list = cf.options(isc)  # 取到这个section下的所有option，存在列表中
            for iopt in option_list:  # 遍历option列表
                if cf.get(isc,iopt)[0]<>"!": # 如果配置文件值的第一个字符不为！，则表示这个值是服务器新生成并返回的，判断其对错需要正则
                    option_value_list = cf.get(isc,iopt).split("~")  # 把列表里的每一个元素以“~”为界拆成一个列表，列表里第一个元素是服务器返回的json转成的字典的值的层次结构，第二个元素是匹配值的正则表达式
                    # 如果以option_value_list[0]的层级结构从result_dict取出的值存在于option_list，则可进行比对，否则返回错误信息
                    try:
                        # 如果result_dict+tem_list[0]所组成的层级结构下的值等于用正则从ExcelG列中匹配出来的值，说明服务器返回正确
                        if re.findall(eval(option_value_list[1]),str(eval('result_dict'+ option_value_list[0]))) <> []: # 用option_value_list[1]的正则表达式判断用option_value_list[0]拼接起来的层级结构下的值是否可匹配成功
                            pass
                        else:
                            result_digit=1
                            error_str += str(option_value_list[0])+":"+"未匹配出结果；"
                            #write_tem_error_str(error_str)
                    except:
                        print "第" + str(row - 1) + "条用例对应的配置文件值" + option_value_list[0] + "在返回值中找不到"
                        sys.exit()

                if cf.get(isc,iopt)[0]=="!": # 如果配置文件值的第一个字符为！，则表示这个值是服务器从输入值里取到的，判断其对错需要到Excel中比对
                    option_value_list=cf.get(isc,iopt)[1::].split("~")
                    try:
                        # 这个if是用来兼容用例里输入的json的username本来就为空的情况，由于服务器返回的是unicode格式，所以需要[u'']，它代表username为空
                        if [eval('result_dict'+option_value_list[0])]==[u''] and re.findall(eval(option_value_list[1]),str(ex.get_value("G"+str(row))))==[]:
                            pass
                        # 如果result_dict+tem_list[0]所组成的层级结构下的值等于用正则从ExcelG列中匹配出来的值，说明服务器返回正确
                        elif re.findall(eval(option_value_list[1]),str(ex.get_value("G"+str(row))))<>[]:
                            if eval('result_dict'+option_value_list[0])==re.findall(eval(option_value_list[1]),str(ex.get_value("G"+str(row))))[0]:
                                pass
                            else:
                                result_digit = 1
                                error_str += str(option_value_list[0]) + ":" + "返回值与输入值不符；"
                        else:
                            result_digit = 1
                            error_str += str(option_value_list[0]) + ":" + "返回值与输入值不符；"
                            #write_tem_error_str(error_str)
                    except:
                        print "第" + str(row - 1) + "条用例对应的配置文件值" + option_value_list[0] + "在返回值中找不到"
                        sys.exit()

    if result_digit==0:
        return result_dict
    else:
        #error_str = read_tem_error_str()
        return result_dict,error_str