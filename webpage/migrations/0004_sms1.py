# Generated by Django 4.1.4 on 2023-03-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_question_question_choices_rename_members_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sms1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.BooleanField(default=False)),
                ('main', models.BooleanField(default=True)),
                ('date', models.BooleanField(default=False)),
                ('link', models.BooleanField(default=True)),
            ],
        ),
    ]
