from flask import Flask, request, jsonify
import logging
from DB import db_request, connect
import coordinate_validation
import forecast_summery


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


errors = {'no_args': {'error': 'please provide lon and lat args'},
          'wrong_value': {'error': 'lon must be between -180 to 180 and lat must be between -90 to 90'},
          'no_forecast': {'error': "we don't have forecast for this coordinate"}}
columns_dict = {column_name: connect.columns.index(column_name) for column_name in connect.columns}


def get_args(request_args):
    lon = request_args.get('lon')
    lat = request_args.get('lat')
    if not lon or not lat:
        return None, None
    return lon, lat


def lon_lat_check_and_round(lon, lat):
    try:
        lon = round(float(lon)*2)/2
        lat = round(float(lat)*2)/2
        if -180 <= lon <= 180 and -90 <= lat <= 90:
            return lon, lat
        return None, None
    except Exception:
        return None, None


app = Flask(__name__)


@app.route('/data', methods=['GET'])
def data():
    lon, lat = get_args(request.args)
    if not lon or not lat:
        return jsonify(errors['no_args']), 400
    lon, lat = coordinate_validation.lon_lat_check_and_round(lon, lat)
    if not lon or not lat:
        return jsonify(errors['wrong_value']), 400
    forecasts = db_request.get_forecast(lon, lat)
    if not forecasts:
        return jsonify(errors['no_forecast']), 400
    forecasts_json = []
    for forecast in forecasts:
        forecast_json = dict(forecastTime=forecast[columns_dict['forecast_time']],
                             Temperature=forecast[columns_dict['Temperature_Celsius']],
                             Precipitation=forecast[columns_dict['Precipitation_Rate']])
        forecasts_json.append(forecast_json)
    return jsonify(forecasts_json)


@app.route('/summarize', methods=['GET'])
def summarize():
    lon, lat = get_args(request.args)
    if not lon or not lat:
        return jsonify(errors['no_args']), 400
    lon, lat = coordinate_validation.lon_lat_check_and_round(lon, lat)
    if not lon or not lat:
        return jsonify(errors['wrong_value']), 400
    summarize_dict = forecast_summery.generate(lon, lat)
    if not summarize_dict:
        return jsonify(errors['no_forecast']), 400
    return jsonify(summarize_dict)


if __name__ == '__main__':
    connect.db_connect()
    app.run('0.0.0.0')
