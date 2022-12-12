from ipware import get_client_ip
from django.http import HttpResponse
from django.contrib.gis.geoip2 import GeoIP2
from .models import Visit
import requests

class IPIsValid:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip, is_routable = get_client_ip(request)
        
        response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=40213bf4125645b6b0ef263b4aeaf88f&ip_address=" + ip)
        data = response.json()
        # ip = Visit(ip_address = data['ip_address'], city = data['city'],region = data['region'],country = data['country'],continent = data['continent'],timezone = data['timezone']['current_time'])
        ip = Visit(ip_address = data['ip_address'])
        ip.save()
        response = self.get_response(request)
        return response