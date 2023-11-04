from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Cодержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts/', verbose_name='Изображение')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_change_date', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('is_published', models.BooleanField(verbose_name='Признак публикации')),
                ('paid_published', models.BooleanField(default=False, verbose_name='Платная публикация')),
                ('cost', models.IntegerField(default=100, verbose_name='Цена подписки')),
                ('count_views', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('count_pay', models.IntegerField(default=0, verbose_name='Количество покупок')),
            ],

            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-create_date'],
            },
        ),
    ]
