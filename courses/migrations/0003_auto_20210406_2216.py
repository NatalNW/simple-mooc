# Generated by Django 3.1.7 on 2021-04-07 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210402_0020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={
                'ordering': ['name'],
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(
                blank=True, verbose_name='About the Course'
            ),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(verbose_name='Shortcut'),
        ),
    ]
