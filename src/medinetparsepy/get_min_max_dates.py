# get_min_max_dates.py

import pandas


def get_min_max_dates(tidy_schedule: pandas.DataFrame) -> tuple:
    """
    Returns a tuple of the first and last date in a schedule returned by
    load_tidy_schedule(). Meant to be used for creating titles for plots.

    :param tidy_schedule: A schedule as returned by load_tidy_schedule().
    :type tidy_schedule: pandas.DataFrame
    :return: A tuple where the first value is the first date in the schedule
        and the last value is the last date in the schedule.
    :rtype: tuple
    """
    return (tidy_schedule['date'].min().strftime('%Y-%m-%d'),
            tidy_schedule['date'].max().strftime('%Y-%m-%d'))
