# Generated by Django 5.2 on 2025-07-31 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0012_remove_download_app_download_app_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='app_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloads', to='downloads.appversion'),
        ),
    ]
