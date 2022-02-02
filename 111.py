from Samples.mapapi_PG import show_map
from Samples.geocoder import get_coordinates, get_ll_span
from Samples.business import find_business, find_businesses
from Samples.distance import lonlat_distance
import sys

adress = ' '.join(sys.argv[1:])
lon, lat = get_coordinates(adress)
res = get_ll_span(adress)
param1 = f'{lon},{lat}'
param2 = "&spn=3,3"
result = find_business(param1, res[1], 'аптека')
result_coords_apt = result["geometry"]["coordinates"]
adr = result["properties"]["description"]
name = result["properties"]["name"]
t = result["properties"]["CompanyMetaData"]["Hours"]["text"]
s = lonlat_distance([lon, lat], result_coords_apt)
d = round(float(s) * 0.00001, 4)
lon_apt, lat_apt = result_coords_apt
print(f"Название: {name}, Адрес: {adr}, Часы работы: {t}, Расстояние: {s}")
show_map(ll_spn=f"ll={res[0]}&spn={d},{d}", add_params=f"pt={lon_apt},"
        f"{lat_apt},pmntl1~{lon},{lat},pm2rdm")
