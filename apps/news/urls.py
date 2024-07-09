from django.urls import path
from .views import *

app_name = "news"

urlpatterns = [
    path("", index, name="index"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('news/', news_list, name="news_list"),
    path('news/<int:pk>/', news_detail, name="news_detail"),
    path('product/<int:pk>/', product_details, name="product_detail"),
]