'''
unittest + selenium 用例
'''
from selenium import webdriver
import unittest, time


class BaiduIde(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def test_baidu_ide(self):
        driver = self.driver
        driver.get(self.base_url)
        search_text = driver.find_element_by_id("kw")
        search_text.clear()
        search_text.send_keys("selenium ide")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertEqual("selenium ide__百度搜索", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
