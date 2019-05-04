# Generated by Django 2.2 on 2019-05-04 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nt_training', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Department Name')),
                ('person', models.CharField(help_text='Person in charge of the department', max_length=50)),
                ('email', models.EmailField(help_text='Email address of the person in charge', max_length=254)),
                ('weight', models.IntegerField(unique=True)),
                ('department_icon', models.CharField(default='fa fa-', help_text='From <a href="https://fontawesome.com/icons?d=gallery&m=free">Font Awesome 5</a>. Example: <code>fas fa-user</code>.', max_length=25, verbose_name='Icon Code')),
            ],
            options={
                'ordering': ['weight'],
            },
        ),
        migrations.AlterModelOptions(
            name='icon',
            options={'ordering': ['itemType', 'weight']},
        ),
        migrations.AlterModelOptions(
            name='training_session',
            options={'verbose_name': 'Training Session'},
        ),
        migrations.AlterModelOptions(
            name='training_spec',
            options={'ordering': ['category', 'trainingId'], 'verbose_name': 'Training Specification'},
        ),
        migrations.AddField(
            model_name='person',
            name='is_trainer',
            field=models.BooleanField(default=False, help_text='Tick if this person trains others.'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='iconName',
            field=models.CharField(max_length=25, verbose_name='Icon Name'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='iconRef',
            field=models.CharField(help_text='From <a href="https://fontawesome.com/icons?d=gallery&m=free">Font Awesome 5</a>. Example: <code>fas fa-user</code>.', max_length=25, verbose_name='Icon Code'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='primary',
            field=models.BooleanField(default=False, help_text='For pages only. Tick to appear on the homepage.'),
        ),
        migrations.AlterField(
            model_name='icon',
            name='viewName',
            field=models.CharField(blank=True, default=None, help_text='For pages only.', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='training_spec',
            name='category',
            field=models.ForeignKey(limit_choices_to={'itemType': 'CAT'}, on_delete=django.db.models.deletion.DO_NOTHING, to='nt_training.Icon'),
        ),
        migrations.AlterField(
            model_name='training_spec',
            name='safety',
            field=models.BooleanField(default=False, help_text='Tick if training point has a health and safety element, or requires a period of supervision before signing off.'),
        ),
        migrations.AlterField(
            model_name='training_spec',
            name='trainingTitle',
            field=models.CharField(max_length=50, verbose_name='Training Title'),
        ),
        migrations.AddField(
            model_name='icon',
            name='department',
            field=models.ForeignKey(blank=True, help_text="Department this category belongs to. If you're using departments, you <strong>must</strong> set this for the category to appear.", null=True, on_delete=django.db.models.deletion.SET_NULL, to='nt_training.Department'),
        ),
    ]
