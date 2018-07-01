from django.shortcuts import render

# Create your views here.


def students_page(request):
    return render(request, 'testsbazadannyh/list_user.html')
