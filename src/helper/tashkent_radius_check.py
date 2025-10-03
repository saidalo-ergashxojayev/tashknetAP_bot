from shapely.geometry import Point, shape
import json

def is_in_tashkent(lat, lon, geojson_file="tashkent_city.geojson"):
    with open(geojson_file, "r", encoding="utf-8") as f:
        geo = json.load(f)

    point = Point(lon, lat)  # shapely expects (x=lon, y=lat)

    for feature in geo["features"]:
        polygon = shape(feature["geometry"])
        if polygon.contains(point):
            return True
    return False
