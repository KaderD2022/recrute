# Generated by Django 4.2.5 on 2023-09-12 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_email_user_first_name_user_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
