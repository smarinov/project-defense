# Generated by Django 3.1.4 on 2020-12-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='devices')),
                ('description', models.TextField(max_length=500)),
                ('type', models.CharField(choices=[('smartphone', 'Smartphone'), ('tablet', 'Tablet'), ('laptop', 'Laptop')], max_length=10)),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('storage_capacity', models.IntegerField()),
                ('ram', models.IntegerField()),
                ('cpu_speed', models.FloatField()),
                ('os', models.CharField(max_length=50)),
                ('price', models.FloatField()),
            ],
        ),
    ]
