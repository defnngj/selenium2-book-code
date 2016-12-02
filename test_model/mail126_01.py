from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.126.com")

# 登录
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("username")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("password")
driver.find_element_by_id("loginBtn").click()
driver.switch_to.default_content()

# 收信、写信、删除信件等操作
# ……

# 退出
driver.find_element_by_link_text("退出").click()
driver.quit()