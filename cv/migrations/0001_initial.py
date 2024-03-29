# Generated by Django 5.0 on 2024-01-19 19:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('school', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('is_key_education', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('period_from', models.CharField(max_length=50)),
                ('period_to', models.CharField(max_length=50)),
                ('is_key_expertise', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Expertise',
                'verbose_name_plural': 'Expertise',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_image', models.ImageField(blank=True, null=True, upload_to='portfolio_image')),
                ('project_name', models.CharField(max_length=100)),
                ('period_done', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Webinar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_name', models.CharField(max_length=100)),
                ('date_conducted', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('alt_emails', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('alt_phone_number', models.CharField(blank=True, max_length=100)),
                ('git_hub_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('facebook_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('language', models.CharField(blank=True, max_length=50)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
