'''
Author: 虫师
Date: 2016/12/1
Method:
  * get_screenshot_as_file() 截取窗口图片。
'''
from selenium import webdriver
from time import sleep
import os

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
sleep(2)

# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file(os.path.abspath('./webdriver_api/web_page/baidu_page.jpg'))
driver.quit()
