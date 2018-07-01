from django.urls import path
from apps.testsbazadannyh.views import students_page

urlpatterns = [
    path('', students_page, name='students'),
]
