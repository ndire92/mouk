from django.contrib import admin
from .models import Category, Product, Customer, Cart, CartItem, Order, Feedback


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category', 'created_at')
    list_filter = ('category', 'created_at', 'price')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    autocomplete_fields = ('category',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'mobile', 'address', 'user')
    search_fields = ('user__username', 'mobile', 'address')
    list_filter = ('user__is_active',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price')
    list_filter = ('created_at',)
    search_fields = ('user__username',)

    @admin.display(description='Total Price')
    def total_price(self, obj):
        return f"{obj.total_price():.2f} FCFA"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'total_price')
    search_fields = ('product__name', 'cart__user__username')

    @admin.display(description='Total Price')
    def total_price(self, obj):
        return f"{obj.total_price():.2f} FCFA"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'status', 'ordered_at', 'payment_status')
    list_filter = ('status', 'payment_status', 'ordered_at')
    search_fields = ('user__username', 'product__name', 'shipping_address')
    ordering = ('-ordered_at',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'feedback', 'date')
    list_filter = ('date',)
    search_fields = ('customer__user__username', 'feedback')
