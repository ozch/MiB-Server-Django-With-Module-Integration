# Generated by Django 2.1.7 on 2019-03-31 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackgroundJobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkportscanner',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='networksnifferscanner',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
