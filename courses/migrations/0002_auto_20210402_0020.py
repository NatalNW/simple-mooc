# Generated by Django 3.1.7 on 2021-04-02 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='courses/images',
                verbose_name='Image',
            ),
        ),
    ]
