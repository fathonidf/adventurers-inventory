import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect #tutor 3
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    total_items = items.count()

    context = {
        'app_name': 'Adventurer\'s Inventory',
        'name': request.user.username,
        'total_items': total_items,
        'items': items,
        'last_login': request.COOKIES.get("last_login")
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def increment_item(request, id):
    item = Item.objects.get(id=id)
    item.amount += 1
    item.save()

    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def decrement_item(request, id):
    item = Item.objects.get(id=id)
    if (item.amount > 0):
        item.amount -= 1
        item.save()
    if (item.amount == 0):
        item.delete()

    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def trash_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()

    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def get_item_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':

        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        link_image = request.POST.get("link_image")
        item_level = request.POST.get("item_level")
        user = request.user

        if amount and price and item_level:
            amount = int(amount)
            price = int(price)
            item_level = int(item_level)
            new_item = Item(name=name, amount=amount, price=price, description=description, link_image=link_image, item_level=item_level, user=user)
            new_item.save()
            return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(pk=item_id)
        item.delete()
        return HttpResponse(b"DELETED", status=200)
    
    return HttpResponseNotFound()