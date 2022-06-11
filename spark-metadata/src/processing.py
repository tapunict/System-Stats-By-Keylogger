from datetime import date, datetime

from deep_translator import GoogleTranslator
from elasticsearch import Elasticsearch


ES_URL = 'http://elasticsearch:9200'
ES_INDEX = 'keylogger_stats'

es = Elasticsearch(
    ES_URL,
    verify_certs=False
)  


def getDeltaTimestamps(t_begin, t_end):
    tdelta = t_end - t_begin
    delta_secs = tdelta.total_seconds()
    return dict({'delta_secs': delta_secs})

def loadWindowTitles(path):
    with open(path, 'r') as fd:
        return fd.read().split('\n')

def getWindowClassification(window):
    social = loadWindowTitles('titles/social.txt')
    utilities = loadWindowTitles('titles/utilities.txt')
    entertainment = loadWindowTitles('titles/entertainment.txt')
    web = loadWindowTitles('titles/web.txt')
    office = loadWindowTitles('titles/office_study.txt')

    window = GoogleTranslator(source='auto', target='en').translate(window).lower()  
    
    if any(t in window for t in social):
        return dict({'window_category': 'Social'})

    if any(t in window for t in utilities):
        return dict({'window_category': 'Utility'})

    if any(t in window for t in entertainment):
        return dict({'window_category': 'Entertainment'})

    if any(t in window for t in web):
        return dict({'window_category': 'Web Browsing'})

    if any(t in window for t in office):
        return dict({'window_category': 'Office & Study'})

    return dict({'window_category': 'Other'})


def processBatch(df, id):
    for idx, row in enumerate(df.collect()):
        
        doc = row.asDict()
        doc.update(getDeltaTimestamps(doc['timestamp_begin'], doc['timestamp_end']))
        doc.update(getWindowClassification(doc['window']))
        print(doc)

        id_str = '{}-{}-1'
        id = id_str.format(id, idx)

        response = es.index(index=ES_INDEX, id=id, document=doc)
        print(response)
