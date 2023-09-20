# Generated by Django 4.2.5 on 2023-09-17 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_type_employee_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='categ',
            field=models.ManyToManyField(to='erp.category'),
        ),
    ]
