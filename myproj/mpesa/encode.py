#create password
#call it from encode import generate_pass()
#then call it and place in formatted tome

import base64 

from mpesa_values import AM,AS

def generate_pass(formatted_time):
    
    password = base64.b64encode((AM + AS + formatted_time).encode('ascii')).decode('utf-8') 

    return password
