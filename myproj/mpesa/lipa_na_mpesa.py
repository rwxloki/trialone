# Authorization Request in Python ***|
# additions
# added django config settings to enable reading from environment
# variables, the settings.configure to call it .
# Made a fn that will use those settings to read from env variables
# created env variables to store the data 
# an option to use keys.py .
# tweaked settings alittle with the django.config
# had installed decuple but it was not reading config well so unistalled it
# deleted it actually coz it was annoying then installed python decouple


from django.conf import settings
settings.configure()
import base64 
from datetime import datetime

import requests

import keys

import os
#from dotenv import load_dotenv

# load_dotenv()

# AM = os.getenv('MPESA_EXPRESS_SHORTCODE')
# AS = os.getenv('MPESA_PASSKEY')

from decouple import config, UndefinedValueError
#from python.decouple import config
import os
from requests import Response



def mpesa_config(key):
	"""
	Get Mpesa configuration variable with the matching key
	
	Arguments:
		key (str) -- The configuration key

	Returns:

		str: Mpesa configuration variable with the matching key

	Raises:
		MpesaConfigurationException: Key not found
	"""

	value = getattr(settings, key, None)
	if value is None:
		#try:
			value = config(key)
		#except UndefinedValueError:
			# Check key in settings file
			#raise MpesaConfigurationException('Mpesa environment not configured properly - ' + key + ' not found')

	return value

AM = mpesa_config('MPESA_EXPRESS_SHORTCODE')
AS = mpesa_config('MPESA_PASSKEY')



####################################

# phone_number = format_phone_number(phone_number)
# 		url = api_base_url() + 'mpesa/stkpush/v1/processrequest'
# 		passkey = mpesa_config('MPESA_PASSKEY')
		
# 		mpesa_environment = mpesa_config('MPESA_ENVIRONMENT')
# 		if mpesa_environment == 'sandbox':
# 			business_short_code = mpesa_config('MPESA_EXPRESS_SHORTCODE')
# 		else:
# 			business_short_code = mpesa_config('MPESA_SHORTCODE')

# 		timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

# MPESA_ENVIRONMENT = sandbox
# MPESA_CONSUMER_KEY = Xa2gIgRqQDCRHNMGqdcjd4wI908HWUsT
# MPESA_CONSUMER_SECRET = vcqcJNWAIDwhMwtF
# LNM_PHONE_NUMBER = 254701581799
# MPESA_PASSKEY = bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919
# MPESA_EXPRESS_SHORTCODE = 174379
###############################################################################


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

password = base64.b64encode((AM + AS + formatted_time).encode('ascii')).decode('utf-8') 
# data_to_encode = keys.business_shortCode + keys.lipa_na_mpesa_passkey + formatted_time
# encoded_string = base64.b64encode(data_to_encode.encode)

# decoded_password = encoded_string.decode('utf-8')
# print(decoded_password)
#import requests
from requests.auth import HTTPBasicAuth

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))
json_response = r.json()
#r.json()['access_token']
my_access_token = json_response["access_token"]
'''
response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': 'Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' })
print(response.text.encode('utf8'))
{
  "access_token": "ke4NOZXAIWjLk0EYL2RsT9Sks535",
  "expires_in": "3599"
}
'''

def lipa_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    #querystring = {"grant_type":"client_credentials"}
    #payload = ""
    #headers = {"Authorization": "Basic SWZPREdqdkdYM0FjWkFTcTdSa1RWZ2FTSklNY001RGQ6WUp4ZVcxMTZaV0dGNFIzaA=="}
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
          
    "BusinessShortCode":keys.business_shortCode,    
    "Password": password,    
    "Timestamp":formatted_time,    
    "TransactionType": "CustomerPayBillOnline",    
    "Amount":"1",    
    "PartyA":keys.phoneNumber,    
    "PartyB":keys.business_shortCode,    
    "PhoneNumber":keys.phoneNumber,    
    "CallBackURL":"https://darajambili.herokuapp.com/express-payment",    
    "AccountReference":"Loice Did this",    
    "TransactionDesc":"Mytrial one "
    
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)

lipa_mpesa()