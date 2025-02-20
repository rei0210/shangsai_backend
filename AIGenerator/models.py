from django.db import models
import ollama

from Questionnaire.models import Questionnaire


# Create your models here.
class AIGenerator:
    def __init__(self):
        self.qn=Questionnaire()


    def generate_question(self,user_input):
        self.qn.chat_history_list.append({"role": "user", "content": user_input})
        # 调用 Mistral 进行聊天
        response = ollama.chat(
            model="mistral",
            messages=self.qn.chat_history_list  # 传入完整的对话历史
        )

        # 获取 AI 响应
        ai_response = response["message"]["content"]
        print(f"Mistral: {ai_response}")


        # 追加 AI 回复到对话历史
        self.qn.chat_history_list.append({"role": "assistant", "content": ai_response})