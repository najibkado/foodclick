# Generated by Django 3.2.7 on 2021-11-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_entity_giveaway_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nin',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
