# Generated by Django 4.0.6 on 2022-07-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0006_rename_sr_no_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]