# Generated by Django 4.0.6 on 2022-07-16 09:07

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindori',
            name='what_can_drug_doru',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now, verbose_name='Ruscha: Farmakoterapeftik guruhi:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maindori',
            name='what_can_drug_do',
            field=ckeditor.fields.RichTextField(verbose_name='Farmakoterapeftik guruhi:'),
        ),
    ]
