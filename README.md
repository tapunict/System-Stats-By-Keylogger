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
[Window Name] :: (Timestamp)
...Text logged...
```
For instance:
```
[Untitled - Notepad] :: (2022-01-01 12:30:00)
Hello Wot[BACKSPACE]rld!

[Calculator] :: (2022-01-01 12:32:46)
50+50[ENTER]/4[ENTER]
```

### Server System

There is a socket which receives the log and passes it to the pipeline described above and illustrated below:

![pipeline](/docs/imgs/pipeline.png)

The purpose of the project is to make stats on the use of the system by the user. <br/>
Specifically, the following functions are available:
* aaa
* bbb

Additionally, this project was created as an exam project, to test and practice the following skills:
* Knowledge of Docker
* Knowledge of Data Ingestion via Logstash
* Knowledge of Data Streaming via Kafka
* Knowledge of Data Processing via Spark 
* Knowledge of Data Storage via ElasticSearch
* Knowledge of Data Visualization via Kibana
* Knowledge of Jupyter Notebook (for the presentation)
* Good coding skills (legible, reliable, documentation, etc.) :computer:

## Structure and Demo

Lets see a step-by-step explanation integrated with some screenshots of the demo.

<img src="docs/logos/logstash-logo.png" height="60px" />

Logstash is an open-source data collection engine with real-time pipelining capabilities. Logstash can dynamically unify data from disparate sources and normalize the data into destinations of your choice.

<img src="docs/logos/kafka-logo.png?v=1653055181" height="60px" />

Kafka is a distributed data streaming platform that can handle and process streams of records in real-time. It is designed to handle data streams from multiple sources and deliver them to numerous consumers.

<img src="docs/logos/elasticsearch-logo.png" height="60px" />

Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the free and open Elastic Stack, it centrally stores your data for lightning fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.

<img src="docs/logos/spark-logo.png" height="60px" />

Spark is a unified analytics engine for large-scale data processing in real-time.

<img src="docs/logos/kibana-logo.png?v=1653055181" height="60px" />

Kibana is a free and open front-end application that sits on top of the Elastic Stack, providing search and data visualization capabilities for data indexed in ElasticSearch. Commonly known as the charting tool for the Elastic Stack, Kibana also acts as the user interface for monitoring and managing.

## Getting Started

So that the repository is successfully cloned and simulator run smoothly, a few steps need to be followed.

### Requisites

* Need to download and install [Docker](https://docs.docker.com/get-docker/).
* The use of [Docker Desktop](https://www.docker.com/products/docker-desktop/) is recommended.
* The use of [Visual Studio Code](https://code.visualstudio.com/download) is recommended.

### Installation and Use

1. Clone the repository 
```sh
   git clone https://github.com/ElephanZ/System-Stats-By-Keylogger.git
``` 
2. Go into the repository project
```sh
   cd yourPath/System-Stats-By-Keylogger/
``` 
3. Run the project
```sh
   bash run.sh 
``` 

## License

Distributed under the **GNU General Public License v3.0**. See ``` LICENSE ``` for more information.
