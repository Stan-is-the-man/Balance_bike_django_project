# Generated by Django 4.1.3 on 2022-11-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_order_alter_balancebike_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='balancebike',
            name='model',
            field=models.CharField(choices=[('Класик', 'Classic')], max_length=15),
        ),
    ]
