# Generated by Django 5.1 on 2024-08-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(default='Yet to Start', max_length=100),
        ),
    ]
