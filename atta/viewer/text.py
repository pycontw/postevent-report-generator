def welcome_ask_year():
    print("Welcome to the PyCon attendees analyzer.")
    year = int(input('Please enter the year to be analyzed: '))
    return year


def select_column(df):
    cols = df.keys().tolist()
    for i, col in enumerate(cols):
        print(i, ':', col)

    registration_date = int(input('Please select the number for '
                                  '"報名日期/Paid date": '))
    nationality = int(input('Please select the number for '
                            '"國籍/Nationality": '))
    gender = int(input('Please select the number for '
                       '"性別/Gender": '))
    job_title = int(input('Please select the number for '
                          '"職稱/Job Titles": '))

    df_selected = df.iloc[:, [gender, nationality,
                              registration_date, job_title]]

    df_selected.columns = ['Gender', 'Nationality',
                           'Registration_date', 'Title']

    return df_selected
