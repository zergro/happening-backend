# Generated by Django 4.0.5 on 2022-07-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, choices=[('Smiles', 'Smiles'), ('Laughter', 'Laughter'), ('Crazy', 'Crazy'), ('Food', 'Food'), ('Outside', 'Outside')], max_length=200, null=True),
        ),
    ]
