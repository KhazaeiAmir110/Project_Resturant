from django import forms
from .models import Reservation
"""
forms.Form => باید به صورت دستی مقادیر را وارد کنیم
"""
# class ReservationForm(forms.Form):
#     name = forms.CharField(max_length=200, required=True)
#     email = forms.EmailField(max_length=254, required=True)
#     phone = forms.IntegerField(max_length=12, required=True)
#     number = forms.IntegerField(max_length=10, default=1, required=True)
#     data = forms.DateField(required=True)
#     time = forms.TimeField(required=True)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
