# coding=utf-8
import os
from Util.excel import *

excel_path=os.path.dirname(os.path.dirname(__file__))+"\\keyword_data\\kd.xlsx"

runlog_path=os.path.dirname(os.path.dirname(__file__))+"\\run_log\\run.log"

userlog_path=os.path.dirname(os.path.dirname(__file__))+"\\run_log\\user.log"

url="http://39.106.41.11:8080"

check_url=os.path.dirname(os.path.dirname(__file__))+"\\config\\check.ini"

tem_store_path=os.path.dirname(os.path.dirname(__file__))+"\\config\\tem_store_read.conf"

tem_login_info_path=os.path.dirname(os.path.dirname(__file__))+"\\config\\tem_login_info.conf"
