# Generated by Django 4.1.7 on 2023-04-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('sec_file', models.FileField(upload_to='sec_file/%Y/%m/%d/')),
            ],
        ),
    ]
