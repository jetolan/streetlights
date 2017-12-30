from mapbox import Geocoder
import os
geocoder=Geocoder()

geocoder.session.params['access_token'] == os.environ['MAPBOX_ACCESS_TOKEN']


response = geocoder.forward("200 queen street")
print(response.status_code)


