import unittest

from base.A import A
from base.B import B


class TestIns(unittest.TestCase):
    def setUp(self):
        print('测试开始执行')

    def test_ins(self):
        print('测试equals方法')
        self.assertTrue(isinstance(A(), A))
        self.assertTrue(type(A()) == A)
        self.assertTrue(isinstance(B(), A))
        self.assertFalse(type(B()) == A)


if __name__ == '__main__':
    unittest.main()
