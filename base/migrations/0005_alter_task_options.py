# Generated by Django 3.2.9 on 2021-12-18 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_task_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed']},
        ),
    ]
