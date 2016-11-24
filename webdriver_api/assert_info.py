'''
Author: 虫师
Date: 2016/11/24
Method: 
  *  title         获取当前页面title
  *  current_url   获取当前页面URL
  *  text          获得文本信息
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.126.com")

print('Before login================')
# 打印当前页面 title
title = driver.title
print(title)

# 打印当前页面 URL
now_url = driver.current_url
print(now_url)

# 执行邮箱登录
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("username")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("password")
driver.find_element_by_id("loginBtn").click()
driver.switch_to.default_content()
time.sleep(5)

print('After login================')
# 再次打印当前页面 title
title = driver.title
print(title)

# 打印当前页面 URL
now_url = driver.current_url
print(now_url)

# 获得登录的用户名
user = driver.find_element_by_id('spnUid').text
print(user)

driver.quit()