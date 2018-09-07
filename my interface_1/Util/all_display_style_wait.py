#coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 判断下拉框的选项是否可选，可选则返回True，否则返回False
# 调用时，首先要先选中下拉框的某个选项，再调用此函数
# tuple1为一个元组，里面包含了两个值，一个是查找方式，通常是By.ID，一个是需要判断的下拉选项的id
# 元组中如果第一个元素是By.NAME，那么第二个元素则为需要怕暖的下拉选项的name
# True代表可用,driver为浏览器的实例对象,ws代表等待的秒数，es代表在ws时间段内每隔多少毫秒尝试选择一次
# 例：isselected((By.ID, "orange"),True,10,0.2)
# 代表某下拉选项的id为orange，在10秒内，每隔0.2秒（200毫秒）尝试选择一次，直到选择成功，成功后代码向后执行
def isselected(tuple1,True,driver,ws,es):
    wait = WebDriverWait(driver,ws,es)
    return wait.until(EC.element_located_selection_state_to_be(tuple1,True))


# 判断页面上某元素是否可见和可被点击（任何元素都可以被点击，不仅限于输入框）,可被点击返回该元素对象，否则返回False
# driver为浏览器实例化对象，ws为等待的秒数，es为ws时间段内每隔多少毫秒查看一次该元素是否可见和可被点击
# vcxpath为查找该元素所使用的xpath语句
# 例：visible_clicked(driver,10,0.2,"//input[@id='kw']")
def visible_clicked(driver,ws,es,vcxpath):
    wait = WebDriverWait(driver,ws,es)
    return wait.until(EC.element_to_be_clickable((By.XPATH,vcxpath)))


# 判断frame是否可用，如可用，则返回True并切入frame，不可用则返回False
# driver为浏览器的实例化对象，ws为等待的秒数，es为ws时间段内每隔多少毫秒判断一次frame是否可用
# tuple有两个值，一个是查找方式，可以By.ID，也可以 By.XPATH，另一个是该frame的id
# tuple的第一个值如果是By.NAME，那么第二个值就是该frame的NAME
# 例1：frame_isusabled(driver,10,0.2,(By.ID, "x-URS-iframe"))
# 例2：frame_isusabled(driver, 10, 0.2,(By.XPATH,"//iframe[@id='x-URS-iframe']"))
def frame_isusabled(driver,ws,es,tuple1):
    wait = WebDriverWait(driver,ws,es)
    return wait.until(EC.frame_to_be_available_and_switch_to_it(tuple1))


# 判断某元素是否出现，如在规定的时间内出现，则返回True，代码继续往下执行，否则返回False
# 可通过try except捕获异常的方式来设置如果被等待元素未出现时如何处理
# driver为浏览器实例化对象，ws为等待的秒数，es为ws时间段内每隔多少秒（通常为0.2，即200毫秒）查看一次该元素是否出现
def isvisible(driver,ws,es,thisxpath):
    wait=WebDriverWait(driver,ws,es)
    thiselement = driver.find_element("xpath", thisxpath)
    vc_thiselement=wait.until(EC.visibility_of(thiselement))
    if vc_thiselement==thiselement:
        return True
    else:
        return False


# 判断元素（标签）中是否有某文本，如<a href="http://news.baidu.com" name="tj_trnews">新闻</a>，a标签中的文本“新闻”
# tuple1是一个元组，其中有两个值，第一个通常是By.XPATH，即通过xpath定位某元素，当然也可以通过其他方式定位，如By.TAG_NAME
# tuple1的第二个元素是xpath语句，如果第一个参数是By.TAG_NAME，那么第二个元素就是TAG_NAME
# driver是浏览器实例化对象，ws是等待的秒数，es是在ws时间段内每隔多少毫秒查看一次该元素的text是否存在,text是欲等待的文本
# 包含返回True，否则返回False
# 例：istext((By.XPATH,"//a[@name='tj_trnews']"),driver,10,0.2,u"新闻")
def istext(tuple1,driver,ws,es,text):
    wait = WebDriverWait(driver, ws, es)
    return wait.until(EC.text_to_be_present_in_element(tuple1,text))


# 判断页面上的title标签内容是否包含partial_title，只需要部分符合即可，只要包含，则证明已跳转至该页面
# 包含返回True，否则返回False
#driver为浏览器的实例化对象，ws是等待的秒数，es是在ws时间段内每隔多少毫秒判断一次title是否部分符合
def title_contains(driver, ws, es,partial_title):
    wait = WebDriverWait(driver, ws, es)
    return wait.until(EC.title_contains(partial_title))


#  判断页面title标签是否与title_value符合，如符合，则证明已跳转至该页面
#  常用于上传文件，点击上传按钮后，通过此法查看是否跳转至上传成功的页面
# driver为浏览器的实例化对象，ws是等待的秒数，es是在ws时间段内每隔多少毫秒判断一次title是否符合
# 如title出现则返回True，未出现则返回False
# 例：istitle(driver,10,0.2,u"搜狐")
def istitle(driver,ws,es,title_value):
    wait = WebDriverWait(driver,ws,es)
    return wait.until(EC.title_is(title_value))

if __name__=="__main__":
    from selenium import webdriver
    import time
    driver=webdriver.Firefox(executable_path=r"D:\Program Files\webdriver\geckodriver.exe")
    driver.get("https://www.126.com/")
    time.sleep(5)
    frame = driver.find_element_by_xpath("//iframe[@id='x-URS-iframe']")
    driver.switch_to_frame(frame)
    username = driver.find_element("xpath", '//input[@data-placeholder="邮箱帐号或手机号" and @tabindex="1"]')
    username.clear()
    username.send_keys('anyg1314')
    ps = driver.find_element("xpath", "//input[@data-placeholder='密码' and @name='password']")
    ps.send_keys('****************')
    driver.find_element("xpath", '//a[@id="dologin"]').click()
    driver.switch_to.default_content()
    time.sleep(4)
    if isvisible(driver, 10, 0.2, "//span[.='写 信']")==1:
        print "----------------"
