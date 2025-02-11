# Generated by Django 5.1.5 on 2025-02-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test_table_Gov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Location', models.CharField(max_length=20)),
                ('eligibility', models.CharField(max_length=20)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Test_table_IT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Location', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('eligibility', models.CharField(max_length=20)),
                ('link', models.TextField()),
            ],
        ),
    ]
