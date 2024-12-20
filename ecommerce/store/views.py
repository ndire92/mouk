from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Cart, CartItem, Order, Feedback

# Vue pour la page d'accueil
def home(request):
    categories = Category.objects.all()  # Liste des catégories
    products = Product.objects.all()[:6]  # Exemple : 6 produits récents
    return render(request, 'ecommerce/home.html', {'categories': categories, 'products': products})

# Vue pour la liste des catégories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'ecommerce/category_list.html', {'categories': categories})

# Vue pour les produits d'une catégorie
def product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'ecommerce/product_list.html', {'category': category, 'products': products})

# Vue pour tous les produits
def product_list_all(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

# Vue pour le détail d'un produit
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'ecommerce/product_detail.html', {'product': product})

# Vue pour afficher le panier
@login_required
def cart_detail(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'ecommerce/cart.html', {'cart': cart})

# Vue pour ajouter un produit au panier
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = cart.cart_items.get_or_create(product=product)

    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

# Vue pour supprimer un produit du panier
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart_detail')

# Vue pour passer une commande
@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if cart.cart_items.exists():
        for item in cart.cart_items.all():
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity,
                shipping_address=request.user.customer_profile.address
            )
        cart.cart_items.all().delete()  # Vider le panier après la commande
        return redirect('order_list')
    return redirect('cart_detail')

# Vue pour afficher les commandes
@login_required
def order_list(request):
    orders = request.user.orders.all()
    return render(request, 'ecommerce/order_list.html', {'orders': orders})

# Vue pour la caisse
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'ecommerce/checkout.html', {'cart': cart})

# Vue pour ajouter un avis sur un produit
@login_required
def add_feedback(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')
        Feedback.objects.create(
            customer=request.user.customer_profile,
            product=product,
            feedback=feedback_text
        )
        return redirect('product_detail', product_id=product.id)
    return render(request, 'ecommerce/add_feedback.html', {'product': product})

# Vue pour afficher le profil utilisateur
@login_required
def profile(request):
    return render(request, 'ecommerce/profile.html', {'customer': request.user.customer_profile})

# Vue pour mettre à jour le profil utilisateur
@login_required
def update_profile(request):
    customer = request.user.customer_profile
    if request.method == 'POST':
        customer.address = request.POST.get('address', customer.address)
        customer.mobile = request.POST.get('mobile', customer.mobile)
        if 'profile_pic' in request.FILES:
            customer.profile_pic = request.FILES['profile_pic']
        customer.save()
        return redirect('profile')
    return render(request, 'ecommerce/update_profile.html', {'customer': customer})
