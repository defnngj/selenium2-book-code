from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from model import myunit, function
from page_obj.login_page import LoginPage
from page_obj.mail_page import MailPage


class loginTest(myunit.MyTest):
    '''社区登录测试'''

    def test_login_user_pawd_null(self):
        '''用户名、密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action("","")
        sleep(2)
        self.assertEqual(po.login_error_hint(), '请输入帐号')

    def test_login_pawd_null(self):
        '''密码为空登录'''
        po = LoginPage(self.driver)
        po.open()
        po.login_action("testaaa","")
        sleep(2)
        self.assertEqual(po.login_error_hint(), '请输入密码')

    def test_login_user_pawd_error(self):
        '''用户名、密码为错误'''
        po = LoginPage(self.driver)
        po.open()
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "test" + character
        po.login_action(username,"@#$%")
        sleep(2)
        self.assertEqual(po.login_error_hint(), '帐号或密码错误')

    def test_login_success(self):
        '''用户名、密码正确，登录成功'''
        po = LoginPage(self.driver)
        po.open()
        user = "username"
        po.login_action(user,"password")
        sleep(2)
        po2 = MailPage(self.driver)
        self.assertEqual(po2.login_success_user(), user+"@163.com")


if __name__ == '__main__':
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(loginTest("test_login_user_pawd_null"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
