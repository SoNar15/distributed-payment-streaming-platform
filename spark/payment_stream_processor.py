from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("PaymentStreamProcessor")
    .master("local[1]")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

print("Creating Kafka stream...")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "172.27.32.1:9092")
    .option("subscribe", "payments")
    .option("startingOffsets", "earliest")
    .load()
)

print("Kafka stream created")

json_df = df.selectExpr(
    "CAST(value AS STRING) as message",
    "offset",
    "partition"
)


print("Starting stream query...")


query = (
    json_df.writeStream
    .outputMode("append")
    .format("parquet")
    .option(
        "path",
        "data/bronze/payments"
    )
    .option(
        "checkpointLocation",
        "data/checkpoints/payments"
    )
    .start()
)


print("Stream query started")

print("Query active:", query.isActive)

query.awaitTermination()