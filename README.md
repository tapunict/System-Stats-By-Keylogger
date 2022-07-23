# System-Stats-By-Keylogger
_Project of Technologies for Advanced Programming_

_Grade: 30 with honors / 30_

_Antonio Scardace_ @ 
_Dept of Math and Computer Science, University of Catania_

## Introduction

The course aims to study and use useful technologies to build end-to-end solutions to analyze, manage, archive, process, and view a high amount of data in real-time. For instance, we have seen: Docker containers, and pipelines built with Logstash (for data ingestion), Kafka (for data streaming), Spark (for data processing), ElasticSearch (for data storing), and Kibana (for data visualization). 

This project was created as an exam project, to test and practice the following skills:
* Knowledge of Docker
* Knowledge of Data Ingestion via Logstash
* Knowledge of Data Streaming via Kafka
* Knowledge of Data Processing via Spark 
* Knowledge of Data Storing via Elasticsearch
* Knowledge of Data Visualization via Kibana
* Knowledge of Jupyter Notebook (for the presentation)
* Good coding skills (legible, reliable, documented, etc.) :computer:

## Real Use Case

The aim of the project is to make stats on the real-time use of the system by the user (and by users in general).

It can be useful as:
1. System Monitor owned by **Operating Systems** owners
2. System Monitor for **Public Offices Computers**
3. System Monitor for **Prison Computers**
4. **Parental Control**
5. **Spyware**

### Data Source: Windows Keylogger

The data source is a Windows Keylogger for Italian keyboards only, developed in C++14 using Windows APIs. Sends a log to the TCP server on each foreground window change OR after 1 minute of user inactivity.

The log has the following pattern:
```
[UUID] :: [Window Title] :: [Timestamp Start]
Logged Text...
[Timestamp End] :: [IP Address]
```

Each log is composed by:
- **UUID**: Identifies the PC univocally. Has the following format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
- **Window Title**: Is the title of the window where the user has typed.
- **Timestamp Start**: Indicates when the user started typing in that window.
- **Logged Text**: Is the set of keys pressed by the user and logged by the keylogger.
- **Timestamp End**: Indicates when the user finished typing in that window.
- **IP Address**: Is the public IP address. If the PC has no connection, the default value is "Unknown".

For instance:
```
[00000000-0000-0000-0000-000000000000] :: [WhatsApp] :: [2022-01-01 12:00:00]
Hi Nicole, happy new year!!
[2022-01-01 12:00:13] :: [1.2.3.4]
```

### Server System

Receives logs (from multiple clients) and passes them to the pipeline illustrated below:
<p align="center"> <img src="docs/images/pipeline.png?v=1654694080" height="470px"/> </p>

The following functions are available for each user (personal stats) and for all users (general stats):
- For Logged Text:
    + Top 8 Last Logged Texts :page_facing_up:
    + Sentiment analysis :chart_with_upwards_trend:
- For Metadata:
    + Top 10 most used applications :bookmark:
    + Used windows classification :bar_chart:
        * Social
        * Utility
        * Entertainment
        * Web Browsing
        * Office & Study
        * Other
    + Customers Geolocation by IP :earth_americas:
    + Overall time spent writing to the PC :computer:
    + Average time spent writing in a window :memo:
    + Average time spent writing in each category of window :satellite:
    + Overall time spent on each category of window :eyes:

## Structure & Demo

Let's see the structure of the project and how I have used all the components. <br/>
Each component used in this project has been put inside a **Docker Container** :whale:

