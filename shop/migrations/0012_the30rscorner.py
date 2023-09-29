# Generated by Django 4.2 on 2023-05-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_combos'),
    ]

    operations = [
        migrations.CreateModel(
            name='The30RsCorner',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
                ('product_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=400)),
                ('category', models.CharField(default='', max_length=50)),
                ('price', models.CharField(max_length=30)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
