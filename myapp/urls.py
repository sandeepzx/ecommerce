from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('allpro/<int:id>', views.allpro, name='allpro'),
    path('login', views.login1, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('users', views.users, name='users'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('pro_reg', views.pro_reg, name='pro_reg'),
    path('products', views.products, name='products'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete_cart/<int:id>', views.delete_cart, name='delete_cart'),
    path('pdelete/<int:id>', views.pdelete, name='pdelete'),
    path('cat_reg', views.cat_reg, name='cat_reg'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('cart_pro', views.cart_pro, name='cart_pro'),
    path('decr/<int:id>', views.decr, name='decr'),
    path('adds/<int:id>', views.adds, name='adds'),
    path('checkout', views.checkout, name='checkout'),
]