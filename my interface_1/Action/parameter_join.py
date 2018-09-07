#coding=utf-8
from ProjectVar.var import *
import json
from Util.excel import *
from selenium import webdriver

def joinurl(row):
    eins = Excel_r_w(excel_path, u"用例")
    if str(eins.get_value("E"+str(row))).encode("utf-8").strip().lower()=="post":
        thisurl=url+"/"+str(eins.get_value("F"+str(row))).encode("utf-8").strip()+"/"
        return thisurl
    if str(eins.get_value("E"+str(row))).encode("utf-8").strip().lower()=="get":
        thisurl=url+"//"+str(eins.get_value("F"+str(row))).encode("utf-8").strip()+"//"+str(eins.get_value("G"+str(row))).encode("utf-8").strip()+"//"
        return thisurl

def joinjson(row):
    eins = Excel_r_w(excel_path, u"用例")
    thisdict = {}
    for ifg in ["GH","IJ","KL","MN"]:
        thiskey=str(eins.get_value(ifg[0]+str(row)))
        if thiskey=="None":
            continue
        thiskey=thiskey.strip()
        thisvalue=eins.get_value(ifg[1]+str(row).encode("utf-8").strip())
        thisdict[thiskey]=thisvalue
    thisjson=json.dumps(thisdict)
    return thisjson

def joingetkey(row):
    eins = Excel_r_w(excel_path, u"用例")
    thisdict = {}
    thiskey = url+"//"+str(eins.get_value("E"+str(row))).encode("utf-8").strip()
    return thiskey

if __name__=="__main__":
    print type(joinjson(2))
    print joinjson(2)