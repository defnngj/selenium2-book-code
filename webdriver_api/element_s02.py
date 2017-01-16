'''
Author: 虫师
Date: 2016/11/24
Method:
  *  find_elements_by_xpath("xx")          定位一组xpath定位为xx的元素
  *  find_elements_by_css_selector("xx")   定位一组css定位为xx的元素
'''
from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('./webdriver_api/web_page/checkbox.html')
driver.get(file_path)

# 通过 XPath 找到 type=checkbox 的元素
# checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

# 通过 CSS 找到 type=checkbox 的元素
checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)

# 打印当前页面上 type 为 checkbox 的个数
print(len(checkboxes))

# 把页面上最后 1 个 checkbox 的钩给去掉
driver.find_elements_by_css_selector('input[type=checkbox]').pop().click()

driver.quit()
