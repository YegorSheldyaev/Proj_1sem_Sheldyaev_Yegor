# В исходном текстовом файле (radio_stations.txt) найти все домены из
# URL-адресов (например, в URL-адресе http://stream.hoster.by:8081
# /pilotfm/audio/icecast.audio домен выделен полужирным).

import re

with open('radio_stations.txt', 'r', encoding='utf-8') as exp:
    text = exp.read()
    m = re.findall('https?://([A-Za-z_0-9.-]+).*', text)
    print(m)
