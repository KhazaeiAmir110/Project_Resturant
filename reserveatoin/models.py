from django.db import models
from django.utils.translation import gettext as _


class Reservation(models.Model):
    name = models.CharField(_("نام و نام خانوادگی"), max_length=200)
    email = models.EmailField(_("ایمیل"), max_length=254)
    phone = models.IntegerField(_("تلفن"), max_length=12)
    number = models.IntegerField(_("تعداد"), max_length=10, default=1)
    data = models.DateField(_("تاریخ"))
    time = models.TimeField(_("ساعت"))

    def __str__(self):
        return self.name
