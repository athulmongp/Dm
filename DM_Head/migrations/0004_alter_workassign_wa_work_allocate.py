# Generated by Django 4.2.5 on 2023-10-20 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0001_initial'),
        ('DM_Head', '0003_workregister_allocated_emp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workassign',
            name='wa_work_allocate',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='allocated_tl', to='Registration_Login.employeeregister_details'),
        ),
    ]
