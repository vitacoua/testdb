from django.urls import path
from apps.testsbazadannyh.views import general_page

urlpatterns = [
    path('', general_page, name='home'),
]
