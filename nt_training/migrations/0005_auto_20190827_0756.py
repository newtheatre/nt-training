# Generated by Django 2.2.4 on 2019-08-27 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nt_training', '0004_auto_20190504_2029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icon',
            options={'ordering': ['weight']},
        ),
        migrations.RemoveField(
            model_name='icon',
            name='itemType',
        ),
        migrations.RemoveField(
            model_name='icon',
            name='primary',
        ),
        migrations.RemoveField(
            model_name='icon',
            name='viewName',
        ),
    ]
