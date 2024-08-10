# Generated by Django 5.1 on 2024-08-09 15:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0002_category_menuitem_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='inventory',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='featured',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(db_index=True, decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(db_index=True, default=0)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateField(db_index=True)),
                ('delivery_crew', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='delivery_crew', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittlelemonAPI.menuitem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('menuitem', 'user')},
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LittlelemonAPI.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('menuitem', 'order')},
            },
        ),
    ]