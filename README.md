# allsky_snap
Automatically downloads image from LNA's public AllSky Camera!

# What is the LNA?
LNA stands for "Laboratório Nacional de Astrofísica", or "Astrophysics National Laboratory, a research institute focused on Astronomy.
By having access to 3 observatories, it provides the observational infrastructure for national astronomy.

# AllSky Camera
The institute publically provides image from an allsky camera, used for forecast purposes, but the images also can be used for enthusiasts to make some cool time lapses from the sky. As an example, the link below shows a time lapse from GEMINI's allsky camera during a lunar eclipse :
> https://twitter.com/usngo/status/1526336287749263362

# Libraries
To run this code, you'll need the following python libraries:
> wget
> datetime
> pytz
> time

# Specs
## Monochromatic Camera
###### It uploads image with a higher exposition time, when compared to the colored one. The image updates only happen between 6PM and 6 AM (UTC-3), and they're updated by the minute

## Colored Camera
###### Despite having a lower exposition time than the monochromatic one, the colored one gives colored image and it's updated 24/7!

