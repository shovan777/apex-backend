# Generated by Django 3.2.13 on 2022-06-02 13:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0007_alter_question_detail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="option",
            name="detail",
            field=ckeditor.fields.RichTextField(verbose_name="detail"),
        ),
    ]