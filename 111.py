from Samples.mapapi_PG import show_map
from Samples.geocoder import get_coordinates, get_ll_span
from Samples.business import find_business, find_businesses
from Samples.distance import lonlat_distance
import sys

adress = ' '.join(sys.argv[1:])
lon, lat = get_coordinates(adress)
res = get_ll_span(adress)
print(res[1])
param1 = f'{lon},{lat}'
print(param1)
param2 = "&spn=3,3"
result = find_business(param1, res[1], 'аптека')
result_coords_apt = result["geometry"]["coordinates"]


lon_apt, lat_apt = result_coords_apt
show_map(ll_spn=f"ll={res[0]}&spn=0.005,0.005", add_params=f"pt={lon_apt},{lat_apt},pm2rdm")