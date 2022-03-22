# test_plot_shifts_per_doctor.py

import unittest
import matplotlib
from medinetparsepy.load_example_schedule import load_example_schedule
from medinetparsepy.plot_shifts_per_doctor import plot_shifts_per_doctor

class TestTallyShifts(unittest.TestCase):

    def setUp(self):
        self.example_schedule = load_example_schedule()

    def tearDown(self):
        del self.example_schedule

    def test_plot_shifts_per_doctor(self):
        test_fig, test_ax = plot_shifts_per_doctor(self.example_schedule)
        self.assertIsInstance(test_fig,
                              matplotlib.figure.Figure)
        self.assertEqual(test_ax.get_ylabel(),
                         'Doctor')
        self.assertEqual(test_ax.get_xlabel(),
                         'Shift Count')
        self.assertEqual(test_ax.title._text,
                         'Shifts Per Doctor\nBetween 2022-02-28 and 2022-05-08')


if __name__ == '__main__':
    unittest.main()
