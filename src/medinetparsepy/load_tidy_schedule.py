# load_tidy_schedule.py

import bs4
import pandas
import numpy


def load_tidy_schedule(file_path: str) -> pandas.DataFrame:
    """
    Loads a HTML file from Medinet and returns the schedule as a tidy Pandas
    DataFrame.

    :param file_path: String containing the path to the HTML file.
    :type file_path: str
    :return: A tidy data frame conteining the schedule data for analysis.
    :rtype: pandas.DataFrame
    """
    with open(file_path, encoding='latin-1') as file_object:
        file_data = bs4.BeautifulSoup(file_object, 'html.parser')

    day_ids = pandas.DataFrame(
        [day.attrs['id'] for day in file_data.select('[id^=day]')],
        columns=['day_id'])

    shift_types = []

    for day in file_data.select('[id^=day] table'):
        shift_types.append([shift.text for shift in day.find_all('td')])

    shift_types = pandas.DataFrame(shift_types)

    shifts_by_days = (
        day_ids
        .join(shift_types)
        .assign(date=day_ids['day_id'].str.extract('(\d{4}-\d{2}-\d{2})',
                                                   expand=True))
        .assign(doctor_id=day_ids['day_id'].str.extract('day-(\d{1,3})',
                                                        expand=True))
        .melt(id_vars=['date', 'doctor_id', 'day_id'])
        .drop(['variable', 'day_id'], axis=1)
        .dropna()
        .rename(columns={'value': 'shift_type'})
    )

    raw_doctor_ids = (
        pandas.DataFrame(
            [[doctor.attrs['onmouseover'], doctor.text] for doctor in
             file_data.select('td .js-moveSlot[onmouseover^=Medinet]')],
            columns=['raw_doctor_id', 'doctor_name']
        )
    )

    names_by_ids = (
        raw_doctor_ids
        .assign(doctor_id=raw_doctor_ids['raw_doctor_id']
                .str.extract("'(\d{1,3})','doctor'", expand=True))
        .dropna()
        .drop(['raw_doctor_id'], axis=1)
    )

    merged_table = (
        pandas.merge(shifts_by_days, names_by_ids, on='doctor_id')
        .drop(['doctor_id'], axis=1)
    )

    stripped_table = (
        merged_table
        .assign(shift_type=merged_table['shift_type'].str.strip())
        .assign(doctor_name=merged_table['doctor_name'].str.strip())
    )

    return_table = (
        stripped_table[['date', 'doctor_name', 'shift_type']]
        .assign(shift_type=stripped_table['shift_type']
                .replace('', numpy.nan))
        .dropna()
        .astype({'date': 'datetime64[ns]',
                 'doctor_name': 'category',
                 'shift_type': 'category'})
        .sort_values(['doctor_name', 'date', 'shift_type'])
        .reset_index()
        .drop(['index'], axis=1)
    )

    return return_table
