from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from restaurant.models import Meal
from .cart import Cart
from .forms import CartAddMealForm


@require_POST
def cart_add(request, meal_id):
    cart = Cart(request)
    meal = get_object_or_404(Meal, id=meal_id)
    form = CartAddMealForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(meal=meal,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, meal_id):
    cart = Cart(request)
    meal = get_object_or_404(Meal, id=meal_id)
    cart.remove(meal)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddMealForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})