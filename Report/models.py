from django.db import models

from django.db import models

from Questionnaire.models import Questionnaire


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)  # 自动生成 ID
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)  # 关联问卷
    report_content = models.TextField()  # 报告内容

    class Meta:
        db_table = 'report'  # 自定义表名

    def __str__(self):
        return f"Report {self.report_id} for Questionnaire {self.questionnaire.qn_id}"
