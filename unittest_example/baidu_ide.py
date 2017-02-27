'''
通过selenium IDE 录制并导出的测试用例。
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class BaiduIde(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_baidu_ide(self):
        driver = self.driver
        # 百度搜索
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("#kw").clear()
        driver.find_element_by_css_selector("#kw").send_keys("selenium ide")
        driver.find_element_by_id("su").click()
        try: self.assertEqual(u"selenium ide_百度搜索ssssss", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("python")
        driver.find_element_by_id("su").click()
        self.assertEqual(u"python__百度搜索", driver.title)

        for i in range(60):
            try:
                if self.is_element_present(By.ID, "content_left"):
                    break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
