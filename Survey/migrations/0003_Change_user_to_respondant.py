# Generated by Django 2.1.1 on 2018-09-30 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Survey', '0002_Unique_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='user',
            new_name='respondent',
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('respondent', 'question')},
        ),
    ]
