# Generated by Django 2.0.1 on 2018-01-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_file_last_output'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='extension',
            field=models.TextField(blank=True, null=True),
        ),
    ]