from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer, Order

# Create your views here.
def index(request):
    customer = Customer.objects.get(id=1) #只取一個
    print(customer)
    order = Order(price=100,customer=customer)
    order.save()
    customerList = Customer.objects.all() #取所有
    for i in customerList:
        print(i.name)
    orders = Order.objects.filter(customer=customer) #取條件
    for i in orders:
        print(i.price, i.customer.name)
    print('ji')
    return render(request, 'hi.html', context={
        'customerList': customerList,
        'hi': 'jeifj;fijfil',
    })

def hi(request):
    return HttpResponse("你靠邀")