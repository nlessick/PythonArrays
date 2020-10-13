import unittest
import sort_and_search_array.array_assignment as array_assignment
from sort_and_search_array.array_assignment import search_array


class MyTestCase(unittest.TestCase):
    def test_something(self):
        data = [5,4,9]
        result = search_array(data)
        self.assertEqual(result,1)


if __name__ == '__main__':
    unittest.main()
