# Generated by Django 2.1.1 on 2018-10-21 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_group', '0004_auto_20181020_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomgroup',
            name='members',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='create_group.myCustomUsers'),
        ),
        migrations.AlterField(
            model_name='mycustomusers',
            name='user_address',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='mycustomusers',
            name='user_email',
            field=models.EmailField(max_length=128),
        ),
        migrations.AlterField(
            model_name='mycustomusers',
            name='user_exclusions',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='mycustomusers',
            name='user_phone',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='mycustomusers',
            name='user_status',
            field=models.CharField(max_length=128),
        ),
    ]