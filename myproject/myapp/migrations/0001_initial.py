# Generated by Django 4.2.8 on 2023-12-22 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('SSN', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('CusLastName', models.CharField(max_length=255)),
                ('CusFirstName', models.CharField(max_length=255)),
                ('CusMiddName', models.CharField(blank=True, max_length=255, null=True)),
                ('CustSuffix', models.CharField(blank=True, max_length=50, null=True)),
                ('CusDOB', models.DateField()),
                ('CustSalutation', models.CharField(blank=True, max_length=50, null=True)),
                ('CustEmailAddress', models.CharField(blank=True, max_length=255, null=True)),
                ('Gender', models.BooleanField(null=True)),
                ('CustomerLegacyID', models.IntegerField(null=True)),
                ('WithholdingCode', models.IntegerField(null=True)),
                ('StartDate', models.DateField(null=True)),
                ('EndDate', models.DateField(null=True)),
                ('CustomerAliasName', models.CharField(blank=True, max_length=255, null=True)),
                ('CustomerAddressID', models.IntegerField(null=True)),
                ('DocumentID', models.IntegerField(null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Heredity', models.BooleanField(null=True)),
                ('Income', models.IntegerField(null=True)),
                ('InsufficientPhysicalExercises', models.BooleanField(null=True)),
                ('SmokingAndDrinking', models.BooleanField(null=True)),
                ('BurnTheMidnightOil', models.BooleanField(null=True)),
                ('UnhealthyEatingHabit', models.BooleanField(null=True)),
                ('UnstableEmotionStatus', models.BooleanField(null=True)),
                ('TypicalChronicDiseases', models.CharField(blank=True, max_length=255, null=True)),
                ('CustCountry', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('CustomerAddressID', models.AutoField(primary_key=True, serialize=False)),
                ('CustAddress', models.CharField(max_length=255)),
                ('CustCity', models.CharField(max_length=100)),
                ('CustState', models.CharField(max_length=100)),
                ('CustZip', models.CharField(max_length=20)),
                ('AnnualStartDate', models.DateField(null=True)),
                ('AnnualEndDate', models.DateField(null=True)),
                ('SSN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
