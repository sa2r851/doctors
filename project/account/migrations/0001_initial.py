# Generated by Django 4.0.3 on 2022-03-29 22:35

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='sep_choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=20, verbose_name='التخصصات')),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default='doctor.png', upload_to='')),
                ('name', models.CharField(max_length=50, verbose_name='الاسم:')),
                ('who_i', models.TextField(max_length=250, verbose_name='عن الطبيب')),
                ('education', models.TextField(default='دكتور', max_length=100, verbose_name='المؤهلات العلميه')),
                ('price', models.IntegerField(default=0, verbose_name='سعر الكشف')),
                ('address3', models.TextField(default='عنوان العياده', max_length=100, verbose_name='العنوان')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('اسانسير', 'اسانسير'), ('شاشه', 'شاشة'), ('نكييف', 'تكييف')], max_length=18, null=True)),
                ('gender', models.CharField(blank=True, choices=[('دكتور', 'دكتور'), ('دكتورة', 'دكتورة'), ('مستشفي', 'مستشفي')], max_length=10, null=True)),
                ('daywork', multiselectfield.db.fields.MultiSelectField(choices=[('السبت', 'السبت'), ('الاحد', 'الاحد'), ('الاثنين', 'الاثنين'), ('الثلاثاء', 'الثلاثاء'), ('الاربعاء', 'الاربعاء'), ('الخميس', 'الخميس'), ('الجمعه', 'الجمعه')], max_length=51, null=True)),
                ('hourwork', models.TextField(max_length=50, null=True, verbose_name='مواعيد العمل')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('Specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sp_doctor', to='account.sep_choice')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.country'),
        ),
    ]
