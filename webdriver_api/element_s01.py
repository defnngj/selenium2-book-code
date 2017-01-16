'''
Author: 虫师
Date: 2016/11/24
Method:
  *  find_elements_by_tag_name("xx")   定位一组标签名为xx的元素
'''
from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./webdriver_api/web_page/checkbox.html')
driver.get(file_path)

# 选择页面上所有的 tag name 为 input 的元素
inputs = driver.find_elements_by_tag_name('input')
# 然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
for i in inputs:
    if i.get_attribute('type') == 'checkbox':
        i.click()

time.sleep(1)
driver.quit()
