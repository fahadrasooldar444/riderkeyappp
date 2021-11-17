# Generated by Django 3.2.7 on 2021-09-27 08:21

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Designations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('department_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('created_by', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'designations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SalaryStructures',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('hourly_rate', models.CharField(max_length=255)),
                ('per_drop', models.CharField(blank=True, max_length=256, null=True)),
                ('houry_rate_temp', models.CharField(blank=True, max_length=256, null=True)),
                ('delivery_rate', models.CharField(max_length=255)),
                ('extra_per_utr', models.CharField(blank=True, max_length=45, null=True)),
                ('per_km', models.CharField(blank=True, max_length=45, null=True)),
                ('long_distance_1', models.CharField(blank=True, max_length=45, null=True)),
                ('long_distance_2', models.CharField(blank=True, max_length=45, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('overtime_rate', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'salary_structures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('team_leader', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountCategories',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'account_categories',
            },
        ),
        # migrations.CreateModel(
        #     name='Employees',
        #     fields=[
        #         ('id', models.BigAutoField(primary_key=True, serialize=False)),
        #         ('name', models.CharField(max_length=255)),
        #         ('email', models.CharField(blank=True, max_length=255, null=True)),
        #         ('verified', models.CharField(choices=[('no', 'No'), ('IBAN Verified', 'IBAN Verified')], default='No', max_length=255)),
        #         ('status', models.CharField(choices=[('Active', 'Active'), ('inactive', 'Inactive'), ('Salary Suspended', 'Salary Suspended'), ('Terminated', 'Terminated'), ('vacation', 'Vacation')], default='Active', max_length=255)),
        #         ('bank_type', models.CharField(blank=True, choices=[('Bank', 'Bank'), ('TAM', 'TAM')], max_length=45, null=True)),
        #         ('contact_numer', models.CharField(blank=True, max_length=255, null=True)),
        #         ('cpr', models.CharField(max_length=255, unique=True)),
        #         ('talabat_id', models.CharField(max_length=255, unique=True)),
        #         ('type', models.CharField(blank=True, max_length=255, null=True)),
        #         ('branch_id', models.IntegerField(blank=True, null=True)),
        #         ('visa', models.CharField(blank=True, choices=[('Flexi Visa', 'Flexi Visa'), ('notflexi', 'Not Flexi'), ('KA Visa', 'KA Visa'), ('Free Visa', 'Free Visa')], max_length=255, null=True)),
        #         ('visa_expiry_date', models.DateField(blank=True, null=True)),
        #         ('contract_start', models.DateField(blank=True, null=True)),
        #         ('contract_end', models.DateField(blank=True, null=True)),
        #         ('joining_date', models.DateField(blank=True, null=True)),
        #         ('vehicle_type', models.CharField(blank=True, choices=[('Car', 'Car'), ('Bike', 'Bike'), ('Motorbike', 'Motorbike'), ('Motor', 'Motor'), ('HATCHBACK', 'HATCHBACK')], max_length=255, null=True)),
        #         ('vehicle_number', models.CharField(blank=True, max_length=255, null=True)),
        #         ('vehicle_make_model', models.CharField(blank=True, max_length=255, null=True)),
        #         ('vehicle_year', models.CharField(blank=True, max_length=255, null=True)),
        #         ('license', models.CharField(blank=True, max_length=255, null=True)),
        #         ('license_expiry_date', models.CharField(blank=True, max_length=255, null=True)),
        #         ('nationality', models.CharField(blank=True, max_length=255, null=True)),
        #         ('country', models.CharField(blank=True, choices=[('bahrain', 'Bahrain'), ('erbil', 'Erbil'), ('dubai', 'Dubai'), ('iraq', 'Iraq')], max_length=128, null=True)),
        #         ('bank_account_name', models.CharField(blank=True, max_length=255, null=True)),
        #         ('gender', models.CharField(blank=True, max_length=255, null=True)),
        #         ('cpr_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
        #         ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
        #         ('passport_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
        #         ('license_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
        #         ('visa_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
        #         ('contract_file', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
        #         ('passport_number', models.CharField(blank=True, max_length=255, null=True, unique=True)),
        #         ('passport_expiry_date', models.DateField(blank=True, null=True)),
        #         ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
        #         ('updated_at', models.DateTimeField(auto_now=True, null=True)),
        #         ('iban', models.CharField(blank=True, max_length=255, null=True)),
        #         ('cnd', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
        #         ('department_id', models.ForeignKey(blank=True, db_column='department_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='department_employees', to='employees.departments')),
        #         ('designation_id', models.ForeignKey(blank=True, db_column='designation_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='designation_employees', to='employees.designations')),
        #         ('salary_structure', models.ForeignKey(db_column='salary_structure', on_delete=django.db.models.deletion.DO_NOTHING, to='employees.salarystructures')),
        #         ('team_id', models.ForeignKey(blank=True, db_column='team_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='team_employees', to='employees.teams')),
        #         ('user_id', models.OneToOneField(db_column='user_id', db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee', to=settings.AUTH_USER_MODEL)),
        #     ],
        #     options={
        #         'db_table': 'employees',
        #     },
        # ),
        migrations.CreateModel(
            name='Timesheets',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('hours', models.CharField(max_length=255)),
                ('orders', models.CharField(blank=True, max_length=255, null=True)),
                ('utr', models.CharField(blank=True, max_length=45, null=True)),
                ('po_orders', models.CharField(max_length=256)),
                ('po_hours', models.CharField(max_length=256)),
                ('day_deduction', models.CharField(blank=True, max_length=255, null=True)),
                ('pay_per_distance', models.CharField(blank=True, max_length=45, null=True)),
                ('extra_per_utr', models.CharField(blank=True, max_length=45, null=True)),
                ('day_deduction_rate', models.CharField(blank=True, max_length=255, null=True)),
                ('double_orders', models.CharField(blank=True, max_length=255, null=True)),
                ('long_distance_sakhir', models.CharField(blank=True, max_length=45, null=True)),
                ('long_distance_durra', models.CharField(blank=True, max_length=45, null=True)),
                ('month', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employees')),
            ],
            options={
                'db_table': 'timesheets',
            },
        ),
        migrations.CreateModel(
            name='Performances',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('starting_date', models.CharField(max_length=255)),
                ('ending_date', models.CharField(max_length=255)),
                ('shift_count', models.CharField(max_length=255)),
                ('no_shows', models.CharField(max_length=255)),
                ('late_login', models.CharField(max_length=255)),
                ('completed_orders', models.CharField(max_length=255)),
                ('cancelled_orders', models.CharField(max_length=255)),
                ('cancellation_10_orders', models.CharField(max_length=255)),
                ('utr', models.CharField(max_length=255)),
                ('total_working_hours', models.CharField(max_length=255)),
                ('total_break_hours', models.CharField(max_length=255)),
                ('attendance_percentage', models.CharField(max_length=255)),
                ('breaks_percentage', models.CharField(max_length=255)),
                ('notification_count', models.CharField(max_length=255)),
                ('acceptance_count', models.CharField(max_length=255)),
                ('acceptance_rate', models.CharField(max_length=255)),
                ('avg_customer_time', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employees')),
            ],
            options={
                'db_table': 'performances',
            },
        ),
        migrations.CreateModel(
            name='Payslips',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('basic_salary', models.CharField(blank=True, max_length=45, null=True)),
                ('bonus', models.CharField(blank=True, max_length=45, null=True)),
                ('deduction', models.CharField(blank=True, max_length=45, null=True)),
                ('net_payable', models.CharField(max_length=255)),
                ('salary_month', models.CharField(max_length=255)),
                ('payroll_entry_id', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('created_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employees')),
            ],
            options={
                'db_table': 'payslips',
            },
        ),
        migrations.CreateModel(
            name='CashNds',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('previous_date', models.CharField(max_length=255)),
                ('previous_pending', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('previous_deposit', models.DecimalField(decimal_places=2, max_digits=5)),
                ('previous_balance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bonus', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('bonus_type', models.CharField(blank=True, max_length=255, null=True)),
                ('date_selected', models.CharField(max_length=255)),
                ('date_cod', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_pending', models.DecimalField(decimal_places=2, max_digits=5)),
                ('deposit_status', models.CharField(max_length=255)),
                ('deposit_delayed', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employees')),
            ],
            options={
                'db_table': 'cash_nds',
            },
        ),
        migrations.CreateModel(
            name='AccountTypes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('accounttypename', models.CharField(db_column='accountTypeName', max_length=255)),
                ('subaccount', models.IntegerField(blank=True, db_column='subAccount', null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('account_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.accountcategories')),
            ],
            options={
                'db_table': 'account_types',
            },
        ),
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=256, null=True)),
                ('balance', models.IntegerField(default=0)),
                ('holderid', models.IntegerField(db_column='holderID', default=1)),
                ('supplier_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('customer_id', models.PositiveBigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('account_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.accountcategories')),
                ('account_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.accounttypes')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employees')),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]
