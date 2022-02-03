# Generated by Django 4.0.1 on 2022-02-03 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_booking_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Busi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=25)),
                ('image', models.ImageField(default='bus.jpg', upload_to='bus_pics')),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_no', models.IntegerField(default=1)),
                ('bus_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.bus')),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.route')),
            ],
        ),
    ]
