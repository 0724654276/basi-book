from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django_daraja.mpesa.core import MpesaClient
from django.urls import reverse
import requests
from django.shortcuts import render, redirect
from requests.api import get
from requests.auth import HTTPBasicAuth
import json
import re


cl = MpesaClient()
stk_push_callback_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
b2c_callback_url = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'
c2b_callback_url = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'

def getAccessToken(request):
    consumer_key = 'GAeIsGiTzoclVjKZ0lpGkRTKqSOlM4tP'
    consumer_secret = 'il1gZPOjXMF3LeFD'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

def oauth_success(request):
	r = cl.access_token()
	return JsonResponse(r, safe=False)
    

def stk_push_success(request, ph_number,total_amount):
    phone_number = ph_number
    amount = total_amount
    account_reference = 'Store Centre'
    transaction_desc = 'STK Push Description'
    callback_url = stk_push_callback_url
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')



def payment (request):
    if request.method == 'POST':
        name=request.POST.get('fname')
        phone_number=request.POST.get('phone_number')
        amount = request.POST.get("amount")
        ph_number = None
        total_amount = int(amount)
        if phone_number[0] == '0':
            ph_number = '254'+ phone_number[1:]
        elif phone_number[0:2] == '254':
            ph_number = phone_number
        else:
            # messages.error(request, 'Check you Phone Number format 2547xxxxxxxx')
            return redirect(request.get_full_path())


        stk_push_success(request, ph_number,total_amount)

        return render (request,'sucess.html')
        # return HttpResponse(f'Stk Push for {phone_number}')
    
    return render (request,'payment.html', {'title': 'Payment'})