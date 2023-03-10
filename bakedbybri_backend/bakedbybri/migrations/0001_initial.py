# Generated by Django 4.1.5 on 2023-01-12 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='A Baked By Bri Recipe', max_length=100)),
                ('duration', models.DurationField()),
                ('category', models.CharField(default='', max_length=100)),
                ('author', models.ForeignKey(default='Bri', on_delete=django.db.models.deletion.CASCADE, related_name='Author', to=settings.AUTH_USER_MODEL)),
                ('ingredients', models.ManyToManyField(blank=True, related_name='ingredients', to='bakedbybri.ingredients')),
            ],
        ),
    ]
