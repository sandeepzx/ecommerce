from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    Cat_Name = models.CharField( max_length=250)
    

class Product(models.Model):
    Pro_Name = models.CharField(max_length=250)
    Pro_Price = models.IntegerField(null=True)
    Pro_Desc = models.TextField(null=True)
    Pro_Image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    Pro_Cat = models.ForeignKey(Categories, on_delete=models.CASCADE)
        
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Age = models.IntegerField(null=True)
    Number = models.CharField( max_length=250)
    Address = models.TextField(null=True)
    Image = models.ImageField(null=True, upload_to='images/', height_field=None, width_field=None, max_length=None)

class Cart(models.Model):
    cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(null=True)
    def total_price(self):
        return self.Quantity*self.prod.Pro_Price
    

    
