import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import base64

class MpesaClient:
    def __init__(self):
        self.consumer_key = 'RcnrrUMXxDMGVg5tcWMGYHAfI77o1qoz8Z2RnzOFGINeepQB'
        self.consumer_secret = 'ueVewvcGSsMyqzX08tt9Rt9lL5IxOeqQl2succfZh1r7x9iy8bi5hGhhAPA72IVm'
        self.shortcode = '174379'
        self.passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        self.base_url = 'https://sandbox.safaricom.co.ke'

    def get_access_token(self):
        url = f'{self.base_url}/oauth/v1/generate?grant_type=client_credentials'
        try:
            response = requests.get(url, auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret))
            response.raise_for_status()
            response_data = response.json()
            access_token = response_data.get('access_token')
            if access_token:
                return access_token
            else:
                print("Access token not found in response:", response_data)
        except requests.RequestException as e:
            print("Error retrieving access token:", e)
        return None


    def stk_push(self, amount, phone_number, account_reference, transaction_desc):
        access_token = self.get_access_token()
        if access_token is None:
            return None

        url = f"{self.base_url}/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": f"Bearer {access_token}"}
        payload = {
            "BusinessShortCode": self.shortcode,
            "Password": self._generate_password(),
            "Timestamp": self._generate_timestamp(),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone_number,
            "PartyB": '174379',
            "PhoneNumber": phone_number,
            "CallBackURL": "https://mydomain.com/pat",
            "AccountReference": "Test",
            "TransactionDesc": "Test"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    def _generate_password(self):
        data_to_encode = self.shortcode + self.passkey + self._generate_timestamp()
        encoded_string = base64.b64encode(data_to_encode.encode())
        return encoded_string.decode('utf-8')

    def _generate_timestamp(self):
        return datetime.now().strftime('%Y%m%d%H%M%S')
