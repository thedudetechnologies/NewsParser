# Generated by Django 2.2.7 on 2019-11-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsenews', '0002_auto_20191119_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='nid',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='published',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(),
        ),
    ]
