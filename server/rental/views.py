from django.shortcuts import render
from .models import Rental, Email
from rest_framework import  permissions, viewsets
from .serializers import RentalSerializer , EmailSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

from django.conf import settings

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeCheckouView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1M5ENpFMeCnnC3tGULsHZtjy',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=settings.SITE_URL +'/success',
                cancel_url=settings.SITE_URL + '/cancel',
            )

            return redirect(checkout_session.url,)
        except Exception as e:
            return Response(
                {'error': 'Something went wrong while creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class RentalView(APIView):
    """
    List all Rentals, or create a new Rental.
    """

    def get(self, request, format=None):
        rental = Rental.objects.all()
        serializer = RentalSerializer(rental, many=True)
        return Response(serializer.data)

    def post(self, request, format=None, *args, **kwargs):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
            try:
                checkout_session = stripe.checkout.Session.create(
                    line_items=[
                        {
                            # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                            'price': 'price_1M5ENpFMeCnnC3tGULsHZtjy',
                            'quantity': 1,
                        },
                    ],
                    mode='payment',
                    success_url=settings.SITE_URL + '/success',
                    cancel_url=settings.SITE_URL + '/cancel',
                )
                return Response(checkout_session.url, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(
                    {'error': 'Something went wrong while creating stripe checkout session'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def email(request):

    if request.method == "POST":
        subject = "Asap Cab Services"
        message ="Hi, Thankyou for renting a car from us, You'll be updated on how to get the car"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [EmailSerializer.email,]
        send_mail(subject, message, email_from, recipient_list)
        return HttpResponse("Email Sent")
    return HttpResponse("Rent Car by Submitting your email")
