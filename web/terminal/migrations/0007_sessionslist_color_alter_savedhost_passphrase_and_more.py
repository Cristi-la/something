# Generated by Django 4.2.5 on 2023-12-15 20:21

import colorfield.fields
from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0006_rename_savedhosts_savedhost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionslist',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', help_text='Tab color', image_field=None, max_length=25, samples=None),
        ),
        migrations.AlterField(
            model_name='savedhost',
            name='passphrase',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True, help_text='The passphrase for the private key (if applicable).', null=True),
        ),
        migrations.AlterField(
            model_name='savedhost',
            name='password',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True, help_text='The password for accessing the saved host.', null=True),
        ),
    ]
