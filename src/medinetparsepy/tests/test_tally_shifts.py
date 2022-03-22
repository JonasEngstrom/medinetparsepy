# test_tally_shifts.py

import unittest
import pandas
from medinetparsepy.load_example_schedule import load_example_schedule
from medinetparsepy.tally_shifts import tally_shifts

class TestTallyShifts(unittest.TestCase):

    def setUp(self):
        self.example_schedule = load_example_schedule()

    def tearDown(self):
        del self.example_schedule

    def test_tally_shifts(self):
        test_table = tally_shifts(self.example_schedule)
        self.assertIsInstance(test_table,
                              pandas.core.frame.DataFrame)
        self.assertEqual(test_table.shape,
                         (35, 26))


if __name__ == '__main__':
    unittest.main()
