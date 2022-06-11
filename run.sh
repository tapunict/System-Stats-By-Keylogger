docker compose down
docker volume rm $(docker volume ls -q)

docker compose build server-python
docker compose build logstash
docker compose build zookeeper
docker compose build broker
docker compose build kafka-ui
docker compose build init-kafka
docker compose build elasticsearch
docker compose build kibana
docker compose build spark-logs
docker compose build spark-metadata

docker compose up -d
