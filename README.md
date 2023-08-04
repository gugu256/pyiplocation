# pyiplocation

A simple python package to geolocate IPs without the need for a paid/limited API.<br>

## Usage

This code snippet :
```py
from pyiplocation import geolocate

geolocate("42.34.78.123")
```
will return a dictionary containing : <br>
- The IP
- The Hostname
- The Continent Code
- The Continent Name
- The Country Codes
- The Country Name
- The Country Capital
- The State/Province
- The District/County
- The City
- The Zip Code
- The City's Latitude
- The City's Longitude
- The Country's Currency
- The Timezone (name, offset, current time etc..)
- The Calling Code

### And more!