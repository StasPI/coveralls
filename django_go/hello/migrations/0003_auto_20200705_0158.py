# Generated by Django 3.0.7 on 2020-07-04 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20200704_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothingSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing_size', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='staff',
            name='email_adress',
        ),
        migrations.CreateModel(
            name='TypeOfClothing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_clothing', models.CharField(max_length=100)),
                ('clothing_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.ClothingSize')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=200)),
                ('article', models.CharField(max_length=200)),
                ('operational_life_in_months', models.PositiveSmallIntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.Supplier')),
                ('type_of_clothing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello.TypeOfClothing')),
            ],
        ),
    ]
