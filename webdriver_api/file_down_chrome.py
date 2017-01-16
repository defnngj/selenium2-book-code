'''
Author: 虫师
Date: 2016/12/1
Method:
  * download.default_directory 指定文件下载路径。
  * profile.default_content_settings.popups 设置0，禁止下载时弹出窗口。
'''
from selenium import webdriver
import os

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': os.getcwd()
         }
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get("http://pypi.Python.org/pypi/selenium")
driver.find_element_by_partial_link_text("selenium-3.0.2.tar.gz").click()
