from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView
# from store.views import e_handler404, e_handler500
# handler404 = e_handler404
# handler500 = e_handler500


app_name = "store"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('theme/', toggleTheme, name='theme'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='store:home'), name='logout'),
    
    # # Product URLs
    path('products/', ProductListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # # Order URLs
    # path('orders/', OrderListView.as_view(), name='order_list'),
    # path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:id>/create/', OrderCreateView.as_view(), name='order_create'),
    path('cart/', CartView.as_view(), name='cart'),
    path('order/confirm/', OrderConfirmView.as_view(), name='order_confirm'),
    # path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    # path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]
