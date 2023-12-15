# Generated by Django 4.2.5 on 2023-12-14 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('terminal', '0005_log_remove_sessionslist_connected_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SavedHosts',
            new_name='SavedHost',
        ),
        migrations.AlterField(
            model_name='sessionslist',
            name='content_type',
            field=models.ForeignKey(limit_choices_to={'model__in': ['sshdata', 'notesdata']}, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]