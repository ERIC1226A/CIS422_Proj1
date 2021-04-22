"""
pip install geopy
pip install haversine


"""

import haversine as hs
from geopy.geocoders import Nominatim



def distance(address):
    
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(address)
    
    print(location.address)
    
    consumer = ((location.latitude, location.longitude))
    print("consumer address: " + str(location.latitude) + " " +str(location.longitude))

    #need to find actural addi for vaccine_providor
    vaccine_providor = (28.394231,77.050308)
    num = hs.haversine(consumer,vaccine_providor)
    print("address to providor distance: " + str(num) + " km")

def main():
    
    address = ("5014 157th Court Northeast")
    distance(address)


if __name__ == '__main__':
    main()
