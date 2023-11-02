from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('create_product/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/update/', views.update_product,name='update_product'),
]