import requests
from decouple import config, UndefinedValueError


from access_token import generate_access_token
from mpesa_values import *
import keys

def register_url():
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {          
    
    "ShortCode":regc2bshort,
    "ResponseType": "Completed",
    "ConfirmationURL": "https://git.heroku.com/gymplann.git",
    "ValidationURL":"https://git.heroku.com/gymplann.git"
   
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

register_url()

def c2b_simulate():

    access_token = generate_access_token()

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {    

   "ShortCode":c2bshort,
   "Command ID": "CustomerPayBillOnline",
   "Amount":"1",
   "Msisdn":"254701581799", 
   "BillRefNumber":"00000"   

    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

c2b_simulate()