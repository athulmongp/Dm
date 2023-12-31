# Generated by Django 4.2.5 on 2023-10-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_Head', '0005_taskassign_clienttask_register_task_total_progress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskassign',
            name='ta_accept_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='taskassign',
            name='ta_accept_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='taskassign',
            name='ta_target_achived',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='taskassign',
            name='ta_start_date',
            field=models.DateField(null=True),
        ),
    ]
