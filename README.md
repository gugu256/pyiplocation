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
- The Geoname ID
- A Boolean indicating whether or not the IP is in the EU
- The Calling Code
- The Country TLD
- The Country Languages
- The ISP
- The Connection Type
- The Organization
- The AS Number
- The Country's Currency (name, code, symbol)
- The Timezone (name, offset, current time etc..)

### And more!