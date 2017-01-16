'''
Author: 虫师
Date: 2016/12/1
Method:
  * get_cookies() 获得所有 cookie 信息。
  * get_cookie(name) 返回字典的 key 为“ name”的 cookie 信息。
  * add_cookie(cookie_dict) 添加 cookie。“ cookie_dict”指字典对象，必须有name和value 值。
  * delete_cookie(name,optionsString)  删除 cookie 信息。“name”是要删除的 cookie 的名称，
                                       “optionsString”是该 cookie 的选项，目前支持的选项包括“路径”，“域”。
  * delete_all_cookies() 删除所有 cookie 信息。
'''
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# 向 cookie 的 name 和 value 中添加会话信息
driver.add_cookie({'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'})

# 遍历 cookies 中的 name 和 value 信息并打印，当然还有上面添加的信息
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'], cookie['value']))

driver.quit()
