# Generated by Django 4.2.5 on 2024-01-02 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0015_alter_accountdata_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notesdata',
            name='session_master',
            field=models.ForeignKey(default=None, help_text='The user who created the session.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sshdata',
            name='session_master',
            field=models.ForeignKey(help_text='The user who created the session.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
