from pyspark.sql import SparkSession, functions as F, Window


spark = SparkSession.builder.appName("weather_data").master("local[*]").getOrCreate()

dataframe = spark.read.csv("weather_data.csv", header=True, inferSchema=True)

# Преобразуйте столбец date в формат даты.
dataframe = dataframe.withColumn("date", F.to_date(F.col("date"), "yyyy-MM-dd"))

# Заполнение пропущенных значений средними значениями по метеостанциям
dataframe = dataframe.withColumn(
    "temperature",
    F.when(F.col("temperature").isNotNull(), F.col("temperature")).otherwise(
        F.avg("temperature").over(Window.partitionBy("station_id"))
    ),
)

dataframe = dataframe.withColumn(
    "precipitation",
    F.when(F.col("precipitation").isNotNull(), F.col("precipitation")).otherwise(
        F.avg("precipitation").over(Window.partitionBy("station_id"))
    ),
)

dataframe = dataframe.withColumn(
    "wind_speed",
    F.when(F.col("wind_speed").isNotNull(), F.col("wind_speed")).otherwise(
        F.avg("wind_speed").over(Window.partitionBy("station_id"))
    ),
)


# Анализ данных
# Найдите топ-5 самых жарких дней за все время наблюдений.
top_temperature = (
    dataframe.select("date", "temperature")
    .orderBy(F.col("temperature").desc())
    .limit(5)
)
top_temperature.show()

# Найдите метеостанцию с наибольшим количеством осадков за последний год.
max_precipitation = (
    dataframe.filter(F.year("date") == 2023)
    .groupBy("station_id")
    .agg(F.sum("precipitation").alias("sum_precipitation"))
)
max_precipitation = max_precipitation.orderBy(F.col("sum_precipitation").desc()).limit(
    1
)
max_precipitation.show()

# Подсчитайте среднюю температуру по месяцам за все время наблюдений.
avg_temperature = (
    dataframe.withColumn("month", F.month(F.col("date")))
    .groupBy(F.col("month"))
    .agg(F.avg("temperature"))
    .orderBy(F.col("month"))
)
avg_temperature.show()
