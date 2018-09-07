# coding=utf-8
from ProjectVar.var import tem_store_path

def getBlogContenturl():
    with open(tem_store_path,"r") as fp:
        tem_list=fp.readlines()
        value_articleId=tem_list[-1].split("||")[-1]
        return value_articleId

if __name__ == '__main__':
    value_str=getBlogContenturl()
    print value_str
    print type(value_str)