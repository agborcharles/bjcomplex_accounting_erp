from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User



# Create your models here.
class LoansPayable(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Loans Recievable', 'Loans Recievables'),
        ('Cash', 'Cash'),
    )

    ACCOUNT_CR = (
        ('Cash', 'Cash'),
        ('Loans Recievable', 'Loans Recievables'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
        ('WholeSale', 'WholeSale'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    loan_rec_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Loan Id")
    institution = models.CharField( max_length=200, default='', verbose_name = "Institution")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")
    due_date = models.DateField("Due Date", default="", null = True, blank = True,)


    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'LoansPayable'
        verbose_name_plural = 'LoansPayable'
        ordering: ['date']


class LoansRecievable(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Loans Recievable', 'Loans Recievables'),
        ('Cash', 'Cash'),
    )

    ACCOUNT_CR = (
        ('Cash', 'Cash'),
        ('Loans Recievable', 'Loans Recievables'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
        ('WholeSale', 'WholeSale'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    loan_rec_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Loan Id")
    beneficiary = models.CharField( max_length=200, default='', verbose_name = "Beneficiary")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")
    due_date = models.DateField("Due Date", default="", null = True, blank = True,)


    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'LoansRecievable'
        verbose_name_plural = 'LoansRecievables'
        ordering: ['date']


class AccountsRecievable(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Accounts Recievable', 'AccountsRecievables'),
        ('Cash', 'Cash'),
    )

    ACCOUNT_CR = (
        ('Sales', 'Sales'),
        ('Accounts Recievable', 'AccountsRecievables'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
        ('WholeSale', 'WholeSale'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    sales_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    customer = models.CharField( max_length=200, default='', verbose_name = "Customer")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")
    due_date = models.DateField("Due Date", default="", null = True, blank = True,)


    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'AccountsRecievable'
        verbose_name_plural = 'AccountsRecievables'
        ordering: ['date']



class Expense(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Airtime Expense', 'Airtime Expense'),
        ('Miscelleanous Expenses', 'Miscelleanous Expenses'),
        ('Tape expense', 'Tape expense'),
        ('Bike Maintanance Expense', 'Bike Maintanance Expense'),
        ('Bike Repairs Expense', 'Bike Repairs Expense'),
        ('Computer Repairs Expense', 'Computer Repairs Expense'),
        ('Cooler Maintainance expense', 'Cooler Maintainance expense'),
        ('Electrical repairs expense', 'Electrical repairs expense'),
        ('Fridge Repairs Expense', 'Fridge Repairs Expense'),
        ('Generator Maintainance Expense', 'Generator Maintainance Expense'),
        ('Internet Bill Expense', 'Internet Bill Expense'),
        ('Other Repairs Expense', 'Other Repairs Expense'),
        ('Oven Maintainance expenses', 'Oven Maintainance expenses'),
        ('Van Maintainance expense', 'Van Maintainance expense'),
        ('Van Repairs Expense', 'Van Repairs Expense'),
        ('Cable Expenses', 'Cable Expenses'),
        ('Electricity Bill Expense', 'Electricity Bill Expense'),
        ('Water Bill Expense', 'Water Bill Expense'),
        ('Charges expense', 'Charges expense'),
        ('Cleaning Expense', 'Cleaning Expense'),
        ('Commission Expense', 'Commission Expense'),
        ('Health Expense', 'Health Expense'),
        ('Insurance Expense', 'Insurance Expense'),
        ('Off Loading Expense', 'Off Loading Expense'),
        ('Provision for Loss Product Expense', 'Provision for Loss Product Expense'),
        ('Hygiene and Sanitation Expenses', 'Hygiene and Sanitation Expenses'),
        ('Social Insurance Expense', 'Social Insurance Expense'),
        ('Rents Expense', 'Rents Expense'),
        ('Stationaries', 'Stationaries'),
        ('Direct Labour Expense', 'Direct Labour Expense'),
        ('InDirect Labour Expense', 'InDirect Labour Expense'),
        ('Fuel expense', 'Fuel expense'),
        ('Transportation Expense', 'Transportation Expense'),
        ('Gas Expense', 'Gas Expense'),
        ('Salary Expenses', 'Salary Expenses'),
        ('Allowance Expense', 'Allowance Expense'),
        ('Tax Expense', 'Tax Expense'),
        ('Depreciation Expense', 'Depreciation Expense'),
        ('Bank Charges Expense', 'Bank Charges Expense'),
    )

    ACCOUNT_CR = (
        ('Cash', 'Cash'),
        ('Airtime Expense Payables', 'Airtime Expense Payables'),
        ('Miscelleanous Expenses Payables', 'Miscelleanous Expenses Payables'),
        ('Tape expense Payables', 'Tape expense Payables'),
        ('Bike Maintanance Expense Payables', 'Bike Maintanance Expense Payables'),
        ('Bike Repairs Expense Payables', 'Bike Repairs Expense Payables'),
        ('Computer Repairs Expense Payables', 'Computer Repairs Expense Payables'),
        ('Cooler Maintainance expense Payables', 'Cooler Maintainance expense Payables'),
        ('Electrical repairs expense Payables', 'Electrical repairs expense Payables'),
        ('Fridge Repairs Expense Payables', 'Fridge Repairs Expense Payables'),
        ('Generator Maintainance Expense Payables', 'Generator Maintainance Expense Payables'),
        ('Internet Bill Expense Payables', 'Internet Bill Expense Payables'),
        ('Other Repairs Expense Payables', 'Other Repairs Expense Payables'),
        ('Oven Maintainance expenses Payables', 'Oven Maintainance expenses Payables'),
        ('Van Maintainance expense Payables', 'Van Maintainance expense Payables'),
        ('Van Repairs Expense Payables', 'Van Repairs Expense Payables'),
        ('Cable Expenses Payables', 'Cable Expenses Payables'),
        ('Electricity Bill Expense Payables', 'Electricity Bill Expense Payables'),
        ('Water Bill Expense Payables', 'Water Bill Expense Payables'),
        ('Charges expense Payables', 'Charges expense Payables'),
        ('Cleaning Expense Payables', 'Cleaning Expense Payables'),
        ('Commission Expense Payables', 'Commission Expense Payables'),
        ('Health Expense Payables', 'Health Expense Payables'),
        ('Insurance Expense Payables', 'Insurance Expense Payables'),
        ('Off Loading Expense Payables', 'Off Loading Expense Payables'),
        ('Provision for Loss Product Expense Payables', 'Provision for Loss Product Expense Payables'),
        ('Hygiene and Sanitation Expenses Payables', 'Hygiene and Sanitation Expenses Payables'),
        ('Social Insurance Expense Payables', 'Social Insurance Expense Payables'),
        ('Rents Expense Payables', 'Rents Expense Payables'),
        ('Stationaries Payables', 'Stationaries Payables'),
        ('Direct Labour Expense Payables', 'Direct Labour Expense Payables'),
        ('InDirect Labour Expense Payables', 'InDirect Labour Expense Payables'),
        ('Fuel expense Payables', 'Fuel expense Payables'),
        ('Transportation Expense Payables', 'Transportation Expense Payables'),
        ('Gas Expense Payables', 'Gas Expense Payables'),
        ('Salary Expenses Payables', 'Salary Expenses Payables'),
        ('Allowance Expense Payables', 'Allowance Expense Payables'),
        ('Tax Expense Payables', 'Tax Expense Payables'),
        ('Depreciation Expense Payables', 'Depreciation Expense Payables'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
        ('WholeSale', 'WholeSale'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    supplier = models.CharField( max_length=200, default='', verbose_name = "Supplier")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")
    due_date = models.DateField("Due Date", default="", null = True, blank = True,)


    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering: ['date']

class AccountsPayables(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR =(
        ('Cash', 'Cash'),
        ('Airtime Expense Payables', 'Airtime Expense Payables'),
        ('Miscelleanous Expenses Payables', 'Miscelleanous Expenses Payables'),
        ('Tape expense Payables', 'Tape expense Payables'),
        ('Bike Maintanance Expense Payables', 'Bike Maintanance Expense Payables'),
        ('Bike Repairs Expense Payables', 'Bike Repairs Expense Payables'),
        ('Computer Repairs Expense Payables', 'Computer Repairs Expense Payables'),
        ('Cooler Maintainance expense Payables', 'Cooler Maintainance expense Payables'),
        ('Electrical repairs expense Payables', 'Electrical repairs expense Payables'),
        ('Fridge Repairs Expense Payables', 'Fridge Repairs Expense Payables'),
        ('Generator Maintainance Expense Payables', 'Generator Maintainance Expense Payables'),
        ('Internet Bill Expense Payables', 'Internet Bill Expense Payables'),
        ('Other Repairs Expense Payables', 'Other Repairs Expense Payables'),
        ('Oven Maintainance Expenses Payables', 'Oven Maintainance Expenses Payables'),
        ('Van Maintainance Expense Payables', 'Van Maintainance Expense Payables'),
        ('Van Repairs Expense Payables', 'Van Repairs Expense Payables'),
        ('Cable Expenses Payables', 'Cable Expenses Payables'),
        ('Electricity Bill Expense Payables', 'Electricity Bill Expense Payables'),
        ('Water Bill Expense Payables', 'Water Bill Expense Payables'),
        ('Charges expense Payables', 'Charges expense Payables'),
        ('Cleaning Expense Payables', 'Cleaning Expense Payables'),
        ('Commission Expense Payables', 'Commission Expense Payables'),
        ('Health Expense Payables', 'Health Expense Payables'),
        ('Insurance Expense Payables', 'Insurance Expense Payables'),
        ('Off Loading Expense Payables', 'Off Loading Expense Payables'),
        ('Provision for Loss Product Expense Payables', 'Provision for Loss Product Expense Payables'),
        ('Hygiene and Sanitation Expenses Payables', 'Hygiene and Sanitation Expenses Payables'),
        ('Social Insurance Expense Payables', 'Social Insurance Expense Payables'),
        ('Rents Expense Payables', 'Rents Expense Payables'),
        ('Stationaries Payables', 'Stationaries Payables'),
        ('Direct Labour Expense Payables', 'Direct Labour Expense Payables'),
        ('InDirect Labour Expense Payables', 'InDirect Labour Expense Payables'),
        ('Fuel expense Payables', 'Fuel expense Payables'),
        ('Transportation Expense Payables', 'Transportation Expense Payables'),
        ('Gas Expense Payables', 'Gas Expense Payables'),
        ('Salary Expenses Payables', 'Salary Expenses Payables'),
        ('Allowance Expense Payables', 'Allowance Expense Payables'),
        ('Tax Expense Payables', 'Tax Expense Payables'),
        ('Depreciation Expense Payables', 'Depreciation Expense Payables'),
    )

    ACCOUNT_CR = (
        ('Cash', 'Cash'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
        ('WholeSale', 'WholeSale'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    payment_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    accnt_payables_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Stock Accnt Invoice Id")
    supplier_institution = models.CharField( max_length=200, default='', verbose_name = "Supplier/Institution")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")


    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'AccountsPayable'
        verbose_name_plural = 'AccountsPayable'
        ordering: ['date']


class Bank(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
    )

    ACCOUNT_CR = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    transaction_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    bank_reciept_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Bank Reciept Id")
    bank = models.CharField( max_length=200, default='', verbose_name = "Bank Name")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")

    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Bank'
        verbose_name_plural = 'Bank'
        ordering: ['date']


class Purchases(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Inventory', 'Inventory'),
    )

    ACCOUNT_CR = (
        ('Cash', 'Cash'),
        ('Creditors', 'Creditors'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)

    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    stock_accnt_inv_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Stock Accnt Invoice Id")
    supplier = models.CharField( max_length=200, default='', verbose_name = "Supplier")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")
    due_date = models.DateField("Due Date", default="", null = True, blank = True,)

    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Purchases'
        verbose_name_plural = 'Purchases'
        ordering: ['date']



class Creditors(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Creditors', 'Creditors'),
    )

    ACCOUNT_CR = (
        ('Cash', 'Cash'),

    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    payment_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Payment Id")
    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    supplier = models.CharField( max_length=200, default='', verbose_name = "Supplier")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")

    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Creditor'
        verbose_name_plural = 'Creditors'
        ordering: ['date']


class OpeningBalance(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNTS = (
        ('Opening Cash', 'Opening Cash'),
        ('Closing Cash', 'Closing Cash'),
        ('Accounts Receivables Opening Bal', 'Accounts Receivables Opening Bal'),
        ('Accounts Payables Opening Bal', 'Accounts Payables Opening Bal'),
        ('Creditors Opening Bal', 'Creditors Opening Bal'),
        ('Bank Opening Bal', 'Bank Opening Bal'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
    )


    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    customer_institution = models.CharField( max_length=200, default='', verbose_name = "Customer/Supplier/Institution")
    description = models.CharField(max_length=200, default='Opening Cash')
    amount = models.FloatField(default=0.0)
    account = models.CharField(max_length = 500, choices=ACCOUNTS, default='', null = True, blank = True)
    #account_dr = models.CharField(max_length = 500, choices=ACCOUNTS, default='', null = True, blank = True)
    #account_cr = models.CharField(max_length = 500, choices=ACCOUNTS, default='', null = True, blank = True)

    def __str__(self):
        return self.description

    class Meta():
        verbose_name = 'Opening Balance'
        verbose_name_plural = 'Opening Balances'
        ordering: ['date']


class Income(models.Model):
    USERSTATUS = (
        ('Employee', 'Employee'),
        ('Management', 'Management'),
    )

    ACCOUNT_DR = (
        ('Cash', 'Cash'),
        ('Closing Cash', 'Closing Cash'),

    )

    ACCOUNT_CR = (
        ('Accounts Receivables', 'Accounts Receivables'),
        ('Sales', 'Sales'),

    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
        ('Boulangerie', 'Boulangerie'),
        ('Supermarket', 'Supermarket'),
        ('Bar', 'Bar'),
        ('Snack', 'Snack'),
        ('Ice Cream', 'Ice Cream'),
    )

    created_at = models.DateField("Date", default=now)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='', null = True, blank = True)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    user_status = models.CharField(max_length = 500, choices=USERSTATUS, default='', null = True, blank = True)
    customer_institution = models.CharField( max_length=200, default='', verbose_name = "Customer/Institution")
    description = models.CharField(max_length=200)
    amount = models.FloatField(default=0.0)
    account_dr =  models.CharField(max_length = 500, choices=ACCOUNT_DR, default='', null = True, blank = True, verbose_name = "Account Debit")
    account_cr =  models.CharField(max_length = 500, choices=ACCOUNT_CR, default='', null = True, blank = True, verbose_name = "Account Credit")

    def __str__(self):
        return self.department

    class Meta():
        verbose_name = 'Income'
        verbose_name_plural = 'Income'
        ordering: ['date']
