from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('product_detail/<int:id>/', views.index_detail, name='index_detail'),
    path('404/', views.error_404, name='error_404'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/', views.cart, name='cart'),
    path('delete_prod/', views.delete_prod, name='delete_prod'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('product_details/', views.product_details, name='product_details'),
]