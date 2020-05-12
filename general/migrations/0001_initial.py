# Generated by Django 3.0.6 on 2020-05-12 01:59

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
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('MAT', 'Mathematics'), ('ENG', 'English'), ('PHY', 'Physics')], max_length=3)),
                ('price', models.PositiveIntegerField()),
                ('ad_type', models.CharField(choices=[('T', 'TEACH'), ('L', 'LEARN')], max_length=1)),
                ('is_availible', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('MAT', 'Mathematics'), ('ENG', 'English'), ('PHY', 'Physics')], max_length=3)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_ad', to='general.Ad')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
