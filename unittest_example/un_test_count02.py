'''
使用unittest单元测试框架编写单元测试用例。
使用unittest.TestSuite 添加测试用例到测试套件
使用unittest.TextTestRunner 运行测试用例
'''
import unittest
from count import Calculator

# 测试两个整数相加
class TestCount(unittest.TestCase):

    def test_add(self):
        c = Calculator(2,4)
        result = c.add()
        self.assertEqual(result, 6)

    def test_sub(self):
        c = Calculator(8,3)
        result = c.sub()
        self.assertEqual(result, 5)


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestCount('test_add'))
    suite.addTest(TestCount('test_sub'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
