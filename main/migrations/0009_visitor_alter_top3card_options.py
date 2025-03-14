# Generated by Django 5.1.6 on 2025-03-10 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_top3card_alter_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.CharField(blank=True, max_length=500, null=True)),
                ('path', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('visit_count', models.PositiveIntegerField(default=1)),
                ('last_visit', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Visitante',
                'verbose_name_plural': 'Visitantes',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterModelOptions(
            name='top3card',
            options={'ordering': ['created_at'], 'verbose_name': 'TOP 3 Card', 'verbose_name_plural': 'TOP 3 Cards'},
        ),
    ]
