# Generated by Django 3.2.13 on 2022-06-05 10:29

from django.db import migrations

import common.modelFields
import common.validators


class Migration(migrations.Migration):

    dependencies = [
        ("enrollments", "0010_auto_20220605_1454"),
    ]

    operations = [
        migrations.AlterField(
            model_name="session",
            name="end_date",
            field=common.modelFields.ZeroSecondDateTimeField(
                validators=[common.validators.validate_date_time_gt_now],
                verbose_name="end_date",
            ),
        ),
        migrations.AlterField(
            model_name="session",
            name="start_date",
            field=common.modelFields.ZeroSecondDateTimeField(
                validators=[common.validators.validate_date_time_gt_now],
                verbose_name="start_date",
            ),
        ),
    ]