# Generated by Django 3.1.1 on 2020-09-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author', fields=[
                ('author_id', models.AutoField(
                    editable=False, primary_key=True, serialize=False)), ('name', models.CharField(
                        max_length=255)), ], ), ]
