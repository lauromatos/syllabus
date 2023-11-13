# Generated by Django 4.2.6 on 2023-10-24 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('Departamento', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome_departamento', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['Departamento', 'nome_departamento'],
            },
        ),
        migrations.RemoveField(
            model_name='curso',
            name='setor',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='setor',
        ),
        migrations.DeleteModel(
            name='Setor',
        ),
        migrations.AddField(
            model_name='curso',
            name='Departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='syllabus_app.departamento'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='Departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='syllabus_app.departamento'),
        ),
    ]