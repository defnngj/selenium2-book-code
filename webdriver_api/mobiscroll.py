from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

driver = webdriver.Chrome()

driver.get("http://www.jq22.com/yanshi4976")
sleep(5)
driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

dragger = driver.find_element_by_class_name("dwwo")
action = ActionChains(driver)
action.click_and_hold(dragger).perform()  #鼠标左键按下不放

for index in range(18):
    try:
        action.move_by_offset(0, 2).perform() #垂直移动鼠标
    except UnexpectedAlertPresentException:
        break
    action.reset_actions()
    sleep(0.1)  #等待停顿时间
sleep(2)

action.release().perform() # 释放鼠标

driver.find_element_by_class_name("dwb").click()




