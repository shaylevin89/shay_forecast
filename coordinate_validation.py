

def lon_lat_check_and_round(lon, lat):
    try:
        lon = round(float(lon)*2)/2
        lat = round(float(lat)*2)/2
        if -180 <= lon <= 180 and -90 <= lat <= 90:
            return lon, lat
        return None, None
    except Exception:
        return None, None
