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
Text logged...
```
For instance:
```
[Untitled - Notepad] :: (2022-01-01 12:30:00)
Hello Wot[BACKSPACE]rld!

[Calculator] :: (2022-01-01 12:45:00)
50+50[ENTER]/4[ENTER]
```

### Server System

There is a socket which receives the log and passes it to the pipeline described above and illustrated below:

![pipeline](/docs/images/pipeline.jpg)

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
* Good coding skills (legible, reliable, etc.) :computer:

## Structure

Element | Utility
----- | -------
/folder1/ | description...

## Demo

Lets see a step-by-step explanation integrated with some screenshots of the demo.

<img src="docs/logos/logstash-logo.png" height="70px" />

<img src="docs/logos/kafka-logo.png" height="70px" />

<img src="docs/logos/elasticsearch-logo.png" height="70px" />

<img src="docs/logos/spark-logo.png" height="70px" />

<img src="docs/logos/kibana-logo.png" height="70px" />

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
