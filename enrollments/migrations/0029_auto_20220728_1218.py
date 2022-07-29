# Generated by Django 3.2.13 on 2022-07-28 06:33

import django.db.models.deletion
from django.db import migrations, models


def link_exam_session_to_session(apps, schema_editor):
    ExamSession = apps.get_model("enrollments", "ExamSession")
    Session = apps.get_model("enrollments", "Session")
    for (exam_session, session) in zip(
        ExamSession.objects.all(), Session.objects.all()
    ):
        exam_session.session_ptr = session
        exam_session.save()


def reverse_link_exam_session_to_session(apps, schema_editor):
    ExamSession = apps.get_model("enrollments", "ExamSession")
    for exam_session in ExamSession.objects.all():
        exam_session.session_ptr = None
        exam_session.save()


class Migration(migrations.Migration):

    dependencies = [
        ("enrollments", "0028_remove_session_exam"),
    ]

    operations = [
        migrations.AddField(
            model_name="examsession",
            name="session_ptr",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                serialize=False,
                to="enrollments.session",
            ),
            # preserve_default=False,
        ),
        migrations.RunPython(
            link_exam_session_to_session, reverse_link_exam_session_to_session
        ),
        migrations.RemoveField(
            model_name="examsession",
            name="id",
        ),
        migrations.AlterField(
            model_name="examsession",
            name="session_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="enrollments.session",
            ),
            # preserve_default=False,
        ),
    ]