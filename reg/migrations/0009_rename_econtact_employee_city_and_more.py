# Generated by Django 4.0.6 on 2022-07-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0008_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='econtact',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='ename',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='eid',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
