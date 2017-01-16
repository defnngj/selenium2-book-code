'''
Author: 虫师
Date: 2016/11/22
Method:
  *  switch_to.window()  切换窗口
  *  current_window_handle 获得当前窗口的句柄
  *  window_handles：返回所有窗口的句柄到当前会话
'''
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# 获得百度搜索窗口句柄
sreach_windows = driver.current_window_handle
driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to.window(handle)
        print('now register window!')
        driver.find_element_by_name("userName").send_keys('username')
        driver.find_element_by_name('phone').send_keys('phone')
        time.sleep(2)
        # ……
        driver.close()

# 回到搜索窗口
driver.switch_to.window(sreach_windows)
print('now sreach window!')
driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(2)

driver.quit()
