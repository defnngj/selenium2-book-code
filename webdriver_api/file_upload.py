'''
Author: 虫师
Date: 2016/11/28
Method: 
  * send_keys() 指定文件上传路径。
'''
from selenium import webdriver
import os
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./web_page/upfile.html')
driver.get(file_path)

# 定位上传按钮，添加本地文件
driver.find_element_by_name("file").send_keys('D:\\upload_file.txt')
#driver.quit()