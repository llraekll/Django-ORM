# Generated by Django 4.1.4 on 2022-12-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mraks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
