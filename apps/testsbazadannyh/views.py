from django.shortcuts import render

# Create your views here.


def general_page(request):
    return render(request, 'testsbazadannyh/index.html')
