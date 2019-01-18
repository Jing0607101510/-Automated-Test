# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

def test():
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get("https://you.163.com")
    input = wait.until(EC.presence_of_element_located((By.NAME, "searchInput")))
    search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#j-yx-cp-m-top > div.yx-cp-m-funcTab.j-yx-cp-m-funcTab > div > div.yx-cp-m-search.yx-cp-zIndex3 > div.yx-cp-searchButton")))
   # search = browser.find_element_by_class_name('yx-cp-searchButton')
    input.send_keys("大衣")
    search.click()
    time.sleep(2)
    browser.close()

if __name__ == "__main__":
    test()
    
    