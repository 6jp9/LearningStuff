# Generated by Django 5.1.5 on 2025-03-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='eaddr',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='employees',
            name='ename',
            field=models.CharField(max_length=50),
        ),
    ]
