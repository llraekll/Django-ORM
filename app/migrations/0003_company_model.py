# Generated by Django 4.1.4 on 2022-12-21 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_mraks'),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
    ]