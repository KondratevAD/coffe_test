from django.contrib import admin
from .models import CustomUsers, Payments


@admin.register(CustomUsers)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'first_name',
        'last_name',
    )
    search_fields = ('username', 'email')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'price',
        'currency',
        'pay_date',
    )
    search_fields = ('user', 'product')
    list_filter = ('user', 'product', 'pay_date')
