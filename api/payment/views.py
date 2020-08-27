from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# Import braintree lib can be install using {pip install django-braintree}
import braintree

# gateway variable to configure keys (private, public)
gateway = braintree.BraintreeGateway(
	braintree.Configuration(
		braintree.Environment.Sandbox,
		merchant_id = "pwqgv6k2zbkb8p3k",
		public_key = "cvw7mmsxjn6pft65",
		private_key = "9a0dac1e68add9ac315537562b3502ad",
	)
)

# Validate user session to process payment
def validate_user_session(id, token):
    UserModel = get_user_model()
    
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except UserModel.DoesNotExist:
        return False

# Generate token using braintree api and return it back to user for generate nounce at UI side
@csrf_exempt
def generate_token(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid Session, Please login again!'})
    return JsonResponse({'clientToken': gateway.client_token.generate(), 'success': True})

# Collect nounce and send it to braintree server for processing and collect result
@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'Invalid Session, Please Login Again!!!'})
    
    nounce_from_client = request.POST['paymentMethodNounce']
    amount_from_the_client = request.POST['amount']
    
    result = gateway.transaction.sale({
        "amount": amount_from_the_client,
        "payment_method_nounce": nounce_from_client,
        "options": {
            "submit_for_settlement": True
        }
    })
    if result.is_sucess:
        return JsonResponse({
            'success':result.is_success,
            'transaction': {'id': result.transaction.id, 'amount': result.transaction.amount}
        })
    else:
        return JsonResponse({'error': True, 'success': False})