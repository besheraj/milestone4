# Generated by Django 3.1.2 on 2020-11-16 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20201116_0437'),
        ('checkout', '0006_auto_20201114_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='service_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='services.service'),
        ),
    ]
