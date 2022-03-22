# test_plot_shift_type_by_frequency.py

import unittest
import matplotlib
from medinetparsepy.load_example_schedule import load_example_schedule
from medinetparsepy.plot_shift_type_by_frequency import plot_shift_type_by_frequency

class TestTallyShifts(unittest.TestCase):

    def setUp(self):
        self.example_schedule = load_example_schedule()

    def tearDown(self):
        del self.example_schedule

    def test_plot_shift_type_by_frequency(self):
        test_fig, test_ax = plot_shift_type_by_frequency(self.example_schedule)
        self.assertIsInstance(test_fig,
                              matplotlib.figure.Figure)
        self.assertEqual(test_ax.get_ylabel(),
                         'Frequency')
        self.assertEqual(test_ax.get_xlabel(),
                         'Shift Type')
        self.assertEqual(test_ax.title._text,
                         'Shift Type by Frequency\nBetween 2022-02-28 and 2022-05-08')


if __name__ == '__main__':
    unittest.main()
