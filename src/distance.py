import haversine as hs

#this function will return the distance (in m) between two coordinates
#returns a scalar value
def dist(lat1, lon1, lat2, lon2):
    loc1 = (lat1, lon1)
    loc2 = (lat2, lon2)
    distance_between_km = hs.haversine(loc1,loc2)
    distance_between_m = distance_between_km * 1000
    return distance_between_m