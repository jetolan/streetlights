from mapbox import Geocoder

geocoder=Geocoder()

response = geocoder.forward("200 queen street")
print(response.status_code)


