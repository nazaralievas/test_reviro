# Generated by Django 3.2.16 on 2024-03-26 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='establishment',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='establishment',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
