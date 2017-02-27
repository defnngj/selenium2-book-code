'''
使用unittest单元测试框架编写单元测试用例。
'''
import unittest
from count import Calculator

# 测试两个整数相加
class TestCount(unittest.TestCase):

    def test_add(self):
        c = Calculator(2,4)
        result = c.add()
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
