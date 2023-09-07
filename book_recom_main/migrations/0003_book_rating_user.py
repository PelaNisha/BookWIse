# Generated by Django 4.2 on 2023-09-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_recom_main', '0002_remove_user_data_id_alter_user_data_book_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Title', models.CharField(max_length=255)),
                ('Book_Author', models.CharField(max_length=255)),
                ('Year_Of_Publication', models.IntegerField()),
                ('Publisher', models.CharField(max_length=255)),
                ('Image_URL_S', models.URLField()),
                ('Image_URL_M', models.URLField()),
                ('Image_URL_L', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.IntegerField()),
                ('ISBN', models.CharField(max_length=13)),
                ('Book_Rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Location', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
            ],
        ),
    ]
