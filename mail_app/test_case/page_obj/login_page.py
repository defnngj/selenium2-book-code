from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from .base import Base


# 页面对象（PO) 登录页面
class LoginPage(Base):

    url = '/'

    login_iframe_loc = "x-URS-iframe"
    login_username_text_loc = (By.NAME,"email")
    login_password_text_loc = (By.NAME,"password")
    login_button_loc = (By.ID, "dologin")
    login_erro_hint_loc = (By.CLASS_NAME, "ferrorhead")

    #把每一个元素封装成一下方法
    def login_iframe(self):
        self.iframe(self.login_iframe_loc)

    def login_iframe_out(self):
        self.iframe_out()

    def login_username(self,text):
        self.find_element(*self.login_username_text_loc).send_keys(text)

    def login_password(self,text):
        self.find_element(*self.login_password_text_loc).send_keys(text)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def login_error_hint(self):
        self.login_iframe()
        return self.find_element(*self.login_erro_hint_loc).text
        self.login_iframe_out()

    def login_action(self,username,password):
        self.login_iframe()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        self.login_iframe_out()
