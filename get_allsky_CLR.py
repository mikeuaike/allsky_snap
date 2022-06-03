import wget
from datetime import datetime
import pytz
import time

# COLORED!!
url = 'http://200.131.64.237:8090/img/allsky340c.jpg'

# Time Operators
tz_BR = pytz.timezone('Brazil/East')
t = datetime.now(tz_BR)


# Ticking Away~
hour = int(t.strftime("%H"))

while (1):
    while (hour >= 18 or hour <= 6):

        t = datetime.now(tz_BR)

        aux = ("AllSky", t.strftime("%H:%M:%S"), t.strftime("%d-%B-%Y"))
        name = str("_".join(aux))

        wget.download(url, name)
        print("File: ", name, "Saved! ")
        time.sleep(60)
    time.sleep(1800)
