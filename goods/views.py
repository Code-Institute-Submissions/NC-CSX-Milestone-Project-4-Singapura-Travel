from django.shortcuts import render
from .models import Goods

# Create your views here.

def get_goods(request):

    """ A view to show all products, including sorting and search queries """

    goods = Goods.objects.all()

    context = {
        'goods': goods,
    }

    return render(request, 'goods/goods.html', context)