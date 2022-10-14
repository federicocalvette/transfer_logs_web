import requests
import settings


def get_transfer_logs(date_start, date_end):

    URL = settings.URL + f"?date_start={date_start}&date_end={date_end}"

    headers = {
        'x-api-key': settings.API_KEY
    }

    response = requests.request("GET", URL, headers=headers)

    return response.json()
