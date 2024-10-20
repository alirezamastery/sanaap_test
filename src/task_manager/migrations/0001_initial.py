# Generated by Django 4.2.16 on 2024-10-19 11:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('RUNNING', 'Running'), ('FAILED', 'Failed'), ('COMPLETED', 'Completed')], default='PENDING')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
