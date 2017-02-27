'''
discover() 匹配某目录下的所有测试用例。
'''
import unittest


suit = unittest.defaultTestLoader.discover("./test_case", pattern='test_*.py')


if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suit)
