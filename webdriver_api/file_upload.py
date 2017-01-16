'''
Author: 虫师
Date: 2016/11/28
Method:
  * send_keys() 指定文件上传路径。
'''
from selenium import webdriver
import os, time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./webdriver_api/web_page/upfile.html')
driver.get(file_path)

time.sleep(2)
# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys(os.path.abspath('./webdriver_api/web_page/upload_file.txt'))
time.sleep(5)
driver.quit()
