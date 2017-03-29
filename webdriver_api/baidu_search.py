'''
Author: 虫师
Date: 2016/11/22
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium3")
driver.find_element_by_id("su").click()

driver.quit()