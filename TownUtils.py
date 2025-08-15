from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from typing import Optional, Tuple

def getDistance(town1: str, town2: str) -> float:
    geolocator = Nominatim(user_agent="town_locator")
    location1 = geolocator.geocode(town1)
    location2 = geolocator.geocode(town2)
    if location1 and location2:
        return geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude))
    return None

  
print(getDistance("Novi Sad", "Niš"))