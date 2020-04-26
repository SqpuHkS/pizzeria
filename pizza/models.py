from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Group(models.Model):
    group = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.group}'

class Order(models.Model):
    order_id = models.CharField(max_length=20)
    name = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    number = models.IntegerField()


    def __str__(self):
        return f'{self.order_id}'

