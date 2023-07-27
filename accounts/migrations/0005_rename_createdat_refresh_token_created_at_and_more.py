# Generated by Django 4.2.3 on 2023-07-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_refresh_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refresh_token',
            old_name='createdAt',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='refresh_token',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
