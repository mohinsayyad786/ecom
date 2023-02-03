# Generated by Django 4.1.6 on 2023-02-02 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=500)),
                ('product_shape', models.CharField(max_length=50)),
                ('product_size', models.CharField(max_length=500)),
                ('product_location', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=500)),
                ('is_deleted', models.CharField(max_length=10)),
            ],
        ),
    ]