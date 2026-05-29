from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("PaymentStreamProcessor")
    .master("local[1]")
    .config("spark.driver.memory", "1g")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "payments")
    .option("startingOffsets", "latest")
    .load()
)

query = (
    df.selectExpr("CAST(value AS STRING)")
    .writeStream
    .format("console")
    .outputMode("append")
    .start()
)

query.awaitTermination()