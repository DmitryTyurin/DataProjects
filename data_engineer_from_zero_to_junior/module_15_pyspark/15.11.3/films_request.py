from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("spark").master("local[*]").getOrCreate()

# Чтение данных
movies_df = spark.read.csv("movies.csv", header=True, inferSchema=True)
actors_df = spark.read.csv("actors.csv", header=True, inferSchema=True)
movie_actors_df = spark.read.csv("movie_actors.csv", header=True, inferSchema=True)

# Временные таблицы для данных о фильмах, актерах и связях между ними.
movies_df.createOrReplaceTempView("movies")
actors_df.createOrReplaceTempView("actors")
movie_actors_df.createOrReplaceTempView("movie_actors")

# Найдите топ-5 жанров по количеству фильмов.
top_genre = spark.sql(
    """
    select genre, count(movie_id) as count_film
    from movies
    group by genre
    order by count_film desc
"""
)

# Найдите актера с наибольшим количеством фильмов.
top_actor = spark.sql(
    """
    select a.name as actor_name, count(ma.movie_id) as count_film
    from actors a
      left join movie_actors ma on a.actor_id = ma.actor_id
    group by a.name
    order by count_film desc
    limit 1
"""
)

# Подсчитайте средний бюджет фильмов по жанрам.
avg_budget = spark.sql(
    """
    select genre, avg(budget) as avg_budget
    from movies
    group by genre
"""
)

# Найдите фильмы, в которых снялось более одного актера из одной страны.
actor_from_country = spark.sql(
    """
    select m.title, a.country, count(ma.actor_id) as count_actor
    from movies m
      left join movie_actors ma on m.movie_id = ma.movie_id
      left join actors a ON ma.actor_id = a.actor_id
    group by m.title, a.country
    having count_actor > 1
"""
)


# Результаты:
top_genre.show()
top_actor.show()
avg_budget.show()
actor_from_country.show()
