import geocoder
g = geocoder.ip('me')
print(g.city)
print(g.country)
print(g.lat)