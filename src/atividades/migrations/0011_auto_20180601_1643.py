# Generated by Django 2.0.4 on 2018-06-01 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0010_atividade_trofeu3'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atividade',
            name='trofeu1',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='trofeu2',
        ),
        migrations.RemoveField(
            model_name='atividade',
            name='trofeu3',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AddField(
            model_name='atividade',
            name='trofeu',
            field=models.IntegerField(choices=[(3, 'Bronze'), (5, 'Prata'), (7, 'Ouro')], default=1),
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='exemplo@exemplo.com', max_length=120),
        ),
        migrations.AddField(
            model_name='usuario',
            name='instituicao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Trofeu',
        ),
    ]
