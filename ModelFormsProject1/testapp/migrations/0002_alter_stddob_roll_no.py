# Generated by Django 5.1.5 on 2025-02-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stddob',
            name='roll_no',
            field=models.CharField(max_length=10),
        ),
    ]
