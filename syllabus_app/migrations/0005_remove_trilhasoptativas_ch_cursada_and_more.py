# Generated by Django 4.2.6 on 2023-10-24 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_app', '0004_alter_aluno_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trilhasoptativas',
            name='ch_cursada',
        ),
        migrations.RemoveField(
            model_name='trilhasoptativas',
            name='ch_faltando',
        ),
        migrations.RemoveField(
            model_name='trilhasoptativas',
            name='ch_validada',
        ),
    ]