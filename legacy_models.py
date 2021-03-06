# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcceptanceScores(models.Model):
    id = models.BigAutoField(primary_key=True)
    score = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acceptance_scores'


class AccountCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_categories'


class AccountTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    accounttypename = models.CharField(db_column='accountTypeName', max_length=255)  # Field name made lowercase.
    subaccount = models.IntegerField(db_column='subAccount', blank=True, null=True)  # Field name made lowercase.
    account_category = models.ForeignKey(AccountCategories, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_types'


class Accounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=256, blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField()
    holderid = models.IntegerField(db_column='holderID')  # Field name made lowercase.
    account_category = models.ForeignKey(AccountCategories, models.DO_NOTHING)
    account_type = models.ForeignKey(AccountTypes, models.DO_NOTHING)
    employee = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)
    supplier_id = models.PositiveBigIntegerField(blank=True, null=True)
    customer_id = models.PositiveBigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class AttendanceScores(models.Model):
    id = models.BigAutoField(primary_key=True)
    score = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_scores'


class Banksheetdetials(models.Model):
    id = models.BigAutoField(primary_key=True)
    banksheet = models.PositiveBigIntegerField()
    account_name = models.CharField(max_length=255)
    account_id = models.CharField(max_length=45, blank=True, null=True)
    account_address = models.CharField(max_length=255, blank=True, null=True)
    iban = models.CharField(max_length=255)
    sender_name = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255)
    bene_iban = models.CharField(max_length=255, blank=True, null=True)
    branch = models.CharField(max_length=255, blank=True, null=True)
    bank_account = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sender_id_type = models.CharField(max_length=256, blank=True, null=True)
    sender_id = models.CharField(max_length=128, blank=True, null=True)
    sender_account_type = models.CharField(max_length=64, blank=True, null=True)
    bene_id_type = models.CharField(max_length=64, blank=True, null=True)
    bene_id = models.CharField(max_length=64, blank=True, null=True)
    bene_account_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banksheetdetials'


