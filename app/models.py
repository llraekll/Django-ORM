from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=20)
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)

