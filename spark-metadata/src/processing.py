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
        titles = fd.read().split('\n')
        return set(titles)

def checkAndUpdate(titles, window, category):
    for t in titles:
        if t in window:
            return dict({'window': t.title(), 'window_category': category})

def getWindowClassification(window):
    social = loadWindowTitles('titles/social.txt')
    utilities = loadWindowTitles('titles/utilities.txt')
    entertainment = loadWindowTitles('titles/entertainment.txt')
    web = loadWindowTitles('titles/web.txt')
    office = loadWindowTitles('titles/office_study.txt')  
    
    if (check := checkAndUpdate(social, window, 'Social')) is not None:
        return check

    if (check := checkAndUpdate(utilities, window, 'Utility')) is not None:
        return check
        
    if (check := checkAndUpdate(entertainment, window, 'Entertainment')) is not None:
        return check

    if (check := checkAndUpdate(web, window, 'Web Browsing')) is not None:
        return check

    if (check := checkAndUpdate(office, window, 'Office & Study')) is not None:
        return check

    return dict({'window_category': 'Other'})


def processBatch(df, id):
    for idx, row in enumerate(df.collect()):
        
        doc = row.asDict()
        doc['window'] = GoogleTranslator(source='auto', target='en').translate(doc['window']).lower()
    
        doc.update(getDeltaTimestamps(doc['timestamp_begin'], doc['timestamp_end']))
        doc.update(getWindowClassification(doc['window']))
        print(doc)

        id_str = '{}-{}-1'
        id = id_str.format(id, idx)

        response = es.index(index=ES_INDEX, id=id, document=doc)
        print(response)
