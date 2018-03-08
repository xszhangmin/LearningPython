import unittest

from base.BubbleSort import bubbleSort


class TestBubbleSort(unittest.TestCase):

    def testSort(self):
        nums = [1, 3, 2, 5, 4]
        nums = bubbleSort(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
