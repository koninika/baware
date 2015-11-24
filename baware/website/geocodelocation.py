from geopy.geocoders import Nominatim

def getlat(addr):
	geolocator = Nominatim()
	location = geolocator.geocode(addr)
	return (location.latitude, location.longitude)
