# Generated by Django 4.2 on 2023-05-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_hashtag_comment_created_at_blog_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
    ]
