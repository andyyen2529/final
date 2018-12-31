from django.db import models

# Create your models here.

class Customer(models.Model):
    #id primarykey 自已會幫你社
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()

class Order(models.Model):
    price =  models.IntegerField()
    customer = models.ForeignKey(Customer)