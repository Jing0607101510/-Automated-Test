# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup
import time
text_list = [
    "script>alert('xss')</script>",
    '<object type=text/html data="javascript:alert(([code]);"></object>',
    'select count(*) from admin',
    '$sql="select * from user where password like "%$pwd%" order by password";'
]

def test():
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get('https://you.163.com')  
    for text in text_list:
        search = wait.until(EC.presence_of_element_located((By.NAME, "searchInput")))
        search.send_keys(text)
        search.send_keys(Keys.ENTER)
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        res = soup.find('span', {'data-reactid':'.2.0.0.0.0.0.0'})
        print("预期效果：无内容显示", end=" ")
        if res:
            print("实际效果：无内容显示")
        else:
            print("实际效果：脚本注入成功")
        browser.back()
    
    time.sleep(5)
    browser.close()

if __name__ == "__main__":
    time.sleep(5)
    test()
    

        

    