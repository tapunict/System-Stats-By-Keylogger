# System-Stats-By-Keylogger
_Project of Technologies for Advanced Programming_

_Antonio Scardace_ @ 
_Dept of Math and Computer Science, University of Catania_

## Introduction

The course aims to study and use technologies useful to build end-to-end solutions to analyze, manage, store, process, and visualize data acquired in real-time. For instance, we have seen: Docker containers, and pipelines built with Logstash (for data ingestion), Kafka (for data streaming), Spark (for data processing), ElasticSearch (for data storing), and Kibana (for data visualization). 

The purpose of the project is to make stats on the real-time use of the system by the user. <br/>
Additionally, this project was created as an exam project, to test and practice the following skills:
* Knowledge of Docker
* Knowledge of Data Ingestion via Logstash
* Knowledge of Data Streaming via Kafka
* Knowledge of Data Processing via Spark 
* Knowledge of Data Storing via ElasticSearch
* Knowledge of Data Visualization via Kibana
* Knowledge of Jupyter Notebook (for the presentation)
* Good coding skills (legible, reliable, documented, etc.) :computer:

### Data Source: Windows Keylogger

The data source is a Windows Keylogger :warning: written and used just on my computer for academic purposes. <br/>
It has been developed in C++ and uses Windows APIs. <br/>
It sends a log to the TCP server on each foreground window change OR after 1 minute of user inactivity.

The log has the following pattern:
```
[UUID] :: [Window Title] :: [Timestamp Start]
Text logged...
[Timestamp End]
```

Each log is composed by:
- **UUID**: Identifies the PC univocally. Has the following format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
- **Window Title**: Is the title of the window where the user has typed.
- **Timestamp Start**: Indicates when the user started typing in that window.
- **Text logged**: Is the set of keys pressed by the user and logged by the keylogger.
- **Timestamp End**: Indicates when the user finished typing in that window.

For instance:
```
[00000000-0000-0000-0000-000000000000] :: [Calculator] :: [2022-01-01 12:32:37]
50+50[ENTER]/4[ENTER]-0.456[ENTER]
[2022-01-01 12:33:05]

[00000000-0000-0000-0000-000000000000] :: [Untitled - Notepad] :: [2022-01-01 12:33:11]
[SHIFT]The ree[BACKSPACE]sult is 24.544
[2022-01-01 12:33:59]
```

### Server System

There is a socket which receives the log and passes it to the pipeline described above and illustrated below:
<p align="center"> <img src="docs/images/pipeline.png?v=1653225037" height="460px"/> </p>

The following functions are available:
- For the Text Log:
    + Sentiment analysis (NLP) :chart_with_upwards_trend:
- For Windows and Timestamps:
    + Type of window classification (social, game, utility, others) :iphone:
    + How much time the user spends on each category of windows :eyes:
    + How much time the user spends writing to the PC :clock9:

## Structure and Demo

Let's see the structure of the project and how I have used all the components:

<img src="docs/logos/docker-logo.png?v=1653175210" width="150px" />

Each of the following components used has been put inside a **Docker Container**. <br/>

Component | Utility
------ | -------
<img src="docs/logos/python-logo.png" width="165px" /> | I have used it to implement a server that receives logs via TCP requests through the 8800 port. It extracts the features by the log, and saves them into two CSV files. <br/><br/> _metadata.csv_ = [UUID, Window Title, Timestamp of Begin, Timestamp of End] <br/> _log.csv_ = [UUID, Text Log]
<img src="docs/logos/logstash-logo.png" width="165px" /> | **Logstash** is an open-source data collection engine with real-time pipelining capabilities. Logstash can dynamically unify data from disparate sources and normalize the data into destinations of your choice.<br/><br/> I have used it to create two different data flow: one for the metadata and one for the text logs. Logstash takes this input data from two files, metadata.csv and log.csv - they have been shared with the server container via a Docker volume. <br/><br/> Here is an example of what Logstash receives: <br/><br/> <p align="center"> <img src="docs/screens/logstash.png"/> </p>
<img src="docs/logos/kafka-logo.png?v=1653055181" width="165px" /> | **Apache Kafka** is a distributed data streaming platform that can handle and process streams of records in real-time. It is designed to handle data streams from multiple sources and deliver them to numerous consumers. It allows us to use **Kafka Streams**, which is a client library for building applications and microservices, where the input and output data are stored in an Apache Kafka cluster.<br/><br/> I used it to...
<img src="docs/logos/spark-logo.png" width="165px" /> | **Apache Spark** is an open-source unified analytics engine for large-scale data processing in real-time. It provides an interface for programming clusters with implicit data parallelism and fault tolerance. Furthermore, it allows us to use **Spark MLlib** which is used to perform machine learning algorithms. <br/><br/> I used it to...
<img src="docs/logos/elasticsearch-logo.png" width="165px" /> | **Elasticsearch** is a search engine, and is the heart of the ELK Stack. It centrally stores data for lightning fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.<br/><br/> I used it to...
<img src="docs/logos/kibana-logo.png?v=1653055181" width="165px" /> | **Kibana** is a free front-end application that sits on top of the ELK Stack, providing search and data visualization capabilities for data indexed in ElasticSearch. Commonly known as the charting tool for the ELK Stack, Kibana also acts as the UI for monitoring and managing.<br/><br/> I used it to...

## Getting Started

So that the repository is successfully cloned and project run smoothly, a few steps need to be followed.

### Requisites

* Use of Linux, MacOS, or Windows WSL.
* Need to download and install [Docker](https://docs.docker.com/get-docker/) ([Docker Desktop](https://www.docker.com/products/docker-desktop/) is optional).
* The use of [Visual Studio Code](https://code.visualstudio.com/download) is strongly recommended.
* The use of [Jupyter Notebook](https://jupyter.org/install#jupyter-notebook) (also as VS Code extension) is recommended to see the presentation.

### Installation and Use

```sh
   $ git clone https://github.com/ElephanZ/System-Stats-By-Keylogger.git
   $ cd yourPath/System-Stats-By-Keylogger/
   $ bash run.sh
``` 

### Useful Links

Container | URL | Description
----- | ------- | -------
Lorem ipsum | http://localhost:5000 | Lorem ipsum

## License :copyright: 

**Author**: [Antonio Scardace](https://antonioscardace.altervista.org/). <br/>
Distributed under the **GNU General Public License v3.0**. See ``` LICENSE ``` for more information.

PLEASE USE AND READ IT FOR ACADEMIC PURPOSES ONLY. :bangbang: <br/>
I DISCLAIM ANY LIABILITY FOR ILLEGAL USE. :bangbang:
