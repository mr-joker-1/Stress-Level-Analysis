# Generated by Django 4.2.1 on 2023-08-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserPredictModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr', models.CharField(max_length=100)),
                ('rr', models.CharField(max_length=100)),
                ('t', models.CharField(max_length=100)),
                ('lm', models.CharField(max_length=100)),
                ('bo', models.CharField(max_length=100)),
                ('rem', models.CharField(max_length=100)),
                ('srh', models.CharField(max_length=100)),
                ('hr', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
            ],
        ),
    ]
