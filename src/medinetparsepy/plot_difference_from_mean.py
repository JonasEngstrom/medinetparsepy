# plot_difference_from_mean.py

import matplotlib.pyplot
import pandas
import medinetparsepy.get_min_max_dates


def plot_difference_from_mean(tidy_schedule: pandas.DataFrame) -> tuple:
    """
    Plots a bar graph of the difference between the number of shifts that a
    doctor is scheduled and the mean for all the doctors in the schedule.

    :param tidy_schedule: A dataframe containing a schedule, as loaded by
    load_tidy_schedule().
    :type tidy_schedule: pandas.DataFrame
    :return: A tuple with a figure and an axis containing a matplotlib bar
    graph.
    :rtype: tuple
    """
    shift_counts = (
        tidy_schedule
        .groupby('doctor_name')
        .agg({'shift_type': 'count'})
    )

    shift_mean = (
        shift_counts
        .mean()
    )

    dates = medinetparsepy.get_min_max_dates.get_min_max_dates(tidy_schedule)

    fig, ax = matplotlib.pyplot.subplots()

    (
        shift_counts
        .assign(difference_from_mean=
                        shift_counts['shift_type']-shift_mean['shift_type'])
        .sort_values(by='difference_from_mean')
        .drop('shift_type', axis=1)
        .plot(kind='barh', legend=False, ax=ax)
    )

    ax.set_xlabel(f'Difference in Number of Shifts from the Mean '
                  f'of {shift_mean["shift_type"]:.2f} Shifts\n')
                  #f'Numbers above Bars Show Absolute Number of Shifts')
    ax.set_ylabel('Doctor')
    ax.set_title(f'Difference from Mean Number of Shifts\n'
                 f'Between {dates[0]} and {dates[1]}')
    #ax.bar_label(ax.containers[1])

    return(fig, ax)
