import logging
from DB import connect


cur, conn = connect.db_connect()

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def get_forecast(lon, lat):
    try:
        cur.execute(f"""select * from forecast where longitude = '{lon}' and latitude = '{lat}';""")
        return cur.fetchall()
    except Exception as e:
        logging.error(e)
        return


def get_min_forecast(lon, lat):
    try:
        cur.execute(f"""select min (temperature_celsius) from forecast where longitude = '{lon}' and latitude = '{lat}'
        union select min (precipitation_rate) from forecast where longitude = '{lon}' and latitude = '{lat}';""")
        return cur.fetchall()
    except Exception as e:
        logging.error(e)
        return


def get_max_forecast(lon, lat):
    try:
        cur.execute(f"""select max (temperature_celsius) from forecast where longitude = '{lon}' and latitude = '{lat}'
        union select max (precipitation_rate) from forecast where longitude = '{lon}' and latitude = '{lat}';""")
        return cur.fetchall()
    except Exception as e:
        logging.error(e)
        return


def get_avg_forecast(lon, lat):
    try:
        cur.execute(f"""select avg (temperature_celsius) from forecast where longitude = '{lon}' and latitude = '{lat}'
        union select avg (precipitation_rate) from forecast where longitude = '{lon}' and latitude = '{lat}';""")
        return cur.fetchall()
    except Exception as e:
        logging.error(e)
        return
