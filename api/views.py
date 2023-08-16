from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .serializers import UserSerializer, PaymentSerializer
from .models import CustomUsers, Payments


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def get_queryset(self):
        if self.request.user.is_admin:
            return CustomUsers.objects.all()
        else:
            return CustomUsers.objects.filter(id=self.request.user.id).all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    def get_queryset(self):
        if self.request.user.is_admin:
            qs = Payments.objects.all()
        else:
            qs = Payments.objects.filter(user_id=self.request.user.id).all()
        date = self.request.query_params.get('date', None)
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        try:
            if date_to:
                date_to = datetime.strptime(date_to, "%Y-%m-%d").date()
            if date_from:
                date_from = datetime.strptime(date_from, "%Y-%m-%d").date()
            if date:
                date = datetime.strptime(date, "%Y-%m-%d").date()
        except Exception as e:
            raise ValidationError(
                detail={
                    'error': 'Invalid date format. Must be YYYY-MM-DD'})
        if date_to and date_from and date_from > date_to:
            raise ValidationError(
                detail={
                    'error': 'date_from cannot be earlier than date_to'})
        if date:
            qs = qs.filter(
                pay_date__day=date.day,
                pay_date__month=date.month,
                pay_date__year=date.year
            )
        else:
            if date_from:
                qs = qs.filter(pay_date__gt=date_from)
            if date_to:
                qs = qs.filter(pay_date__lt=date_to)
        return qs
