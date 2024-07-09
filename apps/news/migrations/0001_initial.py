# Generated by Django 4.2 on 2024-07-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Sarlavha')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_pictures/%B/')),
                ('body', models.TextField(blank=True, null=True, verbose_name='1 - Qism')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='post_pictures/%B/')),
                ('body2', models.TextField(blank=True, null=True, verbose_name='2 - Qism')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': 'Yangiliklar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='product_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Maxsulot',
                'verbose_name_plural': 'Maxsulotlar',
            },
        ),
    ]
