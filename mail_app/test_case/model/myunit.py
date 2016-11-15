from time import sleep
from .function import insert_img
import unittest
from .driver import browser


class MyTest(unittest.TestCase):

    global case_count
    case_count = 0

    global image_count
    image_count = 0

    # 计算测试用例的个数，用于显示在测试报告中
    def case_id(self):
        global case_count
        case_count += 1
        if case_count <= 9:
            count = "00" + str(case_count)
        elif case_count <= 99:
            count = "0" + str(case_count)
        else:
            count = str(case_count)
        return count

    # 测试完成，生成截图文件的名称
    def image_id(self):
        global image_count
        image_count += 1
        if image_count <= 9:
            count = "00" + str(image_count)
        elif image_count <= 99:
            count = "0" + str(image_count)
        else:
            count = str(image_count)
        return count

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("case " + str(self.case_id()))

    def tearDown(self):
        img_id = self.image_id()
        file_name = img_id + ".jpg"
        insert_img(self.driver, file_name)
        print("image/" + file_name)
        self.driver.quit()


if __name__ == '__main__':

    class Test(MyTest):

        def test_case(self):
            self.driver.get("http://www.baidu.com")
            self.driver.find_element_by_id("kw").send_keys("unittest")
            self.driver.find_element_by_id("su").click()
            sleep(2)

    unittest.main()
