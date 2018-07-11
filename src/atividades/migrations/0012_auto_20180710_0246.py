# Generated by Django 2.0.6 on 2018-07-10 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0011_auto_20180601_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='senha',
            new_name='password',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='em_equipe',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='exemplo@exemplo.com', max_length=120, unique=True),
        ),
    ]
