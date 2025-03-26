# Generated by Django 5.1.7 on 2025-03-23 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaidCafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='maid_cafes/')),
            ],
        ),
        migrations.CreateModel(
            name='Maid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='maids/')),
                ('cafe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maids', to='maid_cafe.maidcafe')),
            ],
        ),
    ]
