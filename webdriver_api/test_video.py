'''
Author: 虫师
Date: 2016/12/1
Method:
  * execute_script() 调用JavaScript操作Web。
'''
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("http://videojs.com/")
video = driver.find_element_by_id("home_video")

# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

# 播放视频
print("start")
driver.execute_script("return arguments[0].play()", video)

# 播放 15 秒钟
sleep(15)

# 暂停视频
print("stop")
driver.execute_script("arguments[0].pause()", video)
driver.quit()
