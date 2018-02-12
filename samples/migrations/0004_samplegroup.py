# Generated by Django 2.0.1 on 2018-01-31 21:55
# Generated by Django 2.0.1 on 2018-01-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0003_sample_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('members', models.ManyToManyField(related_name='samplegroup_members', to='samples.Sample')),
            ],
        ),
    ]