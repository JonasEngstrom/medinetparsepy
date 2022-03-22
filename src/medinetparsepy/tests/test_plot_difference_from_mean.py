# test_plot_difference_from_mean.py

import unittest
import matplotlib
from medinetparsepy.load_example_schedule import load_example_schedule
from medinetparsepy.plot_difference_from_mean import plot_difference_from_mean

class TestTallyShifts(unittest.TestCase):

    def setUp(self):
        self.example_schedule = load_example_schedule()

    def tearDown(self):
        del self.example_schedule

    def test_plot_difference_from_mean(self):
        test_fig, test_ax = plot_difference_from_mean(self.example_schedule)
        self.assertIsInstance(test_fig,
                              matplotlib.figure.Figure)
        self.assertEqual(test_ax.get_ylabel(),
                         'Doctor')
        self.assertEqual(test_ax.get_xlabel(),
                         'Difference in Number of Shifts from the Mean of 61.89 Shifts\n')
        self.assertEqual(test_ax.title._text,
                         'Difference from Mean Number of Shifts\nBetween 2022-02-28 and 2022-05-08')


if __name__ == '__main__':
    unittest.main()
