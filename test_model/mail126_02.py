from selenium import webdriver

# 登录模块
def login():
    driver.switch_to.frame('x-URS-iframe')
    driver.find_element_by_id("idInput").clear()
    driver.find_element_by_id("idInput").send_keys("username")
    driver.find_element_by_id("pwdInput").clear()
    driver.find_element_by_id("pwdInput").send_keys("password")
    driver.find_element_by_id("loginBtn").click()
    driver.switch_to.default_content()

# 退出模块
def logout():
    driver.find_element_by_link_text("退出").click()
    driver.quit()


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.126.com")

login() # 调用登录模块

# 收信、写信、删除信件等操作
# ……

logout() # 调用退出模块