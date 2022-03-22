# test_get_min_max_dates.py

import unittest
from medinetparsepy.load_example_schedule import load_example_schedule
from medinetparsepy.get_min_max_dates import get_min_max_dates

class TestTallyShifts(unittest.TestCase):

    def setUp(self):
        self.example_schedule = load_example_schedule()

    def tearDown(self):
        del self.example_schedule

    def test_get_min_max_dates(self):
        test_table = get_min_max_dates(self.example_schedule)
        self.assertEqual(len(test_table), 2)
        self.assertEqual(test_table[0], '2022-02-28')
        self.assertEqual(test_table[1], '2022-05-08')


if __name__ == '__main__':
    unittest.main()
