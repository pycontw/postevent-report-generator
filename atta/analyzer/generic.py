import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re
import logging
import os
from atta.cleaner.title import cat_title

# VIEW
def welcome_ask_year():
    print("Welcome to the PyCon attendies analyzer.")
    year = int(input('Please enter the year to be analyzed: '))
    return year
# collect data to controller

#View
def select_column(df):
    cols = df.keys().tolist()
    for i, col in enumerate(cols):
        print(i,':',col)
    registration_date = int(input('Please select the number for "報名日期/Paid date": '))
    nationality = int(input('Please select the number for "國籍/Nationality": '))
    gender = int(input('Please select the number for "性別/Gender": '))
    organization = int(input('Please select the number for "服務單位/Company": '))
    job_title = int(input('Please select the number for "職稱/Job Titles": '))
    df_selected = df.iloc[:,[gender, nationality, registration_date, job_title]]
    df_selected.columns = ['Gender','Nationality','Registration_date','Title']
    return df_selected
# Collect data to controller

# Model
def add_cat_title(df):
    df['Title_Categories'] = df['Title'].apply(cat_title)
    return df


# Controller
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

# Show graph in viewer

# def plot_accumulated_count(df,year):
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
