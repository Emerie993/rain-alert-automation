import os
import requests
from twilio.rest import Client


# OWM_API_KEY = "1a009c627b74792d25715e0a99a91ade"
# sid = "ACb1e0b1854c69799e9a81a0c43921c952"
# token = "d7c86c771c7306788ee9a4034777aecc"
MY_LAT = 6.852290
MY_LONG = 7.395650

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
account_token = os.environ["ACCOUNT_TOKEN"]
account_sid  = os.environ["ACCOUNT_SID"]
owm_api_key = os.environ["OWM_API_KEY"]
TEST_LAT = 44.314842
TEST_LONG = -85.602364

parameters ={
    "lat" : TEST_LAT,
    "lon" : TEST_LONG,
    "appid": owm_api_key,
    "cnt" : 4
}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()["list"]


will_rain = False

# This checks if the id the number from the selected hours from the API data reads a value that equal rain
for each_data in weather_data:
    weather_id = each_data["weather"][0]["id"]
    if int(weather_id) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, account_token)
    message = client.messages.\
        create(
        body= "it's going to rain today. Remember to bring an umbrella",
        from_="+17372508034",
        to= "+2349016395839")

# else:
#     print("don't bring an Umbrella")
