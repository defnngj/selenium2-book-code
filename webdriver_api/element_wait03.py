'''
Author: 虫师
Date: 2016/11/24
Method:
  *  implicitly_wait() 隐式等待
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import ctime

driver = webdriver.Chrome()

# 设置隐式等待为 10 秒
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())

driver.quit()
