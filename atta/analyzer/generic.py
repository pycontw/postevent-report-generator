import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import re


def go():

    get_ipython().run_line_magic('matplotlib', 'inline')
    sns.set_style("darkgrid",{"font.sans-serif":['simhei', 'Arial']})

    df = pd.read_csv("./data/2017Attendees.csv")


    # paid date could be relating to "information acquired " earlier vs later
    df.keys()

    df.rename(index=str, columns={"Id": "ID", "Gender / 性別": "Gender","Nationality / 國籍": "Nationality","服務公司(學生或老師請填學校名稱+系所) / Company(Students or teachers please fill in the school name + Department)":"Organization","職稱(如果身分是學生請填”學生”) / Job Titles(If you are a student please fill in \"student\")":"Title","Diet / 飲食":"Special food requirments","Size of T-shirt / T恤尺寸":"Size","發票抬頭(購買 \"個人/企業一般票\" 才需要填寫) / Invoiced Company Name":"Invoice Company name"}, inplace = True)


    df.drop("# invoice policy #",axis = 1, inplace = True)

    # Plotting categorical
    plt.subplots(figsize=(18,5))
    sns.countplot(x='Gender',data=df)

    fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)
    sns.countplot(x='Nationality',data=df)


    # ## Create title category list and plot

    organ_list = df['Organization'].unique().tolist()
    title_list = df['Title'].unique().tolist()
    # Categories
    # Find ones without jobs
    organ_count = len(organ_list)
    title_count = len(title_list)
    print(organ_count, title_count)


    nojob = df.loc[df['Title'] == np.nan]

    title_count = df['Title'].value_counts()
    title_count = title_count.to_frame(name = "Count").reset_index()
    title_count.columns.values[0] = 'Title'
    title_count

    title_count[title_count['Count'] > 4]


    title_list


    # Create main categories in a new column.

    #?? what is PA? how to categorize analyser?

    pattern_engineer = "(?i)[engineer]{6,}|engr|developer|code|software|工程師|碼|程式|資訊|program|軟體|設計|專員|IT|Analysts" # 專員?
    pattern_developer = "(?i)develop|architect|^R.*D$|開發"
    pattern_student = "學生|(?i)student"
    pattern_nobody = "(?i)無|0|沒有人|nobody|nan|自由業|none|self-employed"
    # why no* match everyting???
    pattern_research = "(?i)phd|博|postdoc|research|研究"
    pattern_job_seek = "(?i)待業|Home|job|自由業|助理[^教授]|Freelance|self-employed"
    # 助理 could be a temporary job, but not 助理教授
    pattern_head = "(?i)C.O|chief|lead|chair|director|長|總|founder"
    pattern_professor = "(?i)PI|professor|教授"
    pattern_data_scientist = "(?i)data|資料|使用|經驗|分析|scientist"
    pattern_consultant = "(?i)consultant|顧問"
    pattern_manager = "(?i)manager|[^助]理|pm"
    pattern_graphics = "(?i)graph|art|cgi"
    title_categories = {"graphic_artist":[],"developer":[],"uncategorized":[],
                        "consultant":[],"data_scientist":[],"job_seeker":[],
                        "engineer":[],'student':[],'professor':[],'researcher':[],
                        'nobody':[],'head':[],'manager':[]}

    # Assign to categories
    # Find participants without jobs

    for title in title_list:
        try:
            if re.search(pattern_head, title) != None:
                title_categories['head'].append(title)
            elif re.search(pattern_manager, title) != None:
                title_categories['manager'].append(title)
            elif re.search(pattern_developer, title) != None:
                title_categories['developer'].append(title)
            elif re.search(pattern_engineer, title) != None:
                title_categories['engineer'].append(title)
            elif re.search(pattern_data_scientist, title) != None:
                title_categories['data_scientist'].append(title)
            elif re.search(pattern_student, title) != None:
                title_categories['student'].append(title)
            elif re.search(pattern_nobody, title) != None:
                title_categories['nobody'].append(title)
            elif re.search(pattern_job_seek, title) != None:
                title_categories['job_seeker'].append(title)
            elif re.search(pattern_professor, title) != None:
                title_categories['professor'].append(title)
            elif re.search(pattern_consultant, title) != None:
                title_categories['consultant'].append(title)
            elif re.search(pattern_research, title) != None:
                title_categories['researcher'].append(title)
            elif re.search(pattern_graphics, title) != None:
                title_categories['graphic_artist'].append(title)
            else:
                title_categories['uncategorized'].append(title)
        except TypeError:
            pass


    key = []
    counts = []
    j = -1
    for i in title_categories.values():
        j += 1
        key.append(list(title_categories.keys())[j])
        counts.append(len(i))

    title_cat_counts = pd.DataFrame({'1_Title':key,'2_Counts':counts})
    title_cat_counts['3_Name'] = list(title_categories.values())
    title_cat_counts
    title_cat_counts.sort_values('2_Counts',ascending=False, inplace= True)
    title_cat_counts.reset_index(drop = True)

    title_cat_counts.iloc[1]['3_Name']


    # ## Add new column in dataframe with title categories


    def cat_title(title):
        title = str(title)
        pattern_engineer = "(?i)[engineer]{6,}|engr|developer|code|software    |工程師|碼|程式|資訊|program|軟體|設計|專員|IT|Analysts|SW|AP|PG|F2E|DevOps" # 專員?
        pattern_developer = "(?i)develop|architect|^R.*D$|開發|AP"
        pattern_student = "學生|(?i)student"
        pattern_nobody = "(?i)無|0|沒有人|nobody|nan|自由業|none|self-employed"
        # why no* match everyting???
        pattern_research = "(?i)phd|博|postdoc|research|研究"
        pattern_job_seek = "(?i)待業|Home|job|自由業|助理[^教授]|Freelance|self-employed"
        # 助理 could be a temporary job, but not 助理教授
        pattern_head = "(?i)C.O|chief|lead|chair|director|長|總|founder"
        pattern_professor = "(?i)PI|professor|教授"
        pattern_data_scientist = "(?i)data|資料|使用|經驗|分析|scientist"
        pattern_consultant = "(?i)consultant|顧問"
        pattern_manager = "(?i)manager|[^助]理|pm"
        pattern_graphics = "(?i)graph|art|cgi"
    #     pattern_list = [pattern_consultant, pattern_data_scientist, pattern_developer,
    #                    pattern_engineer, pattern_graphics, pattern_head, pattern_job_seek,
    #                    pattern_manager, pattern_nobody, pattern_professor]
        pattern_dic = {'Engineer':pattern_engineer,'Consultant':pattern_consultant,
                       'Data Scientist':pattern_data_scientist, 'Developer':pattern_developer,
                       'Job Seeker':pattern_job_seek,'Head':pattern_head,'Professor': pattern_professor,
                      'Manager':pattern_manager, 'Graphics': pattern_graphics, 'Researcher':pattern_research,
                      'Student':pattern_student}
        title_cat = ''
        for pattern in pattern_dic:
            if re.search(pattern_dic[pattern], title) != None:
                title_cat = pattern
            else:
                pass
        return title_cat




    new_col = np.nan
    #df.insert(loc=12, column='Title_Categories', value=new_col)
    df['Title_Categories'] = df['Title'].apply(cat_title)
    df


    # In[32]:


    pattern_nobody = "(?i)無|0|沒有人|nobody|nan|自由業|none|self-employed"

    pattern = '家|自'

    # df2 =pd.DataFrame( {'A':[1,2,3],
    #      'B':[4,5,6],'C':[7,8,9]})
    # df3 = df2[['A','B']]
    # df3

    # Without a job: See from Organization

    # Nan: 32,71,101,104,325,569
    # none: 194, 274, 276,301,375,426, 498
    # 不告訴你： 9,263,560
    # 家裡個人接案：435,436,465,
    # 560 : 表情符號...

    # 488是駭客！

    df[['Organization','Title']].iloc[9]


    # ## Plot title categories



    df['Title_Categories'].value_counts('Job Seeker')




    fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)
    ax.set_xticklabels('1_Title',rotation=90,fontdict= {"fontsize": '16'})
    ax.set_xlabel(xlabel="Job Title")
    ax.set_ylabel(ylabel= "Counts")
    sns.set(font_scale = 2)

    sns.countplot(x = 'Title_Categories', data = df, ax = ax,
                  order = ['Engineer', 'Student', 'Developer', 'Manager', 'Researcher',
           'Data Scientist', 'Head', 'Professor', 'Job Seeker', 'Consultant',
           'Graphics', 'Others'])


    fig, ax = plt.subplots()
    fig.set_size_inches(11.7, 8.27)
    ax.set_xticklabels('1_Title',rotation=45,fontdict= {"fontsize": '16'})
    ax.set_xlabel(xlabel="Job Title")
    ax.set_ylabel(ylabel= "Counts")
    sns.set(font_scale = 2)

    sns.barplot(x = '1_Title', y = "2_Counts", data = title_cat_counts, ax = ax)

def fake_go():
    print('fake_go is executed.')
