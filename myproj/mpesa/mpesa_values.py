#function and values that get attributes from mpesa vals

from django.conf import settings
settings.configure()

import os

from decouple import config, UndefinedValueError


def mpesa_config(key):
	
	value = getattr(settings, key, None)
	if value is None:		
			value = config(key)		
	return value

AM = mpesa_config('MPESA_EXPRESS_SHORTCODE')
AS = mpesa_config('MPESA_PASSKEY')
regc2bshort = mpesa_config('MPESA_REG_SHORTCODE')
c2bshort = mpesa_config('MPESA_CTOB_SHORTCODE')
