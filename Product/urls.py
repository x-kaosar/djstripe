from django.urls import path

from .views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView,
    index,
    landing,
    
)

urlpatterns = [
    path('', index, name='home'),
    path('products/<str:pk>/', landing, name='landing'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('create-checkout-session/<int:pk>/',CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]