Component | Description
------ | -------
<img src="docs/logos/python-logo.png" width="165px" /> | I have used it to implement a multi-threading server that receives real-time logs via TCP requests on the 8800 port from multiple clients. It extracts the features seen above from the logs and saves them in two CSV files: <br/><br/> **metadata.csv** = [UUID, Window Title, Timestamp of Begin, Timestamp of End, IP Address] <br/> **logs.csv** = [UUID, Logged Text] <br/><br/> Here is the UML schema: <br/><p align="center"><img src="docs/images/server-schema.svg"/></p>
<img src="docs/logos/logstash-logo.png" width="165px" /> | **Logstash** is an open-source data collection engine with real-time pipelining capabilities. Logstash can dynamically unify data from disparate sources and normalize the data into destinations of your choice.<br/><br/> I have used it to create two different data flow: one for the metadata and one for the text logs. Logstash takes this input data from two files, metadata.csv and logs.csv - they have been shared with the server container via a Docker volume. <br/><br/> Here is an example of what Logstash receives: <br/><br/> <p align="center"> <img src="docs/snaps/logstash.png"/> </p>
<img src="docs/logos/kafka-logo.png?v=1653055181" width="165px" /> | **Apache Kafka** is a distributed data streaming platform that can handle and process streams of records in real-time. It is designed to handle data streams from multiple sources and deliver them to numerous consumers. Kafka uses **Zookeeper** to keep track of which partitions each member in a consumer group is consuming, and uses **Brokers** to receive data and send them to customers on request (Kafka has a pull architecture). <br/> Also, we can use **UI for Apache Kafka** which is a simple tool that makes dataflows observable, helps find and troubleshoot issues faster, and deliver optimal performance. <br/><br/> I have used it to make a single cluster, which has two topics: one for logs and one for metadata. It receives two different dataflows by Logstash and stores them to be pulled by Spark. **Kafka Stream** has not been used. <br/><br/> <p align="center"> <img src="docs/snaps/kafka-ui-clusters.png"/> <img src="docs/snaps/kafka-ui-topics.png"/> </p>
<img src="docs/logos/spark-logo.png" width="165px" /> |  **Apache Spark** is an open-source multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters, with implicit data parallelism and fault tolerance. <br/> It allows the use of **Spark Streaming** which is an extension of the core Spark API, that allows data engineers and data scientists to process real-time data that can be ingested from various sources including (but not limited to) Kafka, and can be processed using complex algorithms expressed with high-level functions. <br/><br/> I have created two Docker Containers - one for each Kafka Topic we need to read from. Each of them, after the processing, saves the documents into the Elasticsearch index _keylogger_. <br/> In the first, Spark Streaming read data from the _logs_ topic and adds a little set of features. It is the VADER dictionary. <br/> In the second, Spark Streaming read data from the _metadata_ topic and adds three features: the type of the window, the difference (in seconds) between the two timestamps fields, and the public IP address geolocation coordinates (if it isn't set to "Unknown"). <br/><br/> <img src="docs/snaps/spark-metadata.png"/> <img src="docs/snaps/spark-logs.png"/>
<img src="docs/logos/elasticsearch-logo.png" width="165px" /> | **Elasticsearch** is a search engine, and is the heart of the ELK Stack. It centrally stores data for lightning fast search, fine‑tuned relevancy, and powerful analytics that scale with ease.<br/><br/> I have used it to create a cluster, containing the *keylogger_stats* index, shared only by a single node: *es001*. It receives docs from Spark Streaming. Data are saved into a Docker Volume to make the application persistent in time. <br/><br/> Here is an example of what Elasticsearch contains and shows: <br/><br/> <p align="center"> <img src="docs/snaps/elasticsearch.png"/> </p>
<img src="docs/logos/kibana-logo.png?v=1653055181" width="165px" /> | **Kibana** is a free front-end application that sits on top of the ELK Stack, providing search and data visualization capabilities for data indexed in ElasticSearch. Commonly known as the charting tool for the ELK Stack, Kibana also acts as the UI for monitoring and managing. Provides a lot of charting tools for all kinds of stats. <br/><br/> I have used it to visualize some stats in real-time - I have set the dashboard auto-refresh to happen every second. The dashboard analyzes just the data that have arrived in the last 24 hours. It shows general data (of all PCs) and if the user clicks on a specific UUID, the dashboard shows data of that particular PC. <br/><br/> <img src="docs/snaps/kibana-0.png"/> <img src="docs/snaps/kibana-1.png?v=1655832199"/> <img src="docs/snaps/kibana-2.png"/> <img src="docs/snaps/kibana-3.png"/> <img src="docs/snaps/kibana-4.png"/>

## Getting Started

So that the repository is successfully cloned and project run smoothly, a few steps need to be followed.

### Requisites

* At least 12 GB of RAM.
* At least 25 GB of free space.
* Use of Linux, MacOS, or Windows WSL.
* Need to download and install [Docker](https://docs.docker.com/get-docker/) (but the use of [Docker Desktop](https://www.docker.com/products/docker-desktop/) is optional).
* The use of [Visual Studio Code](https://code.visualstudio.com/download) is strongly recommended.

### Installation and Use

```sh
   $ git clone https://github.com/ElephanZ/System-Stats-By-Keylogger.git
   $ cd yourPath/System-Stats-By-Keylogger/
   $ bash run.sh
``` 

### Useful Links

Container | URL | Description
----- | ------- | -------
broker | http://localhost:8080 | UI for Kafka
elasticsearch | http://localhost:9200 | ElasticSearch basic URL
elasticsearch | http://localhost:9200/keylogger_stats/_search | ElasticSearch index URL
elasticsearch | [http://localhost:9200/keylogger_stats/_search?...](http://localhost:9200/keylogger_stats/_search?source_content_type=application/json&source={%22query%22:{%22match%22:{%22type%22:%22log%22}}}) | ElasticSearch URL to get all logs
elasticsearch | [http://localhost:9200/keylogger_stats/_search?...](http://localhost:9200/keylogger_stats/_search?source_content_type=application/json&source={%22query%22:{%22match%22:{%22type%22:%22metadata%22}}}) | ElasticSearch URL to get all metadata
kibana | http://localhost:5601 | Kibana basic URL
kibana | [http://localhost:5601/dashboards/list?...](http://localhost:5601/app/dashboards#/list?_g=(filters:!(),refreshInterval:(pause:!f,value:1000),time:(from:now-24h%2Fh,to:now))) | Kibana Dashboards List

## License :copyright: 

**Author**: [Antonio Scardace](https://antonioscardace.altervista.org/). <br/>
Distributed under the **GNU General Public License v3.0**. See ``` LICENSE ``` for more information.

PLEASE USE AND READ IT FOR ACADEMIC PURPOSES ONLY. :bangbang: <br/>
I DISCLAIM ANY LIABILITY FOR ILLEGAL USE. :bangbang:
