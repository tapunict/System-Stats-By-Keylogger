# System-Stats-By-Keylogger
_Project of Technologies for Advanced Programming_

_Antonio Scardace_ @ 
_Dept of Math and Computer Science, University of Catania_

## Introduction

The course aims to study and use technologies useful to build end-to-end solutions to analyze, manage, store, process, and visualize data acquired in real-time. For instance, we have seen: Docker containers, and pipelines built with Logstash (for data ingestion), Kafka (for data streaming), Spark (for data processing), ElasticSearch (for data storing), and Kibana (for data visualization). 

### Data Source: Windows Keylogger

The data source is a Windows Keylogger :warning: written and used just on my computer for academic purposes. <br/>
It has been developed in C++ and uses Windows APIs. <br/>
It sends a log to the TCP server on each foreground window change OR after 1 minute of user inactivity.

The log has the following pattern:
```
[GUID] :: [Window Title] :: [Timestamp Start]
Text logged...
[Timestamp End]
```

Each log is composed by:
- **GUID**: Identifies the PC univocally. Has the following format: 00000000-0000-0000-0000-000000000000.
- **Window Title**: Is the title of the window where the user has typed.
- **Text logged**: Is the set of keys pressed by the user and logged by the keylogger.
- **Timestamp Start**: Indicates when the user started typing in that window.
- **Timestamp End**: Indicates when the user finished typing in that window.

For instance:
```
[08E9C0E6-CF7D-43F7-922D-0D6E3B204F8A] :: [Untitled - Notepad] :: [2022-01-01 12:30:00]
Hello Wot[BACKSPACE]rld!
[2022-01-01 12:31:37]

[08E9C0E6-CF7D-43F7-922D-0D6E3B204F8A] :: [Calculator] :: [2022-01-01 12:32:46]
50+50[ENTER]/4
[2022-01-01 12:33:00]
```

### Server System

There is a socket which receives the log and passes it to the pipeline described above and illustrated below:
<p align="center"> <img src="docs/images/pipeline.png?v=1653225037" height="440px"/> </p>

The purpose of the project is to make stats on the use of the system by the user. <br/>
Specifically, the following functions are available:
- For Text Analysis:
    + Frequency statistics about pressed keys :chart_with_upwards_trend:
    + Sentiment analysis :sparkles:
- For Windows and Timestamps:
    + Type of window classification (social, game, utility, others) :iphone:
    + How much time the user spends on each category of windows :eyes:
    + How much time the user spends writing to the PC :clock9:

Additionally, this project was created as an exam project, to test and practice the following skills:
* Knowledge of Docker
* Knowledge of Data Ingestion via Logstash
* Knowledge of Data Streaming via Kafka
* Knowledge of Data Processing via Spark 
* Knowledge of Data Storage via ElasticSearch
* Knowledge of Data Visualization via Kibana
* Knowledge of Jupyter Notebook (for the presentation)
* Good coding skills (legible, reliable, documentation, etc.) :computer:

## Structure

Let's see the structure of the project and how I have used all the components:

<img src="docs/logos/docker-logo.png?v=1653175210" width="150px" />

Each of the following components used has been put inside a **Docker Container**. <br/>

Component | Utility
----- | -------
<img src="docs/logos/python-logo.png" width="150px" /> | I used it to...
<img src="docs/logos/logstash-logo.png" width="150px" /> | **Logstash** is an open-source data collection engine with real-time pipelining capabilities. Logstash can dynamically unify data from disparate sources and normalize the data into destinations of your choice.<br/><br/> I used it to...
<img src="docs/logos/kafka-logo.png?v=1653055181" width="150px" /> | **Apache Kafka** is a distributed data streaming platform that can handle and process streams of records in real-time. It is designed to handle data streams from multiple sources and deliver them to numerous consumers.<br/><br/> I used it to...
<img src="docs/logos/elasticsearch-logo.png" width="150px" /> | **Elasticsearch** is a search engine, and is the heart of the ELK Stack. It centrally stores data for lightning fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.<br/><br/> I used it to...
<img src="docs/logos/spark-logo.png" width="150px" /> | **Spark** is a unified analytics engine for large-scale data processing in real-time.<br/><br/> I used it to...
<img src="docs/logos/kibana-logo.png?v=1653055181" width="150px" /> | **Kibana** is a free front-end application that sits on top of the ELK Stack, providing search and data visualization capabilities for data indexed in ElasticSearch. Commonly known as the charting tool for the ELK Stack, Kibana also acts as the UI for monitoring and managing.<br/><br/> I used it to...

## Getting Started

So that the repository is successfully cloned and simulator run smoothly, a few steps need to be followed.

### Requisites

* Need to download and install [Docker](https://docs.docker.com/get-docker/).
* The use of [Visual Studio Code](https://code.visualstudio.com/download) is recommended.

### Installation and Use

```sh
   $ git clone https://github.com/ElephanZ/System-Stats-By-Keylogger.git
   $ cd yourPath/System-Stats-By-Keylogger/
   $ ./run.sh
``` 

## License

Distributed under the **GNU General Public License v3.0**. See ``` LICENSE ``` for more information. :copyright:
