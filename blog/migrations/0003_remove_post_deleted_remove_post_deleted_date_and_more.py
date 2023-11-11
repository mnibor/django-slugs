# Generated by Django 4.2.6 on 2023-11-10 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_category_options_post_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='post',
            name='deleted_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]
