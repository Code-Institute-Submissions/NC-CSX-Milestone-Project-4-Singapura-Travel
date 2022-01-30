from django.shortcuts import render
from .models import Package

# Create your views here.

def get_packages(request):

    """ A view to show all products, including sorting and search queries """

    packages = Package.objects.all()

    context = {
        'packages': packages,
    }

    return render(request, 'packages/packages.html', context)