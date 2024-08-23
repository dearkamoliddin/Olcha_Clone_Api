from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.middleware import cache
from rest_framework.authtoken.models import Token
from olcha.models import ProductModel


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


# @receiver(pre_save, sender=ProductModel)
# @receiver(post_save, sender=ProductModel)
# def save_product(sender, instance, **kwargs):
#     cache.delete('product_list')
#     product_id = instance.id
#     cache.delete(f'product_detail_{product_id}')

