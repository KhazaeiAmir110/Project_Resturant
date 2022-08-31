from django.db import models
from django.utils.translation import gettext as _


class Food(models.Model):
    FOOD_TYPE = [
        ("lunch", "تهار"),
        ("dinner", "شام"),
        ("drinks", "نوشیدنی")
    ]
    name = models.CharField(max_length=50)
    description = models.CharField(_('توضیحات'), max_length=50)
    rate = models.IntegerField(_('امتیاز'), default=0)
    price = models.IntegerField()
    time = models.IntegerField(_('زمان'))
    pub_date = models.DateField(_('تاریخ انتشار'), auto_now=False, auto_now_add=True)
    photo = models.ImageField(upload_to='foods/')
    food_type = models.CharField("نوع", max_length=10, choices=FOOD_TYPE, default="drinks")

    # نمایش غذا برای دیگران
    def __str__(self):
        return self.name
