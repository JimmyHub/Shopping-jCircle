# Generated by Django 3.1.7 on 2021-07-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210618_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='limit',
            field=models.IntegerField(default=0, verbose_name='權限'),
        ),
    ]
