# Generated by Django 3.0.4 on 2020-04-10 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200410_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ask',
            old_name='askq',
            new_name='qsns',
        ),
    ]
