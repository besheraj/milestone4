# Generated by Django 3.1.2 on 2020-11-14 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20201114_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='service_name',
            new_name='service_id',
        ),
    ]
