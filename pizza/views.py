from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .forms import *


from .models import *

# Create your views here.

def index(request):
    ingredients = Ingredient.objects.all()
    groups = Group.objects.all()

    data = {'ingredients': ingredients, 'groups': groups}
    return render(request, 'main_page.html', context=data)

def order(request):
    return render(request, 'order_page.html')

class CreateIngredient(View):
    def get(self, request):
        form = IngredientForm()
        return render(request, 'create_ingredients_page.html', context={'form': form})

    def post(self, request):
        bound_form = IngredientForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('main-page')
        return render(request, 'create_ingredients_page.html' ,context={'form': bound_form})


class EditIngredient(View):
    def get(self, request, name):
        obj = Ingredient.objects.get(name=name)
        form = IngredientForm(instance=obj)
        return render(request, 'edit_page.html', {'obj':obj, 'form': form})

    def post(self, request, name):
        obj = Ingredient.objects.get(name=name)
        form = IngredientForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect('main-page')
        return render(request, 'create_ingredients_page.html', context={'obj': obj, 'form': form})

def ingredient_delete(request, name):
    obj = Ingredient.objects.get(name=name)
    obj.delete()
    return redirect('main-page')

@csrf_exempt
def order_create(request):
    temp = dict(request.POST)
    arr = temp.get('data[]')
    if request.is_ajax():
        obj = Order(order_id=arr[0] ,name=Ingredient.objects.get(name=arr[1]), number=arr[2])
        obj.save()