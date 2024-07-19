# Generated by Django 5.0.6 on 2024-07-07 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_item_address_remove_item_blood_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='middlena_me',
            new_name='middle_name',
        ),
        migrations.AddField(
            model_name='item',
            name='agency_employee_no',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='blood_type',
            field=models.CharField(default='O', max_length=3),
        ),
        migrations.AddField(
            model_name='item',
            name='citizenship',
            field=models.CharField(default='Filipino', max_length=50),
        ),
        migrations.AddField(
            model_name='item',
            name='civil_status',
            field=models.CharField(default='Single', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='date_of_birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='item',
            name='email_address',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='item',
            name='fathers_name',
            field=models.CharField(default='Unknown Father', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='gsis_id_no',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='height',
            field=models.FloatField(default=1.7),
        ),
        migrations.AddField(
            model_name='item',
            name='mobile_no',
            field=models.CharField(default='09000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='mothers_name',
            field=models.CharField(default='Unknown Mother', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='pagibig_id_no',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='permanent_address',
            field=models.CharField(default='123 Main St', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='philhealth_no',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='place_of_birth',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='residential_address',
            field=models.CharField(default='123 Main St', max_length=255),
        ),
        migrations.AddField(
            model_name='item',
            name='sex',
            field=models.CharField(default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='item',
            name='sss_no',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='telephone_no',
            field=models.CharField(default='0000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='tin_no',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.FloatField(default=70.0),
        ),
        migrations.AddField(
            model_name='item',
            name='zip_code',
            field=models.CharField(default='1000', max_length=10),
        ),
    ]