import report_generator.config as report_generatorconfig

conf_singlet = report_generatorconfig.Configuration.get_instance()


def welcome_ask_year(interactive=False):
    print("Welcome to the PyCon attendees analyzer.")
    if interactive:
        year = int(input("Please enter the year to be analyzed: "))
    else:
        attendee_session = conf_singlet.config["ATTENDEE"]
        year = attendee_session["year"]

    return year


def pickup_column(column_title, csv_index, field_seperator=","):
    attendee_session = conf_singlet.config["ATTENDEE"]
    column_titles = attendee_session[column_title]
    column_number = column_titles.split(field_seperator)[csv_index]

    return column_number


def select_column(df, interactive, csv_index):

    cols = df.keys().tolist()
    for i, col in enumerate(cols):
        print(i, ":", col)

    if interactive:
        registration_date = int(
            input("Please select the number for " '"報名日期/Paid date": ')
        )
        nationality = int(input("Please select the number for " '"國籍/Nationality": '))
        gender = int(input("Please select the number for " '"性別/Gender": '))
        job_title = int(input("Please select the number for " '"職稱/Job Titles": '))
        seniority = int(input("Please select the seniority: "))
        interested_field = int(
            input("Please select the number for" "Area of Interest / 興趣領域 :")
        )
    else:
        registration_date = int(pickup_column("paid_date", csv_index))
        nationality = int(pickup_column("nationality", csv_index))
        gender = int(pickup_column("gender", csv_index))
        job_title = int(pickup_column("job_title", csv_index))
        seniority = int(pickup_column("seniority", csv_index))
        interested_field = int(pickup_column("interested_field", csv_index))

    df_selected = df.iloc[
        :,
        [
            gender,
            nationality,
            registration_date,
            job_title,
            seniority,
            interested_field,
        ],
    ]

    df_selected.columns = [
        "Gender",
        "Nationality",
        "Registration_date",
        "Title",
        "Seniority",
        "Interested_Field",
    ]

    return df_selected
