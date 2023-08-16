from rest_framework import serializers
from .models import CustomUsers, Payments


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email',
            'role'
        )
        model = CustomUsers


class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        fields = (
            'id', 'user', 'product', 'price', 'currency', 'pay_date',
        )
        model = Payments
