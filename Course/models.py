from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

from Course.manager import CourseManager


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)  # 课程 ID（自动递增）
    course_name = models.CharField(max_length=255)  # 课程名称
    course_simplified_name = models.CharField(max_length=100, blank=True, null=True)  # 简称
    #teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # 关联教师（Django User）

    manager=CourseManager()

    class Meta:
        db_table = 'course'  # 自定义表名

    def __str__(self):
        return self.course_name
