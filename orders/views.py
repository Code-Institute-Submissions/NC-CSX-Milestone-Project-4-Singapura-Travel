from django.shortcuts import render
from .models import orders

# Create your views here.

def get_orders(request):

    """ A view to show all products, including sorting and search queries """

    orders = orders.objects.all()

    context = {
        'orders': orders,
    }

    return render(request, 'orders/orders.html', context)