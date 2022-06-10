import re

with open('radio_stations.txt', 'r', encoding='utf-8') as exp:
    text = exp.read()
    m = re.findall('https?://([A-Za-z_0-9.-]+).*', text)
    print(m)
