# Generated by Django 3.1.4 on 2020-12-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondtech_app', '0003_auto_20201205_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='color',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
