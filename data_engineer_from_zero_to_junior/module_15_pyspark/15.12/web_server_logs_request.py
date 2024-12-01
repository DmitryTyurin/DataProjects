from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("spark").master("local[*]").getOrCreate()

logs_df = spark.read.csv("web_server_logs.csv", header=True, inferSchema=True)

# Анализ информации
# Сгруппируйте данные по IP и посчитайте количество запросов для каждого IP, выводим 10 самых активных IP
top_active_ip = (
    logs_df.groupBy("ip")
    .agg(F.count("ip").alias("request_count"))
    .orderBy(F.col("request_count").desc())
    .limit(10)
)

# Сгруппируйте данные по HTTP-методу и посчитайте количество запросов для каждого метода.
method_count = logs_df.groupBy("method").agg(F.count("method").alias("method_count"))

# Профильтруйте и посчитайте количество запросов с кодом ответа 404.
response_code_by_404 = logs_df.filter(F.col("response_code") == 404).count()

# Сгруппируйте данные по дате и просуммируйте размер ответов, сортируйте по дате.
response_size_by_date = (
    logs_df.withColumn("date", F.to_date(F.col("timestamp"), "yyyy-mm-dd"))
    .groupBy("date")
    .agg(F.sum("response_size").alias("total_response_size"))
    .orderBy(F.col("date"))
)

# Результаты анализа
print("Top 10 active IP addresses:")
top_active_ip.show()

print("Request count by HTTP method:")
method_count.show()

print(f"Number of 404 response codes: {response_code_by_404}")

print("Total response size by date:")
response_size_by_date.show()
