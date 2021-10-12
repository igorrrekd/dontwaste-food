from datetime import timezone

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
# from common.decorators import ajax_required
from .forms import RestaurantCreateForm
from .models import Restaurant, Category, Meal


@login_required
def restaurant_create(request):
    if request.method == 'POST':
        # wysłano formularz
        form = RestaurantCreateForm(request.POST, request.FILES)
        if form.is_valid():
            #  dane formularza są prawidłowe
            #  print(form.cleaned_data)
            new_item = form.save(commit=False)
            # przypisz bieżącego użytkownika do obiektu
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Pomyślnie dodano Restauracje')

            # przekierowanie do widoku szczegółów nowo utworzonego obiektu
            return redirect(new_item.get_absolute_url())
    else:
        # zbudowanie formularza za pomocą danych dostarczonych do bookmarkletu za pomocą żądania GET
        form = RestaurantCreateForm()

    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})


def restaurant_list(request):
    rest = Restaurant.objects.all()
    return render(request,
                  'images/image/list.html',
                  {'section': 'view',
                   'rest': rest})


@login_required
def restaurant_detail(request, name):
    res = get_object_or_404(Restaurant,
                            name=name,
                            is_active=True)
    return render(request,
                  'images/image/detail2.html',
                  {'res': res})


def restaurant_meal_categories(request):
    categories = Category.objects.all()

    return render(request,
                  'food/meals/categories.html',
                  {'categories': categories})


def meal_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    meals = Meal.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        meals = meals.filter(category=category)
    return render(request,
                  'food/meals/list.html',
                  {'category': category,
                   'categories': categories,
                   'meals': meals})


def meal_detail(request, id, slug):
    meal = get_object_or_404(Meal,
                             id=id,
                             slug=slug,
                             available=True)
    return render(request,
                  'food/meals/detail.html',
                  {'meal': meal})





# @login_required
# @require_POST
# def image_like(request):
#     image_id = request.POST.get('id')
#     action = request.POST.get('action')
#     if image_id and action:
#         try:
#             image = Restaurant.objects.get(id=image_id)
#             if action == 'like':
#                 image.users_like.add(request.user)
#             else:
#                 image.users_like.remove(request.user)
#             return JsonResponse({'status':'ok'})
#         except:
#             pass
#     return JsonResponse({'status':'error'})


# @login_required
# def image_list(request):
#     views = Restaurant.objects.all()
#     paginator = Paginator(views, 1)
#     page = request.GET.get('page')
#     try:
#         views = paginator.page(page)
#     except PageNotAnInteger:
#         # Jeśli page nie jest liczbą całkowitą dostarcz pierwszą stronę
#         views = paginator.page(1)
#     except EmptyPage:
#         if request.is_ajax():
#             # If the request is AJAX and the page is out of range
#             # return an empty page
#             return HttpResponse('')
#         # Jeśli page wykracza poza zakres dostarcz ostatnią stronę wyników
#         views = paginator.page(paginator.num_pages)
#     if request.is_ajax():
#         return render(request,
#                       'images/image/list_ajax.html',
#                       {'section': 'view', 'views': views})
#     return render(request,
#                   'images/image/list.html',
#                    {'section': 'views', 'views': views})
