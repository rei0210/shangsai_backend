from Questionnaire.models import Question


def parse_question(question_text):#把llm生成的文本格式的问题解析为一个Question对象

    q=Question()
    return q