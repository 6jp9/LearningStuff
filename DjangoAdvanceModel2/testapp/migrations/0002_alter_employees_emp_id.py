# Generated by Django 5.1.5 on 2025-03-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='emp_id',
            field=models.IntegerField(),
        ),
    ]
