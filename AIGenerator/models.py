from charset_normalizer.cli import query_yes_no
from django.db import models
import ollama

from AIGenerator.exception import QuestionParsingError
from AIGenerator.tools import parse_question, parse_report
from Questionnaire.models import Questionnaire, Question


# Create your models here.
class AIGenerator:
    def __init__(self,qn):
        self.qn=qn
        self.num_of_questions=0


    def initial_question(self):
        initial_input={"role": "system", "content": "You are an intelligent classroom feedback assistant that can generate multiple-choice questions to ask the student's feelings about the course and adaptively create follow-up questions based on user responses."
                                            "No other content needed."
                                            "You should generate only one question at a time"
                                            "The number of choices is not fixed. "
                                            "Please Follow the format below:"
                                            "How do you feel about the course?"
                                            "A) xxxx"
                                            "B) yyyy"
                                           " C) zzzz "
                                           " D) other(please specify)"
                       }


        return self.generate_question(initial_input)


    def generate_question(self,user_input):
        self.qn.chat_history_list.append({"role": "user", "content": user_input})
        # 调用 Mistral 进行聊天
        question_ok=False
        ai_question=Question()
        ai_response=""
        while not question_ok:
            response = ollama.chat(
                model="mistral",
                messages=self.qn.chat_history_list  # 传入完整的对话历史
            )

            # 获取 AI 响应
            ai_response = response["message"]["content"]
            print(f"Mistral: {ai_response}")
            try:
                ai_question=parse_question(ai_response)

                question_ok = True
            except QuestionParsingError as e:
                print(f"Question parsing error: {e}")
                question_ok=False


        # 追加 AI 回复到对话历史
        self.qn.chat_history_list.append({"role": "assistant", "content": ai_response})
        self.num_of_questions+=1
        ai_question.question_id = self.num_of_questions
        return ai_question #返回解析后的问题对象

    def generate_report(self):
        report_input={"role": "system","content":"Please generate a report based on all of the user's response."}
        self.qn.chat_history_list.append(report_input)
        report_ok=False
        while not report_ok:
            response = ollama.chat(
                model="mistral",
                messages=self.qn.chat_history_list  # 传入完整的对话历史
            )

            # 获取 AI 响应
            ai_response = response["message"]["content"]
            print(f"Mistral: {ai_response}")
            try:
                ai_report=parse_report(ai_response)

                report_ok = True

                return ai_report
            except QuestionParsingError as e:
                print(f"Question parsing error: {e}")
                report_ok=False

