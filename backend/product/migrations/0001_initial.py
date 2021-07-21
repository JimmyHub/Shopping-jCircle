# Generated by Django 3.1.7 on 2021-06-01 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30, verbose_name='商品名稱')),
                ('pkind', models.CharField(max_length=30, verbose_name='商品種類')),
                ('pphoto', models.ImageField(upload_to='product/', verbose_name='商品圖片')),
                ('pcontent', models.TextField(verbose_name='商品內容')),
                ('pprice', models.IntegerField(verbose_name='商品金額')),
                ('pway', models.IntegerField(verbose_name='付款方式')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
