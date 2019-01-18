# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

keyword_list = [
    'a或我或123',
    '\0',
    '<div></div> &nbsp;',
    "<script>alert('abc')</script>",
    'https://www.baidu.com',
    'a' * 101,
    '',
    '飞船',
    '大衣',
    '.*',
    '大        衣',
    '        大衣',
    '大衣        ',
    '大衣'
]

browser = webdriver.Chrome()

def test():
    browser.get('https://you.163.com')
    wait = WebDriverWait(browser, 10)
    
    for keyword in keyword_list:
        search = wait.until(EC.presence_of_element_located((By.NAME, "searchInput")))
        search.send_keys(keyword)
        search.send_keys(Keys.ENTER)

        time.sleep(1)
        browser.back()

if __name__ == "__main__":
    test()
    browser.close()



