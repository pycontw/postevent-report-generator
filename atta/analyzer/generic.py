import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re
import logging
import os
import collections
# from atta.cleaner.title import cat_title

def cat_title(title):
    """
    Return the category of a given title.

    >>> cat_title("工程師")
    'Engineer'

    """
    title = str(title)
    pattern_dic = collections.OrderedDict()
    pattern_dic['Potential Job Seeker'] = "(?i)待業|Home|job|自由業|助理[^教授]|" \
                                          "Freelance|self-employed|無|0|沒有人|nobody|nan|自由業|none"
    # 助理 could be a temporary job therefore potential job seeker, but not 助理教授
    pattern_dic['Head'] = "(?i)C.O|chief|lead|chair|director|長|總|founder"
    pattern_dic['Manager'] = "(?i)manager|[^助]理|pm"
    pattern_dic['Engineer'] = "(?i)[engineer]{6,}|engr|develop|code|software|工程師|碼|程式|資訊|program|" \
                              "軟體|設計|IT|Analysts|SW|AP|PG|F2E|DevOps|architect|^R.*D$|開發|bug|hacker"
    #'設計'有點不精確...
    pattern_dic['Student'] = "學生|(?i)student"
    pattern_dic['Academia'] = "(?i)phd|博|postdoc|research|研究|PI|professor|教授"
    pattern_dic['Data Scientist'] = "(?i)data|資料|使用|經驗|分析|scientist"
    pattern_dic['Consultant'] =  "(?i)consultant|顧問"

    title_cat = ''
    for pattern in pattern_dic:
        if re.search(pattern_dic[pattern], title) is not None:
            title_cat = pattern
        else:
            pass
    return title_cat

def welcome_ask_year():
    print("Welcome to the PyCon attendies analyzer.")
    year = int(input('Please enter the year to be analyzed: '))
    return year

def select_column(df):
    cols = df.keys().tolist()
    for i, col in enumerate(cols):
        print(i,':',col)
    registration_date = int(input('Please select the number for "報名日期/Paid date": '))
    nationality = int(input('Please select the number for "國籍/Nationality": '))
    gender = int(input('Please select the number for "性別/Gender": '))
    organization = int(input('Please select the number for "服務單位/Company": '))
    job_title = int(input('Please select the number for "職稱/Job Titles": '))

    # col_index = {'job_title':job_title,'organization':organization,'gender':gender,
    #              'registration_date':registration_date,'nationality':nationality}
    df_selected = df.iloc[:,[gender, nationality, registration_date, job_title]]
    df_selected.columns = ['Gender','Nationality','Registration_date','Title']
    return df_selected

def add_cat_title(df):
    df['Title_Categories'] = df['Title'].apply(cat_title)
#    title_category = df.columns.get_loc("Title_Categories")
    return df



def plot_counts(df,year):
    cols = df.keys().tolist()
    bar_cols = [cols[0],cols[1],cols[4]]  # change here to include more columns for count plots
    for col in bar_cols:
        fig, ax = plt.subplots(figsize=(12, 8))
        plt.title(str(col)+' of the Attendees at PyCon Taiwan in ' + str(year))
        ax.set_xticklabels(str(col), rotation=0, fontdict={"fontsize": '8'})
        ax.set_xlabel(xlabel=str(col))
        ax.set_ylabel(ylabel="Counts")
        sns.set(font_scale=2)
        sns.countplot(x = str(col), data = df)
        # directory = Tk.tk() # Something about
        plt.savefig(str(col) + str(year) + '.jpg')

# def plot_accumulated_count(df,year):

#

# def save_df():
#     df.to_pickle(str(year)+"_analyzed_data")  ## need to refine directory


def go(csvfile):

    '''Get file. Replace hardcoded line with CLI input'''
    # welcome user, ask year of data
    year = welcome_ask_year()
    # read csv as pandas dataframe
    df = pd.read_csv(csvfile)
    # Print the keys as bug messages
    logging.debug(df.keys())
    # select necessary columns from df
    df = select_column(df)
    df = add_cat_title(df)
    plot_counts(df,year)
    print('Go process finished completely. Find results in the same directory as the csv file.')

def fake_go():
    print('fake_go is executed.')

