import wget
from datetime import datetime
import pytz
import time

url = 'http://200.131.64.207/allsky/imagens340/AllSkyCurrentImage.JPG'

# Time Operators
tz_BR = pytz.timezone('Brazil/East')


# Ticking Away~

while (1):

    t = datetime.now(tz_BR)
    hour = int(t.strftime("%H"))
    while ((hour >= 18) or (hour <= 6)):

        t = datetime.now(tz_BR)
        hour = int(t.strftime("%H"))
        aux = ("AllSky", t.strftime("%d-%B-%Y_%H:%M:%S.jpg"))
        name = str("_".join(aux))
        print(hour)
        wget.download(url, name)
        print("File: ", name, "Saved! ")
        time.sleep(60)
    print("It doesn't update during daylight!! \nSleepin for some time...")
    time.sleep(1800)
