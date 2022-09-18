# pip install phonenumbers
# pip install folium
# pip install opencage


from phonenumbers import geocoder
from phonenumbers import carrier

number = int(input("Enter any number ")) 
country = geocoder.parse(number , 'en') 
service_pro = carrier.parse(number, 'en') 
