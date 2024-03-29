# Generated by Django 4.0.5 on 2022-07-08 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(blank=True, choices=[('Publish', 'Publish'), ('Draft', 'Draft')], max_length=200, null=True),
        ),
    ]
