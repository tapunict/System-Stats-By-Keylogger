# System-Stats-By-Keylogger
_Project of Technologies for Advanced Programming_

_Antonio Scardace_ @ 
_Dept of Math and Computer Science, University of Catania_

## Introduction

The course aims to study and use technologies useful to build end-to-end solutions to analyze, manage, store, process, and visualize data acquired in real-time. For instance, we have seen: Docker containers, and pipelines built with Logstash (for data ingestion), Kafka (for data streaming), Spark (for data processing), ElasticSearch (for data storing), and Kibana (for data visualization). 

### Data Source: Windows Keylogger

The data source is a Windows Keylogger :warning: written and used just on my computer for academic purposes. <br/>
It has been developed in C++ and uses Windows APIs. <br/>
It sends a log to the TCP server on each foreground window change OR after 1 minute of user inactivity. <br/>
The log has the following pattern:

```
[Window Name] :: (Timestamp)
Text logged...
```

![log_pattern](/docs/images/log_pattern.jpg)

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

## Demo

...

## Structure

Element | Utility
----- | -------
/folder1/ | description....

## Getting Started

So that the repository is successfully cloned and simulator run smoothly, a few steps need to be followed.

### Requisites

* Need to have [AAA](https://www.test.com/).
* Need to download and install [BBB](https://www.test2.it/).
* The use of [Visual Studio Code](https://code.visualstudio.com/download) is recommended.

### Installation

1. Clone the repository 
```sh
   git clone https://github.com/ElephanZ/System-Stats-By-Keylogger.git
``` 

## License

Distributed under the **GNU General Public License v3.0**. See ``` LICENSE ``` for more information.
