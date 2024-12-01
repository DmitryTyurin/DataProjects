from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("books_data").master("local[*]").getOrCreate()

books_df = spark.read.csv("books.csv", header=True, inferSchema=True)
authors_df = spark.read.csv("authors.csv", header=True, inferSchema=True)

# Обработка данных: Преобразуйте столбцы publish_date и birth_date в формат даты.
if "publish_date" in books_df.columns:
    print("Столбец publish_date найден, преобразование в формат даты.")

    books_df = books_df.withColumn(
        "publish_date", F.to_date(F.col("publish_date"), "yyyy-mm-dd")
    )
else:
    print("Столбец publish_date не найден.")


if "birth_date" in authors_df.columns:
    print("Столбец birth_date найден, преобразование в формат даты.")

    authors_df = authors_df.withColumn(
        "birth_date", F.to_date(F.col("birth_date"), "yyyy-mm-dd")
    )
else:
    print("Столбец birth_date не найден.")

# Объединение данных: Объедините таблицы books и authors по author_id.
join_df = books_df.join(authors_df, on="author_id", how="left")

join_df.show()

# Анализ данных:
# Найдите топ-5 авторов, книги которых принесли наибольшую выручку.
top_author = (
    join_df.groupBy("author_id", "name")
    .agg(F.sum("price").alias("total_revenue"))
    .orderBy(F.col("total_revenue").desc())
    .limit(5)
)

# Найдите количество книг в каждом жанре.
count_genre = (
    join_df.groupBy("genre")
    .agg(F.count("genre").alias("count"))
    .orderBy(F.col("count").desc())
)

# Подсчитайте среднюю цену книг по каждому автору.
avg_price_books = (
    join_df.groupBy("author_id", "name")
    .agg(F.avg("price").alias("average_price"))
    .orderBy(F.col("average_price").desc())
)

# Найдите книги, опубликованные после 2000 года, и отсортируйте их по цене.
new_books = join_df.filter(F.year("publish_date") > 2000).orderBy(F.col("price").desc())

# Результаты: Выведите результаты анализа в виде таблиц.
top_author.show()
count_genre.show()
avg_price_books.show()
new_books.show()
