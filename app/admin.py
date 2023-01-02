from django.contrib import admin
from app.models import Customer, Product, Order , Tag

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
# Register your models here.
