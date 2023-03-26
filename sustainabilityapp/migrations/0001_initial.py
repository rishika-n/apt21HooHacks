# Generated by Django 4.1.7 on 2023-03-26 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(max_length=1000)),
                ('ch1', models.CharField(max_length=1000)),
                ('ch2', models.CharField(max_length=1000)),
                ('ch3', models.CharField(max_length=1000)),
                ('ch4', models.CharField(max_length=1000)),
                ('ch5', models.CharField(max_length=1000)),
                ('ch6', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(default='Alex', max_length=200)),
                ('last_name', models.CharField(default='Smith', max_length=200)),
                ('daily_progress', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('ch1Complete', models.BooleanField(default=False)),
                ('ch2Complete', models.BooleanField(default=False)),
                ('ch3Complete', models.BooleanField(default=False)),
                ('ch4Complete', models.BooleanField(default=False)),
                ('ch5Complete', models.BooleanField(default=False)),
                ('ch6Complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('users1', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender1', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
