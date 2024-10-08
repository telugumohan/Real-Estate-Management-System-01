# Generated by Django 4.2.6 on 2023-11-04 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_city_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_picture',
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('property_title', models.CharField(max_length=200)),
                ('property_description', models.TextField()),
                ('property_type', models.CharField(max_length=50)),
                ('property_category', models.CharField(choices=[('luxury', 'Luxury Estate'), ('oceanfront', 'Oceanfront Retreats'), ('urban', 'Urban Living Gems'), ('countryside', 'Countryside Escapes')], default='luxury', max_length=20)),
                ('property_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('property_location', models.CharField(max_length=100)),
                ('property_features', models.TextField(blank=True, null=True)),
                ('seller_name', models.CharField(max_length=100)),
                ('seller_email', models.EmailField(max_length=254)),
                ('seller_phone', models.CharField(max_length=15)),
                ('property_images', models.ImageField(blank=True, null=True, upload_to='property_images/')),
                ('approved', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='agent_properties', to='users.userprofile')),
            ],
        ),
    ]
