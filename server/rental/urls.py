from django.urls import path

from .views import RentalView, email, StripeCheckouView


app_name = 'cabs'

urlpatterns = [
    path('email/', email, name='email'),
    # path('', RentalView.as_view({'get': 'list'}), name='rental_list'),
    path('', RentalView.as_view(), name='rental_list'),
    path('<uuid:rental_id>/',
         RentalView.as_view(), name='rental_detail'),
    path(r'stripe/create-stripe-checkout-session', StripeCheckouView.as_view()),
]
