# Generated by Django 4.2.3 on 2023-11-07 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Telecaller', '0002_leads_assignto_tc_client_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leads_assignto_tc',
            name='Record',
        ),
        migrations.CreateModel(
            name='Leads_Call_Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record', models.FileField(default='', upload_to='record')),
                ('Leads_assignto_tc_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Telecaller.leads_assignto_tc')),
            ],
        ),
    ]
