# Generated by Django 4.1.3 on 2022-11-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Обработва се...', 'Обработва се...'), ('Изпратена', 'Изпратена'), ('Доставена', 'Доставена'), ('Отказана', 'Отказана')], default='Обработва се...', max_length=50),
        ),
    ]
