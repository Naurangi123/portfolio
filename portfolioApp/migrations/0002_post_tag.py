# Generated by Django 5.0.4 on 2024-04-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='portfolioApp.tag'),
        ),
    ]