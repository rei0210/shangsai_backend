# Generated by Django 5.1.6 on 2025-02-20 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Questionnaire", "0002_alter_questionnaire_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="questionnaire",
            name="user",
        ),
    ]
