import requests

def geolocate(ip: str):
    page = requests.get("https://ipgeolocation.io/ip-location/" + ip).text
    page = page.split("\n")
    return {
        "ip": ip,
        "hostname": page[152].replace("<td>", "").replace("</td>", ""),
        "continent_code": page[156].replace("<td>", "").replace("</td>", ""),
        "continent_name": page[160].replace("<td>", "").replace("</td>", ""),
        "country_codes": {
            "alpha-2": page[164].replace("<td>", "").replace("</td>", ""), 
            "alpha-3": page[168].replace("<td>", "").replace("</td>", "")},
        "country_name": page[172].replace("<td>", "").replace("</td>", ""),
        "country_capital": page[182].replace("<td>", "").replace("</td>", ""),
        "state_province": page[186].replace("<td>", "").replace("</td>", ""),
        "district_county": page[190].replace("<td>", "").replace("</td>", ""),
        "city": page[194].replace("<td>", "").replace("</td>", ""),
        "zip_code": page[198].replace("<td>", "").replace("</td>", ""),
        "latitude": float(page[202].replace("<td>", "").replace("</td>", "").split(", ")[0]),
        "longitude": float(page[202].replace("<td>", "").replace("</td>", "").split(", ")[1]),
        "geoname_id": int(page[206].replace("<td>", "").replace("</td>", "")),
        "is_eu": True if page[210].replace("<td>", "").replace("</td>", "") == "true" else False,
        "calling_code": page[214].replace("<td>", "").replace("</td>", ""),
        "country_tld": page[218].replace("<td>", "").replace("</td>", ""),
        "languages": page[222].replace("<td>", "").replace("</td>", ""),
        "ISP": page[226].replace("<td>", "").replace("</td>", ""),
        "connection_type": page[230].replace("<td>", "").replace("</td>", ""),
        "organization": page[234].replace("<td>", "").replace("</td>", ""),
        "AS_number": page[238].replace("<td>", "").replace("</td>", ""),
        "currency": {
            "name": page[242].replace("<td>", "").replace("</td>", ""),
            "code": page[247][-7:].replace("<td>", "").replace("</td>", "").replace("</a>", ""),
            "name": page[252].replace("<td>", "").replace("</td>", "")},
        "timezone": {
            "name": page[256].replace("<td>", "").replace("</td>", ""),
            "offset": float(page[260].replace("<td>", "").replace("</td>", "")),
            "current_time": page[264].replace("<td>", "").replace("</td>", ""),
            "current_time_unix": page[268].replace("<td>", "").replace("</td>", ""),
            "is_DST": True if page[272].replace("<td>", "").replace("</td>", "") == "true" else False,
            "DST_savings": float(page[276].replace("<td>", "").replace("</td>", ""))}
    }

print(geolocate("79.95.87.19"))