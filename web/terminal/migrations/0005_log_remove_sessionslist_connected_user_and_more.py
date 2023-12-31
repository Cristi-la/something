# Generated by Django 4.2.5 on 2023-12-14 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('terminal', '0004_notesdata_sshdata_alter_savedhosts_user_sessionslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_text', models.TextField(help_text='Log entry text.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the log entry was created.')),
            ],
        ),
        migrations.RemoveField(
            model_name='sessionslist',
            name='connected_user',
        ),
        migrations.RemoveField(
            model_name='sessionslist',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='sessionslist',
            name='session_closed',
        ),
        migrations.AddField(
            model_name='notesdata',
            name='session',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notes', to='terminal.sessionslist'),
        ),
        migrations.AddField(
            model_name='notesdata',
            name='session_master',
            field=models.ForeignKey(blank=True, help_text='The user who created the session.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sessionslist',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Flag indicating if the session is active.'),
        ),
        migrations.AddField(
            model_name='sshdata',
            name='session',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ssh_sessions', to='terminal.sessionslist'),
        ),
        migrations.AddField(
            model_name='sshdata',
            name='session_master',
            field=models.ForeignKey(blank=True, help_text='The user who created the session.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sessionslist',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='notesdata',
            name='logs',
            field=models.ManyToManyField(blank=True, help_text='Logs related to this data.', related_name='%(class)s_logs', to='terminal.log'),
        ),
        migrations.AddField(
            model_name='sshdata',
            name='logs',
            field=models.ManyToManyField(blank=True, help_text='Logs related to this data.', related_name='%(class)s_logs', to='terminal.log'),
        ),
    ]
