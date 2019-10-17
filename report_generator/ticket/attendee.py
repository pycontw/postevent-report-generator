class Attendee:
    def __init__(self, df):
        self.df = df

    @property
    def total_attendee_number(self):
        dates = self.df["Registration_date"]
        # dates.value_counts()
        return len(dates)
