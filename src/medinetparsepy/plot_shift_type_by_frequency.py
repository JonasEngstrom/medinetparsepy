# plot_shift_type_by_frequency.py

import matplotlib.pyplot
import pandas
import medinetparsepy.get_min_max_dates


def plot_shift_type_by_frequency(tidy_schedule: pandas.DataFrame) -> tuple:
    """
    Plots a bar graph of shift type frequencies.

    :param tidy_schedule: A pandas data frame containing a schedule,
    as loaded by load_tidy_schedule().
    :type tidy_schedule: pandas.DataFrame
    :return: A tuple with a figure and an axis containing a matplotlib bar
    graph.
    :rtype: tuple
    """
    return_data = (
        tidy_schedule
        .groupby('shift_type')
        .agg({'shift_type': 'count'})
        .query('shift_type > 0')
        .rename_axis(None)
        .sort_values(by='shift_type', ascending=False)
    )

    dates = medinetparsepy.get_min_max_dates.get_min_max_dates(tidy_schedule)

    fig, ax = matplotlib.pyplot.subplots()

    ax.bar(return_data.index, return_data['shift_type'])
    ax.set_xlabel('Shift Type')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Shift Type by Frequency\nBetween {dates[0]} and {dates[1]}')

    return (fig, ax)
