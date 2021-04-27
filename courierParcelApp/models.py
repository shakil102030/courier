from django.db import models
from django.forms import ModelForm
from django.utils.crypto import get_random_string

class Merchants(models.Model):
    merchant_name = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.merchant_name

class Order(models.Model):
    merchant_nm = models.CharField(max_length=100, blank = True)
    invoiceId = models.CharField(max_length=100,  blank = True)
    product_type = models.CharField(max_length=100, blank = True)
    status = models.CharField(max_length = 100)
    location = models.CharField(max_length=100, null=True)
    weight= models.IntegerField()
    delivery_charge = models.IntegerField()
    cod_charge = models.IntegerField(blank = True)
    return_charge = models.IntegerField(blank = True)
    charge = models.FloatField(blank = True)
    
    def __str__(self):
        return self.product_type.__str__()

    def save(self):
        self.invoiceId = '#' + get_random_string(3).lower()
        if self.cod_charge == None and self.return_charge == None:
            self.cod_charge = 0 
            self.return_charge = 0
        self.charge = self.delivery_charge + self.delivery_charge * (self.cod_charge/100) + self.delivery_charge * (self.return_charge/100)
        super(Order,self).save()


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['merchant_nm', 'product_type', 'status', 'location', 'weight', 'delivery_charge', 'cod_charge', 'return_charge']


