# Generated by Django 2.1.1 on 2018-09-13 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20180913_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancerecord',
            name='emp_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendance.Employee'),
        ),
    ]
