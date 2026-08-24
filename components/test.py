import phonenumbers
from phonenumbers import geocoder

# Pass a real phone number string with the '+' prefix
phone_number = phonenumbers.parse("+919876543210")

# This will successfully print the location (e.g., "India")
print(geocoder.description_for_number(phone_number, 'en'))
