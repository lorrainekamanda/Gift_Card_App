# Generated by Django 4.1.4 on 2022-12-10 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0005_alter_wishlist_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftapp.productcategory'),
        ),
    ]