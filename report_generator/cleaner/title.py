import collections
import re


# Add new column in dataframe with title categories
def cat_title(title):
    """
    Return the category of a given title.

    >>> cat_title("工程師")
    'Engineer'

    """
    title = str(title)
    pattern_dic = collections.OrderedDict()
    pattern_dic["Potential Job Seeker"] = (
        "(?i)待業|Home|job|自由業|"
        "助理[^教授]|"
        "Freelance|self-employed|無|"
        "0|沒有人"
        "|nobody|nan|自由業|none"
    )
    # 助理 could be a temporary job therefore potential job seeker,
    # but not 助理教授
    pattern_dic["Head"] = "(?i)C.O|chief|lead|chair|director|長|總|founder"
    pattern_dic["Manager"] = "(?i)manager|[^助]理|pm"
    pattern_dic["Engineer"] = (
        "(?i)[engineer]{6,}|engr|"
        "develop|code|software|"
        "工程師|碼|程式|資訊|program|"
        "軟體|設計|IT|Analysts|SW|AP|PG|F2E|DevOps|"
        "architect|^R.*D$|開發|bug|hacker"
    )
    # '設計'有點不精確...
    pattern_dic["Student"] = "學生|(?i)student"
    pattern_dic["Academia"] = "(?i)phd|博|postdoc|research" "|研究|PI|professor|教授"
    pattern_dic["Data Scientist"] = "(?i)data|資料|使用|經驗|分析|scientist"
    pattern_dic["Consultant"] = "(?i)consultant|顧問"

    title_cat = ""
    for pattern in pattern_dic:
        if re.search(pattern_dic[pattern], title) is not None:
            title_cat = pattern
        else:
            pass
    return title_cat


if __name__ == "__main__":
    import doctest

    doctest.testmod()
