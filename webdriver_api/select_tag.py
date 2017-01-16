'''
Author: 虫师
Date: 2016/12/2
Method:
  * Select  操作select标签的下拉框。
  * select_by_value  选择vlaue属性。
'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./webdriver_api/web_page/select_tag.html')
driver.get(file_path)

sel = driver.find_element_by_xpath("//select[@id='status']")
Select(sel).select_by_value('0')  #未审核
Select(sel).select_by_value('1')  #初审通过
Select(sel).select_by_value('2')  #复审通过
Select(sel).select_by_value('3')  #审核不通过
