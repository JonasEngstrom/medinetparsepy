# load_example_schedule.py

from importlib.resources import open_text
import pandas

def load_example_schedule():
    """
    An edited example of a ten week schedule for thirty-five doctors
    imported from Medinet using the load_tidy_schedule() function. The names
    have been randomly generated using the swedishname R package. The
    schedule is meant to be used in examples, documentation, and unit tests
    in the package, as well as for experimentation in generating juseful
    visualizations and reports using the package, in case Medinet data is
    not available.

    Contains the following fields:
        date        2,166 non-null Timestamp
        doctor_name 2,166 non-null str
        shift_type  2,166 non-null str

    :return: A 2,166 row, 3 column tidy schedule.
    :rtype: pandas.DataFrame
    """
    with open_text('medinetparsepy', 'example_schedule.json') as file:
        example_schedule = pandas.read_json(file)

    return example_schedule
