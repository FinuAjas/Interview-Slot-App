# Generated by Django 5.1.3 on 2024-11-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.BigIntegerField(unique=True)),
                ('role', models.CharField(choices=[('Candidate', 'Candidate'), ('Interviewer', 'Interviewer')], max_length=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
