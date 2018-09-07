# coding=utf-8
from ProjectVar.var import *
from Util.excel import *

def wirte_None(ex,row):
    ex.write_content("J" + str(row), "")
    ex.write_content("K" + str(row), "")
    ex.write_content("L" + str(row), "")

def write_cr(ex,row,result):
    if isinstance(result,int)==1:
        ex.write_content("J"+str(row),str(result))
        ex.write_content("K" + str(row), str(result))
        ex.write_content("L" + str(row), "不通过")
    elif isinstance(result,tuple)==1:
        ex.write_content("J" + str(row), str(result[0]))
        ex.write_content("K" + str(row),result[1])
        ex.write_content("L" + str(row), "不通过")
    elif result["code"]<>ex.get_value("H" + str(row)).strip():
        ex.write_content("J" + str(row), str(result))
        ex.write_content("K" + str(row), result["code"])
        ex.write_content("L" + str(row), "不通过")
    else:
        ex.write_content("J" + str(row), str(result))
        ex.write_content("L" + str(row), "通过")
        ex.write_content("K" + str(row), "")
