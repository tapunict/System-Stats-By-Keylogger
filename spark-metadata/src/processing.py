from deep_translator import GoogleTranslator

from elasticsearch import Elasticsearch

import requests
import json


ES_URL = 'http://elasticsearch:9200'
ES_INDEX = 'keylogger_stats'
ES_MAPPING = {
    "mappings": {
        "properties": {
            "location": {
                "type": "geo_point"
            }
        }
    }
}

es = Elasticsearch(
    ES_URL,
    verify_certs=False
)  

es.indices.create(
    index=ES_INDEX,
    body=ES_MAPPING, # we overwrite the mapping because otherwise, ES sees the "location" field as text
    ignore=400 # ignore error of "index already exists"
)


# -------------------------------------------------------------------- #
# Calculates the difference between timestamp_end and timestamp_begin
# Returns the difference in seconds
# -------------------------------------------------------------------- #

def getDeltaTimestamps(t_begin, t_end):
    tdelta = t_end - t_begin
    delta_secs = tdelta.total_seconds()
    return dict({'delta_secs': delta_secs})

# ---------------------------------------------------- #
# Retrieves via API the public IP address geolocation
# Returns the point coordinates (lat, lng)
# ---------------------------------------------------- #

def getGeoIpCoords(ip_address):
    api_resp = requests.get('https://geolocation-db.com/jsonp/' + ip_address)

    geoip = api_resp.content.decode().split("(")[1]
    geoip = json.loads(geoip[:-1])
    
    latlng = geoip['latitude'] + ', ' + geoip['longitude']
    return dict({'location': latlng})

# -------------------------------------------------- #
# Given the file of titles, it reads all the titles
# Returns a set of titles 
# -------------------------------------------------- #

def loadWindowTitles(path):
    with open(path, 'r') as fd:
        titles = fd.read().split('\n')
        return set(titles)

# --------------------------------------------------------------------------------- #
# Checks if exists a title that is contained in the window title
# If exists, returns a dictionary containing the Application Name and the Category
# Else returns None by default
# --------------------------------------------------------------------------------- #

def checkAndUpdate(titles, window, category):
    for t in titles:
        if t in window:
            return dict({'window': t.title(), 'window_category': category})

# ------------------------------------------------- #
# Loads window titles for each category of window
# Checks if the window belongs to a known category
# Then returns the dictionary with the result(s)
# ------------------------------------------------- #

def getWindowClassification(window):
    social = loadWindowTitles('titles/social.txt')
    utilities = loadWindowTitles('titles/utilities.txt')
    entertainment = loadWindowTitles('titles/entertainment.txt')
    web = loadWindowTitles('titles/web.txt')
    office = loadWindowTitles('titles/office_study.txt')  
    
    if (res := checkAndUpdate(social, window, 'Social')) is not None:
        return res

    if (res := checkAndUpdate(utilities, window, 'Utility')) is not None:
        return res
        
    if (res := checkAndUpdate(entertainment, window, 'Entertainment')) is not None:
        return res

    if (res := checkAndUpdate(web, window, 'Web Browsing')) is not None:
        return res

    if (res := checkAndUpdate(office, window, 'Office & Study')) is not None:
        return res

    return dict({'window_category': 'Other'})


def processBatch(df, id):
    for idx, row in enumerate(df.collect()):
        
        doc = row.asDict()
        doc['window'] = GoogleTranslator(source='auto', target='en').translate(doc['window']).lower()
    
        doc.update(getDeltaTimestamps(doc['timestamp_begin'], doc['timestamp_end']))
        doc.update(getWindowClassification(doc['window']))

        if doc['ip_address'] != "Unknown":
            doc.update(getGeoIpCoords(doc['ip_address']))

        print(doc)

        id_str = '{}-{}-1'
        id = id_str.format(id, idx)

        response = es.index(index=ES_INDEX, id=id, document=doc)
        print(response)