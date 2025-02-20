import json

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from Course.models import Course



# Create your models here.
class Questionnaire(models.Model):

    qn_id = models.AutoField(primary_key=True)  # 自动生成主键
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联 Django 用户
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    create_time = models.DateTimeField(default=now)  # 创建时间
    finish_time = models.DateTimeField(null=True, blank=True)  # 完成时间
    chat_history = models.TextField(blank=True, null=True)  # 聊天历史（字符串）
    #chat_history_list = models.JSONField(blank=True, null=True)  # 聊天历史（JSON 格式）
    class Meta:
        db_table = 'questionnaire'  # 自定义表名

    @property
    def chat_history_list(self):
        """ 将 chat_history 转换为列表（仅在运行时使用，不存入数据库）"""
        if self.chat_history:
            return json.loads(self.chat_history)
        return []

    @chat_history_list.setter
    def chat_history_list(self, value):
        """ 允许设置 chat_history_list，并自动转换为 JSON 存入 chat_history """
        if isinstance(value, list):
            self.chat_history = json.dumps(value)
        else:
            raise ValueError("chat_history_list must be a list of dictionaries")

class Question:
    def __init__(self, question_id, text, choices=None):
        self.question_id = question_id
        self.text = text
        self.choices = choices or []  # 选项列表




    def add_choice(self, choice):
        """ 添加选项 """
        self.choices.append(choice)

    def to_dict(self):
        """ 转换为字典格式 """
        return {
            "question_id": self.question_id,
            "text": self.text,
            "choices": [choice.to_dict() for choice in self.choices]
        }

    def __str__(self):
        return f"Question({self.question_id}): {self.text}"


class Choice:
    def __init__(self, choice_id, text, need_fill=False):
        self.choice_id = choice_id
        self.text = text
        self.need_fill = need_fill  # 是否需要手动填写

    def to_dict(self):
        """ 转换为字典格式 """
        return {
            "choice_id": self.choice_id,
            "text": self.text,
            "need_fill": self.need_fill
        }

    def __str__(self):
        return f"Choice({self.choice_id}): {self.text} (need_fill: {self.need_fill})"