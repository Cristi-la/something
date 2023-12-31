# Generated by Django 4.2.5 on 2023-12-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdata',
            name='first_name',
            field=models.CharField(blank=True, help_text='The first name of the user.', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='accountdata',
            name='last_name',
            field=models.CharField(blank=True, help_text='The last name of the user.', max_length=30, null=True),
        ),
    ]
