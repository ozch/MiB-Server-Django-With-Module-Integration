# Generated by Django 2.1.7 on 2019-04-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Topology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopologyServer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=300, null=True)),
            ],
            options={
                'db_table': 'topology_server',
                'managed': True,
            },
        ),
    ]