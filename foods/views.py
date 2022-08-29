from django.shortcuts import render
from .models import Food


def food_list(request):
    foods_list = Food.objects.all()
    context = {
        "foods": foods_list
    }
    return render(request, "foods/list.html", context)


def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    context = {
        "food": food
    }
    return render(request, "foods/detail.html", context)
