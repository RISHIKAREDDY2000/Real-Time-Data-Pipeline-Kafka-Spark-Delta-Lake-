from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("FraudDetectionPipeline") \
    .getOrCreate()

schema = StructType([
    StructField("id", IntegerType()),
    StructField("date", StringType()),
    StructField("client_id", IntegerType()),
    StructField("card_id", IntegerType()),
    StructField("amount", DoubleType()),
    StructField("merchant_id", IntegerType()),
    StructField("merchant_city", StringType()),
    StructField("merchant_state", StringType()),
    StructField("zip", IntegerType()),
    StructField("mcc", IntegerType())
])

df = spark \
.readStream \
.format("kafka") \
.option("kafka.bootstrap.servers","localhost:9092") \
.option("subscribe","transactions_topic") \
.load()

transactions = df.selectExpr("CAST(value AS STRING)") \
.select(from_json(col("value"), schema).alias("data")) \
.select("data.*")

transactions.writeStream \
.format("delta") \
.option("checkpointLocation","/tmp/checkpoints") \
.start("/delta/transactions")
