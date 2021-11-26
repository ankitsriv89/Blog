# Generated by Django 3.2.6 on 2021-08-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date']},
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='created',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='publish',
            new_name='publish_date',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish_date'),
        ),
    ]
