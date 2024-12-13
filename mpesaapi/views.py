from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .mpesa_client import MpesaClient
from .forms import MpesaForm
import json
# mpesaapi/views.py
from django.shortcuts import render

def mpesa(request):
    if request.method == "POST":
        # Handle the M-Pesa form submission logic here if needed
        pass
    return render(request, 'mpesa.html')


# Create your views here.
@csrf_exempt
def stk_push(request):
    if request.method == "POST":
        form = MpesaForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            if not phone_number.startswith('254'):
                phone_number = '254' + phone_number[-9:]

            # Define other parameters
            amount = 100  # Example static amount, or compute dynamically if needed
            account_reference = 'Order12345'  # Static or computed value
            transaction_desc = 'Payment for Order'  # Static or computed value

            mpesa_client = MpesaClient()
            response = mpesa_client.stk_push(amount, phone_number, account_reference, transaction_desc)

            return JsonResponse(response)
        else:
            return JsonResponse({"error": "Invalid form data"}, status=400)
    else:
        form = MpesaForm()
        return render(request, 'mpesa.html', {'form': form})


@csrf_exempt
def callback(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Accepted"})



