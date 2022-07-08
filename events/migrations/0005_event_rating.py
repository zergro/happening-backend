# Generated by Django 4.0.5 on 2022-07-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_unique_together_alter_event_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='rating',
            field=models.CharField(blank=True, choices=[('Great choice', 'Great choice'), ('Fun for the whole family', 'Fun for the whole family')], max_length=200, null=True),
        ),
    ]
