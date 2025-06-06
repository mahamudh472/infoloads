# Generated by Django 5.2 on 2025-05-04 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apps', to='downloads.category'),
        ),
        migrations.AddField(
            model_name='app',
            name='language',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='license',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='os',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='app',
            name='platform',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
