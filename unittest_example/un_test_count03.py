'''
常用断言方法：
assertEqual()  判断相等
assertNotEqual()  判断不相等
assertIn()  判断包涵
assertNotIn()  判断不包涵
assertTrue()   判断为True
assertFalse()  判断为False
'''
import unittest
from count import Calculator, is_prime

#
class TestEqual(unittest.TestCase):

    def test_mul(self):
        c = Calculator(2,4)
        result = c.mul()
        self.assertEqual(result, 8)

    def test_div(self):
        c = Calculator(8,3)
        result = c.div()
        self.assertNotEqual(result, 999)

class TestIn(unittest.TestCase):

    def test_in(self):
        a = "hello"
        b = "hello world"
        self.assertIn(a, b)

    def test_not_in(self):
        a = "helloooo"
        b = "hello world"
        self.assertNotIn(a, b)

class TestTrue(unittest.TestCase):

    def test_true(self):
        result = is_prime(7)
        self.assertTrue(result)

    def test_false(self):
        result = is_prime(8)
        self.assertFalse(result)


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestEqual('test_mul'))
    suite.addTest(TestEqual('test_div'))
    suite.addTest(TestIn('test_in'))
    suite.addTest(TestIn('test_not_in'))
    suite.addTest(TestTrue("test_true"))
    suite.addTest(TestTrue("test_false"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
