# Generated by Django 3.2.5 on 2022-08-15 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0013_alter_recipe_recipe_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=128),
        ),
    ]
