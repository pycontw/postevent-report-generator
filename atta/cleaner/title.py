import re


# Add new column in dataframe with title categories
def cat_title(title):
    """
    Return the category of a given title.

    >>> cat_title("工程師")
    'Engineer'

    """
    title = str(title)
    pattern_engineer = "(?i)[engineer]{6,}|engr|developer|code|software    |工程師|碼|程式|資訊|program|軟體|設計|專員|IT|Analysts|SW|AP|PG|F2E|DevOps"  # 專員?
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
    pattern_dic = {'Engineer': pattern_engineer, 'Consultant': pattern_consultant,
                   'Data Scientist': pattern_data_scientist, 'Developer': pattern_developer,
                   'Job Seeker': pattern_job_seek, 'Head': pattern_head, 'Professor': pattern_professor,
                   'Manager': pattern_manager, 'Graphics': pattern_graphics, 'Researcher': pattern_research,
                   'Student': pattern_student}
    title_cat = ''
    for pattern in pattern_dic:
        if re.search(pattern_dic[pattern], title) != None:
            title_cat = pattern
        else:
            pass
    return title_cat

if __name__ == "__main__":
    import doctest
    doctest.testmod()
