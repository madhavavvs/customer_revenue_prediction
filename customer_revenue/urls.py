from django.contrib import admin
from django.urls import path
# from customer_revenue import views
from customer_revenue import views
urlpatterns = [
    path("", views.index, name='home'),
    # path('', first, name='homepage'),
    path("contact", views.contact, name='contact'),
    path("customer", views.first, name='homepage'),
]
