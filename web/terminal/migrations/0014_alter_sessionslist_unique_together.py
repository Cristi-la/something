# Generated by Django 4.2.5 on 2024-01-02 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('terminal', '0013_notesdata_name_sshdata_name_alter_sessionslist_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sessionslist',
            unique_together={('user', 'content_type', 'object_id')},
        ),
    ]
