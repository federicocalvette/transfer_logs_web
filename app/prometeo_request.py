import requests
import settings


def get_transfer_logs(date_start, date_end, apikey):

    URL = settings.URL + f"?date_start={date_start}&date_end={date_end}"

    headers = {
        'x-api-key': apikey
    }

    response = requests.request("GET", URL, headers=headers)

    if settings.DEBUG: print(response.json())

    return response.json()
