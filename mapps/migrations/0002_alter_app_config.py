# Generated by Django 4.2.5 on 2023-09-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='config',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
