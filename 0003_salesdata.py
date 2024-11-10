# Generated by Django 5.1.3 on 2024-11-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_expenses_amount_remove_expenses_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('sales', models.IntegerField()),
            ],
            options={
                'db_table': 'sales_data2',
            },
        ),
    ]
