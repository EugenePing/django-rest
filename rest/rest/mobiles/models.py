from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Mobile(models.Model):
    brand = models.CharField(verbose_name='Brand', db_index=True, max_length=64)
    model = models.CharField(verbose_name='Model', max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    MOBILE_OS = (
        (1, 'Android'),
        (2, 'IOS'),
    )
    os = models.IntegerField(verbose_name='OS', choices=MOBILE_OS)
    MOBILE_TYPES = (
        (1, 'Smartphone'),
        (2, 'Buttonphone'),
        (3, 'Clamshell'),
    )
    phone_type = models.IntegerField(verbose_name='Phone_Type', choices=MOBILE_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
