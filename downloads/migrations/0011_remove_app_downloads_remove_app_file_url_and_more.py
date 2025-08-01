# Generated by Django 5.2 on 2025-07-30 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloads', '0010_appimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='downloads',
        ),
        migrations.RemoveField(
            model_name='app',
            name='file_url',
        ),
        migrations.RemoveField(
            model_name='app',
            name='mod',
        ),
        migrations.RemoveField(
            model_name='app',
            name='size',
        ),
        migrations.RemoveField(
            model_name='app',
            name='version',
        ),
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_name', models.CharField(max_length=100)),
                ('version_code', models.IntegerField()),
                ('is_mod', models.BooleanField(default=False)),
                ('file_url', models.URLField()),
                ('size', models.CharField(max_length=20)),
                ('changelog', models.TextField(blank=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('log_url', models.URLField(blank=True, null=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='downloads.app')),
                ('original_version', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mod_variants', to='downloads.appversion')),
            ],
            options={
                'ordering': ['-version_code'],
                'unique_together': {('app', 'version_code', 'is_mod')},
            },
        ),
    ]
