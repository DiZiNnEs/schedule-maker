# Generated by Django 3.2.3 on 2021-05-17 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0003_alter_task_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chief',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='chief_of_category',
            field=models.ForeignKey(default=1, help_text='Chief of category', on_delete=django.db.models.deletion.CASCADE, to='schedule_app.chief'),
            preserve_default=False,
        ),
    ]