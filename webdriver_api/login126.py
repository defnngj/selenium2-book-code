'''
Author: 虫师
Date: 2016/11/22
Method: 
  *  clear()   清除输入框的内容
  *  send_keys()   输入框输入
  *  click()   点击任何可点击的元素（按钮、链接、复选框等）
  *  switch_to.frame()  进入表单
  *  switch_to.default_content()  退出表单至根页面
'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.126.com")

driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("username")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("password")
driver.find_element_by_id("loginBtn").click()
driver.switch_to.default_content()

driver.quit()