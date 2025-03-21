# Generated by Django 5.1.6 on 2025-03-07 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('execution_date', models.DateField()),
                ('problem_description', models.TextField()),
                ('code_request', models.AutoField(primary_key=True, serialize=False)),
                ('code_type_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.typework')),
                ('id_needy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.needy')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id_service', models.AutoField(primary_key=True, serialize=False)),
                ('execution_date', models.DateField()),
                ('code_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.request')),
                ('id_volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.volunteer')),
            ],
        ),
    ]
