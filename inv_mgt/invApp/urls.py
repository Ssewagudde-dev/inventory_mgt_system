from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create', views.add_product_view, name='add_product'),
    path('list/', views.product_list_view, name='product_list'),
    path('update/<int:product_id>/', views.update_product_view, name='product_update'),
    path('delete/<int:product_id>/', views.delete_product_view, name='product_delete'),
]