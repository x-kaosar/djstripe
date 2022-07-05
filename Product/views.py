import stripe
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from .models import Product
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY



class SuccessView(TemplateView):
    template_name = 'success.html'

class CancelView(TemplateView):
    template_name = 'cancel.html'

def index(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'index.html', context)

def landing(request,pk):
    products = Product.objects.get(id=pk)
    context = {
        'product':products,
        'STRIPE_PUBLIC_KEY':settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'product-detail.html', context)

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = 'https://djstripe.herokuapp.com'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': int(product.price)*100,
                        'product_data': {
                            'name': product.name,
                            'images': ['https://scontent.fjsr11-1.fna.fbcdn.net/v/t1.6435-9/142422872_1125949994484381_3281419797722937871_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=09cbfe&_nc_eui2=AeF_DNIx0E-Fsl_36eEUV_gIyR7AUimx8znJHsBSKbHzOYKq2tZTZdQ57Zf5-3YvoQHM4Luv3zn4v33hHKaN2vFL&_nc_ohc=3U3VZIVo4A4AX9cHfoN&_nc_ht=scontent.fjsr11-1.fna&oh=00_AT_cvQAI3JHM2AVlqqDDm0hWZ01IB-ADEIKcCvJ-r2CD0w&oe=62E74F83'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": 'product.id'
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        # return redirect(checkout_session.url, code=303)
        return JsonResponse({'id':checkout_session.id})
