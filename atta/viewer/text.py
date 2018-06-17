import atta.config as attaconfig


conf_singlet = attaconfig.Configuration.get_instance()


def welcome_ask_year(interactive=False):
    print("Welcome to the PyCon attendees analyzer.")
    if interactive:
        year = int(input('Please enter the year to be analyzed: '))
    else:
        attendee_session = conf_singlet.config['ATTENDEE']
        year = attendee_session['year']

    return year


def select_column(df, interactive):
    attendee_session = conf_singlet.config['ATTENDEE']

    cols = df.keys().tolist()
    for i, col in enumerate(cols):
        print(i, ':', col)

    if interactive:
        registration_date = int(input('Please select the number for '
                                      '"報名日期/Paid date": '))
        nationality = int(input('Please select the number for '
                                '"國籍/Nationality": '))
        gender = int(input('Please select the number for '
                           '"性別/Gender": '))
        job_title = int(input('Please select the number for '
                              '"職稱/Job Titles": '))
    else:
        registration_date = int(attendee_session['paid_date'])
        nationality = int(attendee_session['nationality'])
        gender = int(attendee_session['gender'])
        job_title = int(attendee_session['job_title'])

    df_selected = df.iloc[:, [gender,
                              nationality,
                              registration_date,
                              job_title]]

    df_selected.columns = ['Gender', 'Nationality',
                           'Registration_date', 'Title']

    return df_selected
