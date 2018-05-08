import re
import collections

# Add new column in dataframe with title categories
def cat_title(title):
    """
    Return the category of a given title.

    >>> cat_title("工程師")
    'Engineer'

    """
    title = str(title)
    pattern_engineer = "(?i)[engineer]{6,}|engr|develop|code|software|工程師|碼|程式|資訊|program|軟體|設計|專員|IT|" \
                       "Analysts|SW|AP|PG|F2E|DevOps|architect|^R.*D$|開發|bug|hacker"
    pattern_student = "學生|(?i)student"
    pattern_academia = "(?i)phd|博|postdoc|research|研究|PI|professor|教授"
    pattern_job_seek = "(?i)待業|Home|job|自由業|助理[^教授]|Freelance|self-employed|無|0|沒有人|nobody|nan|自由業|none"
    # 助理 could be a temporary job therefore potential job seeker, but not 助理教授
    pattern_head = "(?i)C.O|chief|lead|chair|director|長|總|founder"
    pattern_data_scientist = "(?i)data|資料|使用|經驗|分析|scientist"
    pattern_consultant = "(?i)consultant|顧問"
    pattern_manager = "(?i)manager|[^助]理|pm"
    pattern_graphics = "(?i)graph|art|cgi"
    pattern_dic = collections.OrderedDict()
    pattern_dic.update({'Head': pattern_head, 'Consultant': pattern_consultant, 'Manager': pattern_manager,
                   'Data Scientist': pattern_data_scientist, 'Engineer': pattern_engineer,'Graphics': pattern_graphics,
                    'Academia': pattern_academia, 'Potential Job Seeker': pattern_job_seek,'Student': pattern_student})
    title_cat = ''
    for pattern in pattern_dic:
        if re.search(pattern_dic[pattern], title) is not None:
            title_cat = pattern
        else:
            pass
    return title_cat

if __name__ == "__main__":
    import doctest
    doctest.testmod()
