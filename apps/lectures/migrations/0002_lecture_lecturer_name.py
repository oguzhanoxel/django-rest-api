# Generated by Django 3.1.2 on 2020-10-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecturer_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]