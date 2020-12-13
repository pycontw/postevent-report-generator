class Conference:
    def __init__(self, year, report_yaml, talks_df, p_talks_df):
        self.year = year

        self._report_yaml = report_yaml
        self._talks_df = talks_df
        self._p_talks_df = p_talks_df

    @property
    def acceptance_rate(self):
        return get_acceptance_rate(self._talks_df, self._p_talks_df)

    @property
    def talk_number_accepted(self):
        return self._talks_df["category"].value_counts().sum()

    @property
    def fa_amount(self):
        return str(self._report_yaml["General_Info"]["FA_amount"])

    @property
    def fa_amount_usd(self):
        twd = self._report_yaml["General_Info"]["FA_amount"]
        usd = twd * self._report_yaml["General_Info"]["rate_twd_usd"]
        usd_round = "{:.6}".format(usd)
        return usd_round


def get_acceptance_rate(accepted_talk_df, proposed_talk_df):
    accepted_talk_number = accepted_talk_df["category"].value_counts().sum()
    all_talk_number = proposed_talk_df["category"].value_counts().sum()
    acceptance_rate = "{:.1%}".format(accepted_talk_number / all_talk_number)

    print(
        f"{accepted_talk_number} accepted proposals out of {all_talk_number}. Acceptance rate: {acceptance_rate}"
    )

    return acceptance_rate
