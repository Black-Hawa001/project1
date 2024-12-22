from django.shortcuts import render
from .models import vyakula , vinywaji , Users
from .forms import FoodForm


def home_view(request,*args , **kwargs):
    return render (request , "home.html", {})
    print(args , kwargs)
    print(request.user)


def  food_details_view (request):
    obj = vyakula.objects.get(id=1)
    context = {
    'name' : obj.name,
    'description' : obj.description,
    'address': obj.address,
    'category' : obj.category
    }
    return render (request,"food/food.html",context)

def food_create_view (request):
    form = FoodForm (request.POST or None)
    if form.is_valid ():
        form.save()
        form = FoodForm()
    context = {
    'form' : form

    }
    return render (request,"food/form.html",context)