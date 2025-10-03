from config.consts import DISTRICTS, DISTRICTS_LONG_LAT

def get_long_lat(district: str) -> tuple:
    for dist, name in DISTRICTS.items():
        if name == district:
            return DISTRICTS_LONG_LAT[dist]
    return None