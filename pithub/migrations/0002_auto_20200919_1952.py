# Generated by Django 3.1.1 on 2020-09-19 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pithub', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время получения')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pithub.profile', verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
