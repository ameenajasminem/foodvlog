from django.db import models
from shop.models import products


# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='cartlist'
        ordering=['date_added']
    def __str__(self):
        return self.cart_id
class item(models.Model):
    prodt=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)


    class Meta:
        db_table='item'
    def sub_total(self):
        return self.products.price *self.quan
    def __str__(self):
        return self.products
    def total(self):
        return self.prodt.price*self.quan
