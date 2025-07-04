# Generated by Django 5.1.7 on 2025-05-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_todoapp_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoapp',
            name='gender',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='todoapp',
            name='place',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='todoapp',
            name='position',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='todoapp',
            name='age',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
