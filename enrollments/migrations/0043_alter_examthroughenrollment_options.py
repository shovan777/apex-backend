# Generated by Django 3.2.13 on 2022-12-26 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("enrollments", "0042_alter_coursethroughenrollment_completed_date"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="examthroughenrollment",
            options={
                "ordering": ["-id"],
                "verbose_name": "ExamThroughEnrollment",
                "verbose_name_plural": "ExamThroughEnrollments",
            },
        ),
    ]