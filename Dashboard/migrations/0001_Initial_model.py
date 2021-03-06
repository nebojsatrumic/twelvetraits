# Generated by Django 2.1.1 on 2018-09-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RespondentDashboardData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_on', models.DateTimeField(auto_created=True, auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('openness', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('conscientiousness', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('extraversion', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('agreeableness', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('neuroticism', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'verbose_name_plural': 'Respondent Data',
            },
        ),
    ]
