# Generated by Django 3.1.2 on 2020-10-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0002_auto_20201019_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='level',
            field=models.IntegerField(default=2, verbose_name='Class Level'),
            preserve_default=False,
        ),
    ]