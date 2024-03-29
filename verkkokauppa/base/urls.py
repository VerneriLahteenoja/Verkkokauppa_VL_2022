from django.urls import path
from . import views

# profile page eventually
urlpatterns = [
    path('', views.home, name='home-page'),
    path('store/', views.store, name='store-page'),
    path('about/', views.about, name='about-page'),
    path('store/product/<int:category_id>', views.products, name='product-page'),
]