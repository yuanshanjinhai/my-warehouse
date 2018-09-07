# coding=utf-8
from ProjectVar.var import tem_store_path

def getBlogsContenturl():
    with open(tem_store_path,"r") as fp:
        tem_list=fp.readlines()
        articleIds=""
        for it in tem_list:
            articleIds = articleIds + it.split("||")[-1].strip()+","
        return articleIds[0:-1]

if __name__ == '__main__':
    value_str=getBlogsContenturl()
    print value_str