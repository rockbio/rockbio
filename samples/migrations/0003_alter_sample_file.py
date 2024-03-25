# Generated by Django 4.2.6 on 2023-10-25 14:40

from django.db import migrations, models
import samples.models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0002_sample_description_sample_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='file',
            field=models.FileField(blank=True, max_length=600, upload_to=samples.models.Sample.get_upload_path),
        ),
    ]