import requests
from datetime import datetime
import smtplib
import time
email = "kokatekush96@gmail.com"
password = "qfcr mbnv kqqg wglg"
MY_LAT = 13.082680
MY_LONG = 80.270721
def is_latitude():


    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LONG-5<=iss_longitude<=MY_LAT+5 and MY_LONG-5<=iss_latitude<=MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data['results']["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = datetime.now().hour
    if time_now >= sunrise and time_now <= sunset:
        return True
#close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
 # BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_latitude() and is_night():
        requests = smtplib.SMTP("smtp.gmail.com", 587)
        requests.starttls()
        requests.login(user=email, password=password)
        requests.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:Look up ^\n\n The ISS is above you !")

