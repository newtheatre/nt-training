# Generated by Django 2.2.4 on 2019-08-27 08:05

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('nt_training', '0005_auto_20190827_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site_Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(max_length=25)),
                ('weight', models.IntegerField()),
                ('primary', models.BooleanField(default=False)),
                ('viewName', models.CharField(max_length=25)),
            ],
        ),
        migrations.RenameModel(
            old_name='Icon',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['weight'], 'verbose_name': 'Training Category', 'verbose_name_plural': 'Training Categories'},
        ),
    ]
