# Generated by Django 3.1.13 on 2021-09-06 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210825_1458'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('title',), 'permissions': [('special_status', 'Can read all books')], 'verbose_name': 'Book', 'verbose_name_plural': 'Books 📚'},
        ),
    ]
