# Generated by Django 3.2.2 on 2021-06-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogcomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
