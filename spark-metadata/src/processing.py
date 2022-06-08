from datetime import date, datetime

from deep_translator import GoogleTranslator

from elasticsearch import Elasticsearch


ES_URL = 'http://elasticsearch:9200'
ES_INDEX = 'keylogger'

es = Elasticsearch(
    ES_URL,
    basic_auth=(ES_USER, ES_PSW),
    verify_certs=False
)  


def getDeltaTimestamps(t_begin, t_end):
    tdelta = t_end - t_begin
    delta_secs = tdelta.total_seconds()
    return dict({'delta_secs': delta_secs})

def getHeuristicWindowClassification(window):
    social = [
        'microsoft teams',
        'whatsapp',
        'instagram',
        'facebook',
        'telegram',
        'tiktok',
        'discord',
        'twitter',
        'gmail',
        'google meet',
        'youtube',
        'tumblr',
        'skype',
        'linkedin',
        'inbox'
    ]

    utilities = [
        'calculator',
        'calendar',
        'notepad',
        'snipping tool',
        'command prompt',
        'notepad',
        'settings',
        'control panel',
        'clock',
        'search',
        'programs and features',
        'windows security',
        'photos',
        'word',
        'excel',
        'powerpoint',
        'access',
        'unknown'
    ]

    window = GoogleTranslator(source='auto', target='en').translate(window).lower()  
    
    for s in social:
        if window.find(s) != -1:
            return dict({'window_category': 'Social'})
    
    for u in utilities:
        if window.find(u) != -1:
            return dict({'window_category': 'Utility'})

    return dict({'window_category': 'Other'})


def processBatch(df, id):
    for idx, row in enumerate(df.collect()):
        
        doc = row.asDict()
        doc.update(getDeltaTimestamps(doc['timestamp_begin'], doc['timestamp_end']))
        doc.update(getHeuristicWindowClassification(doc['window']))
        doc['timestamp'] = datetime.now()
        print(doc)

        id_str = '{}-{}-1'
        id = id_str.format(id, idx)

        response = es.index(index=ES_INDEX, id=id, document=doc)
        print(response)
