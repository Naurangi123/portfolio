# Generated by Django 5.0.4 on 2024-04-07 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0002_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='first_name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='last_name',
            new_name='l_name',
        ),
    ]
