from AIGenerator.exception import QuestionParsingError
from Questionnaire.models import Question, Choice
from Report.models import Report
import re
import json

def parse_question(text):#把llm生成的文本格式的问题解析为一个Question对象

    q = Question(0, "")
    q.question_id = 0
    question_pattern = re.compile(r'(?P<question>^.+?)\s*(?P<choices>(?:[A-D])\)\s.+(?:\n[A-D]\)\s.+)*)',
                                  re.MULTILINE | re.DOTALL)

    match = question_pattern.search(text)
    # print(match)
    if not match:
        raise QuestionParsingError("cannot parse the question")
    question_text = match.group("question").strip()
    choices_text = match.group("choices").strip()
    choices_text = re.sub(r'\n', '', choices_text).strip()
    # print(question_text)
    # print(choices_text)

    # Regex to extract individual choices
    choice_list_str = re.split(r'\s+(?=[A-D]\))', choices_text)
    #print(choice_list_str)
    choice_pattern = re.compile(r'([A-D])\)\s(.+)')
    choices = []
    for choice in choice_list_str:
        match = choice_pattern.match(choice)
        if match:
            one_choice_id = match.group(1)  # 选项字母 A, B, C, D
            one_choice_text = match.group(2).strip()  # 选项内容，去除两端空格
            # print("选项字母:", choice_id)
            #print("选项内容:", one_choice_text)
            is_other = "(please specify)" in one_choice_text.lower()
            c = Choice(one_choice_id, one_choice_text, is_other)
            choices.append(c)
    #print(choices)
    # for choice_match in choice_pattern.finditer(choices_text):
    #     print(choice_match.group())
    #     choice_id = choice_match.group(1)  # A, B, C, D
    #     choice_text = choice_match.group(2).strip()  # "xxxx", "yyyy", etc.

    # Check if the choice contains "other(please specify)"

    # choices.append({
    #     "choice_id": choice_id,
    #     "text": choice_text,
    #     "need_fill": is_other  # Boolean to indicate if it's an "Other" option
    # })
    q.choices = choices
    q.text = question_text

    return q

def parse_report(report_text):
    r=Report()
    return r

