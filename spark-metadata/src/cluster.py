from pyspark.sql import SparkSession
from pyspark.sql import types as tp
from pyspark.sql.functions import from_json, col

from processing import processBatch


APP_NAME = 'KeyloggerStats'

KAFKA_SERVER = 'broker:9093'
KAFKA_TOPIC = 'metadata'


def getLogSchema():
    return tp.StructType([
        tp.StructField(name='type',            dataType=tp.StringType()),
        tp.StructField(name='timestamp_begin', dataType=tp.TimestampType()),
        tp.StructField(name='window',          dataType=tp.StringType()),
        tp.StructField(name='uuid',            dataType=tp.StringType()),
        tp.StructField(name='timestamp_end',   dataType=tp.TimestampType()),
    ])


spark = SparkSession.builder.appName(APP_NAME).getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

df = spark.readStream \
    .format('kafka') \
    .option('kafka.bootstrap.servers', KAFKA_SERVER) \
    .option('subscribe', KAFKA_TOPIC) \
    .load() \
    .select(from_json(col("value").cast("string"), getLogSchema()).alias("data")) \
    .select("data.*")

df.writeStream \
    .foreachBatch(processBatch) \
    .start() \
    .awaitTermination()