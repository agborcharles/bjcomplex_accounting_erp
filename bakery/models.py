from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class BakeryOpeningBalances(models.Model):
    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )



    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    ob_no = models.CharField(max_length=200, null = True, blank = True, verbose_name = "OB No")
    openingbalance_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Opening Balance Id")
    customer = models.CharField(max_length=200, verbose_name = 'Customer')
    amount = models.FloatField(default=0.0, verbose_name = 'Amount')


    def __str__(self):
        return self.customer

    def post_save_settings_model_receiver(sender, instance, created, *args, **kwargs):
        if created:
            try:
                UserSetting.objects.create(user=instance)
            except:
                pass

    post_save.connect(post_save_settings_model_receiver, sender= settings.AUTH_USER_MODEL)

    class Meta():
        verbose_name = 'BakeryOpeningBalance'
        verbose_name_plural = 'BakeryOpeningBalances'
        ordering: ['date']


class BakeryCollector(models.Model):
    created_at = models.DateField("Date", default=now)
    collector = models.CharField(max_length=200, verbose_name = 'Collector')


    def __str__(self):
        return self.collector

    class Meta():
        verbose_name = 'BakeryCollector'
        verbose_name_plural = 'BakeryCollectors'
        ordering: ['date']

class BakeryPayment(models.Model):

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    COLLECTORS = (
        ('Moses', 'Moses'),
        ('Glory', 'Glory'),
        ('Kesty', 'Kesty'),
        ('Charles', 'Charles'),
        ('Cyril', 'Cyril'),
        ('Aly', 'Aly'),
        ('Joan', 'Joan'),
        ('Micheal', 'Micheal'),
        ('Esther', 'Esther'),
        ('Violet', 'Violet'),
        ('Kaba', 'Kaba'),

    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    session = models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    collector = models.CharField(max_length = 500, choices=COLLECTORS, null = True, blank = True, verbose_name = 'Collector')
    payment_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Payment Invoice Id")
    customer = models.CharField(max_length=200, verbose_name = 'Customer')
    amount = models.FloatField(default=0.0, verbose_name = 'Amount')

    def __str__(self):
        return self.customer

    class Meta():
        verbose_name = 'BakeryPayment'
        verbose_name_plural = 'BakeryPayments'
        ordering: ['date']


class BakeryReturn(models.Model):
    SUPPLIER = (
        ('Moses', 'Moses'),
        ('Glory', 'Glory'),
        ('Kesty', 'Kesty'),
    )

    CATEGORY = (
        ('Bread', 'Bread'),
        ('Confectionary', 'Confectionary'),
        ('Hamburger', 'Hamburger'),
        ('Sandwich', 'Sandwich'),
        ('Cake', 'Cake'),
        ('Milk Bread', 'Milk Bread'),
        ('Biscuit', 'Biscuit'),
        ('Croissant', 'Croissant'),
        ('Fruitage', 'Fruitage'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order_no =  models.IntegerField()
    return_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Return Invoice Id")
    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    customer_from = models.CharField(max_length=200, verbose_name = 'Customer_from')
    customer_to = models.CharField(max_length=200, verbose_name = 'Customer_to')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Sub Department')
    category = models.CharField(max_length = 500, choices=CATEGORY, default='', null = True, blank = True)
    product = models.CharField(max_length=200, verbose_name = 'Product Name')
    qty = models.IntegerField(verbose_name = 'Quantity')
    cost_price = models.FloatField(default=0.0, verbose_name = 'Cost Price')
    total_amount = models.FloatField(default=0.0)

    @property
    def get_net_amount(self):
        return self.qty * self.cost_price

    #@property
    #def get_discount_amount(self):
        #return self.discount * self.qty


    #@property
    #def get_net_amount(self):
        #return self.net_amount - self.total_amount_paid
#---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_amount = self.get_net_amount
        #self.discount_value = self.get_discount_amount
        #self.net_amount = self.total_amount - self.discount_value

        super(BakeryReturn, self).save(*args, **kwargs)


    def __str__(self):
        return self.customer_from

    class Meta():
        verbose_name = 'BakeryReturns'
        verbose_name_plural = 'BakeryReturns'
        ordering: ['date']


class BakerySales(models.Model):
    SUPPLIER = (
        ('Moses', 'Moses'),
        ('Glory', 'Glory'),
        ('KESTY', 'KESTY'),
    )

    CATEGORY = (
        ('Bread', 'Bread'),
        ('Confectionary', 'Confectionary'),
        ('Hamburger', 'Hamburger'),
        ('Sandwich', 'Sandwich'),
        ('Cake', 'Cake'),
        ('Milk Bread', 'Milk Bread'),
        ('Biscuit', 'Biscuit'),
        ('Croissant', 'Croissant'),
        ('Fruitage', 'Fruitage'),
    )

    DEPARTMENTS = (
        ('Bakery', 'Bakery'),
    )

    SUBDEPARTMENTS = (
        ('Boulangerie', 'Boulangerie'),
        ('Patisserie', 'Patisserie'),
    )

    SESSIONS = (
        ('Morning', 'Morning'),
        ('Evening', 'Evening'),
    )

    created_at = models.DateField("Date", default=now)
    employee = models.ForeignKey(to=User, on_delete=models.CASCADE)
    order_no =  models.IntegerField()
    invoice_id = models.CharField(max_length=200, null = True, blank = True, verbose_name = "Invoice Id")
    supplier = models.CharField(max_length = 500, choices=SUPPLIER, default='', null = True, blank = True, verbose_name = 'Supplier')
    customer = models.CharField(max_length=200, verbose_name = 'Customer')
    department =  models.CharField(max_length = 500, choices=DEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Department')
    sub_department =  models.CharField(max_length = 500, choices=SUBDEPARTMENTS, default='Bakery', null = True, blank = True, verbose_name = 'Sub Department')
    category = models.CharField(max_length = 500, choices=CATEGORY, default='', null = True, blank = True)
    session = models.CharField(max_length = 500, choices=SESSIONS, default='', null = True, blank = True, verbose_name = 'Session')
    product = models.CharField(max_length=200, verbose_name = 'Product Name')
    qty = models.IntegerField(verbose_name = 'Quantity')
    cost_price = models.FloatField(default=0.0, verbose_name = 'Cost Price')
    total_amount = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0, verbose_name = 'Discount')
    discount_value = models.FloatField(default=0.0, verbose_name = 'Discount Value')
    net_amount = models.FloatField(default=0.0, verbose_name = 'Net Amount')
    commission = models.FloatField(default=0.0, verbose_name = 'Commission')

    @property
    def get_net_amount(self):
        return self.qty * self.cost_price

    @property
    def get_discount_amount(self):
        return self.discount * self.qty


    #@property
    #def get_net_amount(self):
        #return self.net_amount - self.total_amount_paid
#---------------- Value Calculations -----------------#

    def save(self, *args, **kwargs):
        self.total_amount = self.get_net_amount
        self.discount_value = self.get_discount_amount
        self.net_amount = self.total_amount - self.discount_value

        super(BakerySales, self).save(*args, **kwargs)


    def __str__(self):
        return self.supplier

    class Meta():
        verbose_name = 'BakerySales'
        verbose_name_plural = 'BakerySales'
        ordering: ['date']
