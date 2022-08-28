# Generated by Django 3.2.5 on 2022-08-14 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0008_auto_20220813_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='source',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='IngredientAlias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aliases', to='playground.ingredient')),
            ],
        ),
    ]
