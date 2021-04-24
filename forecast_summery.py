from DB import db_request


def format_forecast_sum_dict(temp_and_prec_response):
    if len(temp_and_prec_response) == 1:
        return
    if not temp_and_prec_response[0] or not temp_and_prec_response[1]:
        return
    temperature = temp_and_prec_response[0][0]
    precipitation = temp_and_prec_response[1][0]
    return dict(Temperature=round(temperature, 2),
                Precipitation=round(precipitation, 2))


def generate(lon, lat):
    min_dict = format_forecast_sum_dict(db_request.get_min_forecast(lon, lat))
    max_dict = format_forecast_sum_dict(db_request.get_max_forecast(lon, lat))
    avg_dict = format_forecast_sum_dict(db_request.get_avg_forecast(lon, lat))
    if not min_dict or not max_dict or not avg_dict:
        return
    summarize_dict = dict(min=min_dict,
                          max=max_dict,
                          avg=avg_dict)
    return summarize_dict
