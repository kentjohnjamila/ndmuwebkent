# Generated by Django 2.1.3 on 2018-12-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ndmu', '0002_remove_comment_author_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
    ]