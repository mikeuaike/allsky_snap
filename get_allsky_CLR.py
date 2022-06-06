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
i = 0
while (1):
    while (hour >= 18 or hour <= 6):

        t = datetime.now(tz_BR)
        i_name = str(i).zfill(5)
        aux = ("AllSky", i_name, '.jpg')
        name = str("_".join(aux))

        wget.download(url, name)
        print("File: ", name, "Saved! ")
        i = i + 1
        time.sleep(60)
    time.sleep(1800)
