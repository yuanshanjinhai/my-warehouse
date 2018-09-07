# coding=utf-8
import requests
from Util.write_log_caseresult import *
from ProjectVar.var import *

ex=Excel_r_w(excel_path,u"用例")
wl=Writelog(log_path)

for ir in range(2,int(ex.get_max_row())):
    if ex.get_value("E" + str(ir))==None:
        break
    if ex.get_value("P" + str(ir))=="n":
        continue
    if ex.get_value("E"+str(ir)).encode("utf-8").strip().lower()=="post":
        print joinurl(ir)
        print joinjson(ir)
        result=requests.post(joinurl(ir),data=joinjson(ir))
        if str(result.status_code)<>"200":
            writelogexcel(ex,wl,result.status_code,"99",ir)
            continue
        if str(result.status_code)=="200" and str(result.json()["code"])<>str(ex.get_value("O"+str(ir))).strip():
            writelogexcel(ex,wl,"200",str(result.json()["code"]),ir)
            continue
        if str(result.status_code)=="200" and str(result.json()["code"])==str(ex.get_value("O"+str(ir))).strip():
            writelogexcel(ex,wl,"200",str(result.json()["code"]),ir)
            continue
    if ex.get_value("E"+str(ir)).encode("utf-8").strip().lower()=="get":
        result=requests.get(joingetkey(ir))
        if result.status_code<>"200":
            writelogexcel(ex, wl, result, result.status_code, result.json()["code"], ir)
            continue
        if result.status_code=="200" and result.json()["code"]<>str(ex.get_value("E"+str(ir))).strip():
            writelogexcel(ex, wl, result, result.status_code, result.json()["code"], ir)
            continue
        if result.status_code=="200" and result.json()["code"]==str(ex.get_value("E"+str(ir))).strip():
            writelogexcel(ex, wl, result, result.status_code, result.json()["code"], ir)
            continue
        print result
        print str(result.json())
wl.writelog("-"*200)
wl.closefp()
ex.save_content()

if __name__=="__main__":
    pass