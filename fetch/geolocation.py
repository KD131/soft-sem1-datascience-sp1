from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='python-school-cphbusiness')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def geolocation(address):
    loc = geocode(address)
    # could use a dict to specify the format, but then I have to worry about formatting. Not all the city names are valid either.
    # a straight search is easier to do
    return (loc.latitude, loc.longitude) if loc else (None, None)