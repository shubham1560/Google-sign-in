# Generated by Django 2.2.2 on 2020-05-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemproperties',
            name='id',
            field=models.IntegerField(default=1567, primary_key=True, serialize=False),
        ),
    ]
