class Opass:
    def __init__(self, df):
        self.df = df
        self.opass_sheet = df.get("Opass")

    @property
    def total_day1checkin_number(self):
        dates = self.opass_sheet[["Token", "Day1Checkin"]].dropna()
        # dates.value_counts()
        return len(dates)

    @property
    def total_day2checkin_number(self):
        dates = self.opass_sheet[["Token", "Day2Checkin"]].dropna()
        # dates.value_counts()
        return len(dates)

    @property
    def total_day3checkin_number(self):
        dates = self.opass_sheet[["Token", "Day3Checkin"]].dropna()
        # dates.value_counts()
        return len(dates)
