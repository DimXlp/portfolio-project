# Generated by Django 2.2.6 on 2019-11-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='title', max_length=50),
            preserve_default=False,
        ),
    ]
