# Generated by Django 5.1.1 on 2024-09-05 14:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_social'),
        ('education', '0004_alter_direction_faculty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('passport', models.CharField(max_length=9)),
                ('pinfl', models.CharField(max_length=14)),
                ('gender', models.CharField(choices=[('male', 'Erkak'), ('female', 'Ayol')], max_length=6)),
                ('birth_date', models.DateField()),
                ('status', models.CharField(choices=[('accepted', 'Qabul qilindi'), ('rejected', 'Rad etildi'), ('pending', 'Kutilmoqda')], default='pending', max_length=16)),
                ('accepted_at', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('contract_url', models.CharField(max_length=255)),
                ('direction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='education.direction')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.district')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
