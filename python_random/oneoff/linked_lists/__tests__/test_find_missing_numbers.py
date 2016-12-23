import unittest
from find_missing_numbers import find_missing_numbers 

class Random(unittest.TestCase):
    def test_find_one_missing_number(self):
        numbers = [1,2,3,5,6,6]
        missing = [4]
        self.assertEqual(find_missing_numbers(numbers),
                         missing)
    
    def test_find_multi_missing(self):
        numbers = [1, 1, 4, 4, 5]
        missing = [2,3]
        self.assertEqual(find_missing_numbers(numbers),
                         missing)

    def test_find_none_missing(self):
        nums = [x for x in range(1,6)]
        missing = []
        self.assertEqual(find_missing_numbers(nums),
                         missing)

if __name__ == '__main__':
    unittest.main()