class Banksheets(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banksheets'


class Bonus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    month = models.CharField(max_length=255)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    amount = models.CharField(max_length=45)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    payroll_entry_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonus'


class BudgetMonthlies(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'budget_monthlies'


class BudgetMonthlyAllocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    budget_monthly = models.ForeignKey(BudgetMonthlies, models.DO_NOTHING)
    account_name = models.CharField(max_length=255)
    budget_amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budget_monthly_allocations'


class Budgets(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    account_category = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    budget_amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'budgets'


class CashNds(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    previous_date = models.CharField(max_length=255)
    previous_pending = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    previous_deposit = models.DecimalField(max_digits=5, decimal_places=2)
    previous_balance = models.DecimalField(max_digits=5, decimal_places=2)
    bonus = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    bonus_type = models.CharField(max_length=255, blank=True, null=True)
    date_selected = models.CharField(max_length=255)
    date_cod = models.DecimalField(max_digits=5, decimal_places=2)
    date_pending = models.DecimalField(max_digits=5, decimal_places=2)
    deposit_status = models.CharField(max_length=255)
    deposit_delayed = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash_nds'


class Cnds(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    date = models.CharField(max_length=255)
    pending_balance = models.CharField(max_length=255)
    last_deposit_amount = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cnds'


class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    vat_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Deductions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateField()
    month = models.CharField(max_length=255)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    amount = models.CharField(max_length=45)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deductions'


class Departments(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class Designations(models.Model):
    id = models.BigAutoField(primary_key=True)
    department_id = models.IntegerField()
    name = models.CharField(max_length=255)
    created_by = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designations'


class DistributionItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    dist = models.ForeignKey('Distributions', models.DO_NOTHING)
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distribution_items'


class Distributions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distributions'


class DriverWallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey('Employees', models.DO_NOTHING)
    date = models.CharField(max_length=255)
    trans_amount = models.CharField(max_length=255)
    trans_mode = models.CharField(max_length=255)
    trans_type = models.CharField(max_length=255)
    trans_reference = models.CharField(max_length=255)
    trans_status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'driver_wallets'


class EmployeeComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee_id = models.IntegerField()
    user_id = models.IntegerField()
    description = models.CharField(max_length=255)
    created_by = models.IntegerField()
    is_read = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_comments'


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    verified = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    bank_type = models.CharField(max_length=45, blank=True, null=True)
    contact_numer = models.CharField(max_length=255, blank=True, null=True)
    cpr = models.CharField(unique=True, max_length=255)
    talabat_id = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    department_id = models.IntegerField(blank=True, null=True)
    designation_id = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    visa = models.CharField(max_length=255, blank=True, null=True)
    visa_expiry_date = models.DateField(blank=True, null=True)
    contract_start = models.DateField(blank=True, null=True)
    contract_end = models.DateField(blank=True, null=True)
    joining_date = models.DateField(blank=True, null=True)
    vehicle_type = models.CharField(max_length=255, blank=True, null=True)
    vehicle_number = models.CharField(max_length=255, blank=True, null=True)
    vehicle_make_model = models.CharField(max_length=255, blank=True, null=True)
    vehicle_year = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    license_expiry_date = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    bank_account_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    cpr_image = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    passport_image = models.CharField(max_length=255, blank=True, null=True)
    license_image = models.CharField(max_length=255, blank=True, null=True)
    visa_image = models.CharField(max_length=255, blank=True, null=True)
    contract_file = models.CharField(max_length=255, blank=True, null=True)
    passport_number = models.CharField(unique=True, max_length=255, blank=True, null=True)
    passport_expiry_date = models.DateField(blank=True, null=True)
    salary_structure = models.ForeignKey('SalaryStructures', models.DO_NOTHING, db_column='salary_structure')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    iban = models.CharField(max_length=255, blank=True, null=True)
    cnd = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Invoices(models.Model):
    id = models.OneToOneField('Suppliers', models.DO_NOTHING, db_column='id', primary_key=True)
    date = models.DateField()
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    supplier_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoices'


class JournalEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    tx = models.ForeignKey('Transactions', models.DO_NOTHING)
    credit_account = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='credit_account')
    debit_account = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='debit_account')
    desc = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journal_entries'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelHasPermissions(models.Model):
    permission = models.OneToOneField('Permissions', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_permissions'
        unique_together = (('permission', 'model_id', 'model_type'),)


class ModelHasRoles(models.Model):
    role = models.OneToOneField('Roles', models.DO_NOTHING, primary_key=True)
    model_type = models.CharField(max_length=255)
    model_id = models.PositiveBigIntegerField()

    class Meta:
        managed = False
        db_table = 'model_has_roles'
        unique_together = (('role', 'model_id', 'model_type'),)


class MonthlyAllocatedItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    allocation = models.ForeignKey('MonthlyAllocations', models.DO_NOTHING)
    account_id = models.CharField(max_length=255)
    amount_allocated = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_allocated_items'


class MonthlyAllocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    dist = models.ForeignKey(Distributions, models.DO_NOTHING)
    year = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_allocations'


class MonthlyBudgetAllocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    distribution = models.ForeignKey('MonthlyBudgets', models.DO_NOTHING)
    account_name = models.CharField(max_length=255)
    budget_amount = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_budget_allocations'


class MonthlyBudgets(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.CharField(max_length=255)
    month = models.CharField(max_length=255)
    percentage = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_budgets'


class MonthlyScoresheets(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    utr_score = models.CharField(max_length=255)
    acceptance_score = models.CharField(max_length=255)
    attendance_score = models.CharField(max_length=255)
    overall_score = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    month = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monthly_scoresheets'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    client_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.PositiveBigIntegerField()
    client_id = models.PositiveBigIntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    secret = models.CharField(max_length=100, blank=True, null=True)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    id = models.BigAutoField(primary_key=True)
    client_id = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PayrollEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    month = models.CharField(max_length=45, blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payroll_entries'


class Payslips(models.Model):
    id = models.BigAutoField(primary_key=True)
    basic_salary = models.CharField(max_length=45, blank=True, null=True)
    bonus = models.CharField(max_length=45, blank=True, null=True)
    deduction = models.CharField(max_length=45, blank=True, null=True)
    net_payable = models.CharField(max_length=255)
    salary_month = models.CharField(max_length=255)
    payroll_entry_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payslips'


class Performances(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    starting_date = models.CharField(max_length=255)
    ending_date = models.CharField(max_length=255)
    shift_count = models.CharField(max_length=255)
    no_shows = models.CharField(max_length=255)
    late_login = models.CharField(max_length=255)
    completed_orders = models.CharField(max_length=255)
    cancelled_orders = models.CharField(max_length=255)
    cancellation_10_orders = models.CharField(max_length=255)
    utr = models.CharField(max_length=255)
    total_working_hours = models.CharField(max_length=255)
    total_break_hours = models.CharField(max_length=255)
    attendance_percentage = models.CharField(max_length=255)
    breaks_percentage = models.CharField(max_length=255)
    notification_count = models.CharField(max_length=255)
    acceptance_count = models.CharField(max_length=255)
    acceptance_rate = models.CharField(max_length=255)
    avg_customer_time = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performances'


class Permissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permissions'


class PickerTimesheets(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    hours = models.CharField(max_length=255)
    temp_hours = models.CharField(max_length=256, blank=True, null=True)
    orders = models.CharField(max_length=255, blank=True, null=True)
    overtime_hours = models.CharField(max_length=255, blank=True, null=True)
    late_hours = models.CharField(max_length=255, blank=True, null=True)
    overtime_late_hours = models.CharField(max_length=255, blank=True, null=True)
    utr = models.CharField(max_length=255, blank=True, null=True)
    month = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picker_timesheets'


class PurchaseInvoiceItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    pinvoice = models.ForeignKey('PurchaseInvoices', models.DO_NOTHING)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_invoice_items'


class PurchaseInvoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    supplier = models.ForeignKey('Suppliers', models.DO_NOTHING)
    date = models.DateField()
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    taxed_amount = models.CharField(max_length=255, blank=True, null=True)
    amount_in_words = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_invoices'


class Revisions(models.Model):
    revisionable_type = models.CharField(max_length=255)
    revisionable_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    key = models.CharField(max_length=255)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'revisions'


class RoleHasPermissions(models.Model):
    permission = models.OneToOneField(Permissions, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey('Roles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_has_permissions'
        unique_together = (('permission', 'role'),)


class Roles(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    guard_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class SalaryStructures(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hourly_rate = models.CharField(max_length=255)
    per_drop = models.CharField(max_length=256, blank=True, null=True)
    houry_rate_temp = models.CharField(max_length=256, blank=True, null=True)
    delivery_rate = models.CharField(max_length=255)
    extra_per_utr = models.CharField(max_length=45, blank=True, null=True)
    per_km = models.CharField(max_length=45, blank=True, null=True)
    long_distance_1 = models.CharField(max_length=45, blank=True, null=True)
    long_distance_2 = models.CharField(max_length=45, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    overtime_rate = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salary_structures'


class SalesInvoiceItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    sinvoice = models.ForeignKey('SalesInvoices', models.DO_NOTHING)
    item = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_invoice_items'


class SalesInvoices(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    date = models.DateField()
    type = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    taxed_amount = models.CharField(max_length=255, blank=True, null=True)
    amount_in_words = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_invoices'


class Suppliers(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=45, blank=True, null=True)
    vat_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'suppliers'


class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    team_leader = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


class TicketComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    ticket = models.ForeignKey('Tickets', models.DO_NOTHING)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    comment = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    is_read = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket_comments'


class Tickets(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    assigned_to = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tickets'


class Timesheets(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    hours = models.CharField(max_length=255)
    orders = models.CharField(max_length=255, blank=True, null=True)
    utr = models.CharField(max_length=45, blank=True, null=True)
    po_orders = models.CharField(max_length=256)
    po_hours = models.CharField(max_length=256)
    day_deduction = models.CharField(max_length=255, blank=True, null=True)
    pay_per_distance = models.CharField(max_length=45, blank=True, null=True)
    extra_per_utr = models.CharField(max_length=45, blank=True, null=True)
    day_deduction_rate = models.CharField(max_length=255, blank=True, null=True)
    double_orders = models.CharField(max_length=255, blank=True, null=True)
    long_distance_sakhir = models.CharField(max_length=45, blank=True, null=True)
    long_distance_durra = models.CharField(max_length=45, blank=True, null=True)
    month = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)
    employee = models.ForeignKey(Employees, models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timesheets'


class Transactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=255)
    country = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class UtrScores(models.Model):
    id = models.BigAutoField(primary_key=True)
    score = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utr_scores'
