from django.db import models
from django.contrib.auth.models import User
from shop.models import Food, Company
from django.db.models import Sum
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.user.username) + "/ " + str(self.company) + ' / ' + str(self.order)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    items_order = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Итем корзины'
        verbose_name_plural = 'Итемы корзины'

    def __str__(self):
        return str(self.food) + " / " + str(self.items_order)

    def total(self):
        total = 0.0
        for item in self.items.all():
            total += (item.product.prodPrice * item.quantity)
        return total

@receiver(pre_save, sender=CartItem)
def correct_price_quantity_save(sender,  **kwargs):
    cart_item = kwargs['instance']
    food = Food.objects.get(id=cart_item.food.id)
    cart = Cart.objects.get(id=cart_item.cart.id)

    #проверка на превышение кол-ва
    if cart_item.quantity > food.quantity:
        cart_item.quantity = food.quantity

    cart_item.total_price = cart_item.quantity * cart_item.price
    cart_item.price = cart_item.quantity * food.price


    cart.save()

@receiver(pre_delete, sender=CartItem)
def correct_price_quantity_delete(sender, **kwargs):
    cart_item = kwargs['instance']
    food = Food.objects.get(id=cart_item.food.id)
    cart_item.price = cart_item.quantity * food.price
    cart = Cart.objects.get(id=cart_item.cart.id)
    cart.total_price -= cart_item.price
    cart.save()



