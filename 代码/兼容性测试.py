#-*- coding:utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread  #导入python多线程模块
def test(browser,url):
    driver = None
    # 你可以自定义这里，添加更多浏览器支持进来
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    elif browser == 'Chrome':
        driver = webdriver.Chrome()
    if driver == None:
        exit()
    print("开始")
    try:
        driver.get(url)
        input = driver.find_element_by_name('searchInput')
        input.clear()
        input.send_keys('大衣')
        input.send_keys(Keys.ENTER)
        time.sleep(5)
        #关闭浏览器
        driver.quit()
    except:
        print("失败")


if __name__=="__main__":
    #浏览器好额首页url
    data = {
        'ie':'https://you.163.com',
        'Firefox':'https://you.163.com',
        'Chrome':'https://you.163.com'
    }
    #构建线程
    thresds = []
    for b,url in data.items():
        t = Thread(target=test,args=(b,url))
        thresds.append(t)
    #启动所有线程
    for s in thresds:
        s.start()