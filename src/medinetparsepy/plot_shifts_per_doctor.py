# plot_shifts_per_doctor.py

import matplotlib.pyplot
import pandas
from medinetparsepy.tally_shifts import tally_shifts
from medinetparsepy.get_min_max_dates import get_min_max_dates


def plot_shifts_per_doctor(tidy_schedule: pandas.DataFrame) -> tuple:
    """
    Plots a bar graph of the total shifts per doctor, stacked by shift type.

    :param tidy_schedule: A data frame containing a schedule, as loaded by
    load_tidy_schedule().
    :type tidy_schedule: pandas.DataFrame
    :return: A tuple with a figure and an axis containing a matplotlib stacked
    bar graph.
    :rtype: tuple
    """
    fig, ax = matplotlib.pyplot.subplots()

    plotting_frame = tally_shifts(tidy_schedule)

    (
        plotting_frame
        .assign(sort_order=plotting_frame.sum(axis=1))
        .sort_values(by='sort_order', ascending=True)
        .drop('sort_order', axis=1)
        .plot(kind='barh', stacked=True, ax=ax)
    )

    dates = get_min_max_dates(tidy_schedule)

    ax.set_xlabel('Shift Count')
    ax.set_ylabel('Doctor')
    ax.set_title(f'Shifts Per Doctor\nBetween {dates[0]} and {dates[1]}')

    return(fig, ax)
