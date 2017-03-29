'''
Author: 虫师
Date: 2016/11/24
Method:
  *
'''
from selenium import webdriver
from time import ctime, sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

print(ctime())
for i in range(10):
    try:
        el = driver.find_element_by_id("kw22")
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
print(ctime())

driver.close()
