# Generated by Django 4.2.5 on 2023-10-30 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DM_Head', '0007_clientregister_work_reg_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadField_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('task_discription', models.TextField(blank=True, default='', null=True)),
                ('field_add_time', models.TimeField(auto_now_add=True, null=True)),
                ('field_status', models.IntegerField(default=0)),
                ('field_add_date', models.DateField(auto_now=True, null=True)),
                ('field_clientId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.clientregister')),
                ('field_work_regId', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='DM_Head.workregister')),
            ],
        ),
    ]