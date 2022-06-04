docker rm -f $(docker ps -a -q)
docker volume rm $(docker volume ls -q)

docker compose build server-python
docker compose build logstash
docker compose build zookeeper
docker compose build broker
docker compose build kafka-ui
docker compose build init-kafka
docker compose build spark
docker compose build elasticsearch
docker compose build kibana

docker compose up -d
