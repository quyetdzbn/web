from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# from django.views.generic import CreateView

# class SignUpView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "app/signup.html"
def register(request):
    form = CreateUserForm()
    context={'form':form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.info(request,'ok')
            return redirect('login')
    context={'form':form}
    return render(request,'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)    
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'User or password not correct!')

    context={}
    return render(request,'app/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def introduce(request):
    return render(request,'app/introduce.html')

def search(request):
    if request.method=="POST":
        searched = request.POST["searched"]
        keys= Product.objects.filter(name__contains=searched)
    if request.user.is_authenticated:
        customer =  request.user
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order={'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context={'products':products,'cartItems':cartItems}
    return render(request,'app/search.html',{"search":searched,"keys":keys,'products':products,'cartItems':cartItems})

def home(request):
    if request.user.is_authenticated:
        customer =  request.user
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login="hidden"
        user_login="show"
    else:
        items=[]
        order={'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login="show"
        user_login="hidden"

    products = Product.objects.all()
    context={'products':products,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/home.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer =  request.user
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login="hidden"
        user_login="show"
    else:
        items=[]
        order={'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login="show"
        user_login="hidden"
    context={'items':items, 'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer =  request.user
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items =order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login="hidden"
        user_login="show"
    else:
        items=[]
        order={'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login="show"
        user_login="hidden"
    context={'items':items, 'order':order,'cartItems':cartItems,'user_not_login':user_not_login,'user_login':user_login}
    return render(request,'app/checkout.html',context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderItem.quantity =orderItem.quantity+1
    if action=='remove':
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    
    return JsonResponse('added',safe=False)