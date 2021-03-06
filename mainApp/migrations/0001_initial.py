# Generated by Django 3.0.4 on 2020-05-11 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('biographi', models.CharField(max_length=500, verbose_name='Биография')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book', models.CharField(max_length=50, verbose_name='Название книги')),
                ('annotation', models.CharField(blank=True, max_length=300, verbose_name='Аннотация к книге')),
                ('publication_date', models.DateTimeField(verbose_name='Дата публицации')),
                ('image_book', models.TextField(null=True, verbose_name='Директория обложки')),
                ('authors', models.ManyToManyField(to='mainApp.Author', verbose_name='Авторы')),
            ],
        ),
        migrations.CreateModel(
            name='Book_series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_series', models.CharField(max_length=50, verbose_name='Название серии')),
                ('image_series', models.TextField(blank=True, verbose_name='Директория обложки')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_chapter', models.CharField(max_length=30, verbose_name='Название главы')),
                ('chapter_text', models.TextField(verbose_name='Содержание главы')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_genre', models.CharField(max_length=50, verbose_name='Жанр')),
            ],
        ),
        migrations.CreateModel(
            name='Image_chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_chapter_directory', models.TextField(verbose_name='Директория изображения')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=20, verbose_name='Псевдоним')),
                ('comment_text', models.CharField(max_length=300, verbose_name='Текст комментария')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Book_raiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genres_book',
            field=models.ManyToManyField(to='mainApp.Genre', verbose_name='Жанры книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainApp.Book_series'),
        ),
    ]
