from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),

    # Gestion des catégories et produits
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.product_list, name='product_list'),
    path('products/', views.product_list_all, name='product_list_all'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

    # Gestion du panier
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),

    # Gestion des commandes
    path('orders/', views.order_list, name='order_list'),
    path('order/place/', views.place_order, name='place_order'),

    # Gestion des avis
    path('feedback/add/<int:product_id>/', views.add_feedback, name='add_feedback'),

    # Gestion des profils
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]
