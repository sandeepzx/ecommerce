# Generated by Django 5.0.7 on 2024-07-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_student_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Pro_Desc',
            field=models.TextField(null=True),
        ),
    ]
