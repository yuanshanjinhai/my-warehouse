# coding=utf-8
from Action.action import *
from ProjectVar.var import *
from Util.CheckCsaeIsNone import *
from Util.excel import *
from write_th.write_caseresult import *
from write_th.write_runlog import *
from write_th.write_userlog import *
from Action.action import *
import re
import sys

clear_file()

ex=Excel_r_w(excel_path,u"用例") # 读写Excel类的实例化

checkcin=CheckCIN(ex) # 判断用例是否有为空项，如果有，提示为空项并退出系统
if checkcin.check()==1:
    sys.exit()

fprl=open(runlog_path,"a") # 读写运行日志的句柄
fpul=open(userlog_path,"a") # 读写uder日志的句柄


for ir in range(2,ex.get_max_row()+1): # 遍历Excel文档中用例标签里的所有有效行，从第二行开始
    if str(ex.get_value("I" + str(ir))).strip() == "n":
        wirte_None(ex,ir)
        continue
    rd = return_dict(ex,ir)  # 接收服务器返回值并判断其正确性的类的实例化
    wrl = write_runlog(fprl,ex,ir) # 写运行日志的类的实例化
    wul = write_userlog(fpul,ex,ir) # 写user日志的类的实例化

    result=rd.judge() # 获取服务器的返回值（已转化为字典）
    wrl.write_rl(result) # 写入运行日志
    wul.write_ul(result) # 写入user日志
    write_cr(ex,ir,result) # 在Excel写入结果

ex.save_content()
fprl.close()
fpul.close()