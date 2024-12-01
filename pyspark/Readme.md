## Локальная установка PySpark на Windows IDE PyCharm
### Spark: https://spark.apache.org/downloads.html
### JAVA JDK (Windows 21 версию): https://www.oracle.com/java/technologies/downloads/
### Winutils.exe: https://github.com/steveloughran/winutils/tree/master/hadoop-3.0.0/bin

#### Установка:

1) Устанавливаем JAVA. Двойной клик по значку с чашкой, затем Next, немного подождать и готово!

![img](https://ucarecdn.com/74f2ca22-77d6-4103-860e-aad0584709b3/)


2) Следующим на очереди будет Spark. Создаем на диске С:/ папку Spark, копируем в нее скачанный ранее архив Spark и распаковываем его туда:

![img](https://ucarecdn.com/111192aa-71b1-493e-be56-49981451cfda/)

3) Также на диске C:/создаем папку Hadoop, а в ней папку bin, и копируем в нее утилиту Winutils.exe

![img](https://ucarecdn.com/6b4d9d42-62b2-4721-9861-841354d176b9/)

4) Теперь необходимо добавить в системные переменные наши 3 переменные. В поиске Windows -> "Переменные среды":

![img](https://ucarecdn.com/1f2f6d27-ec4c-48f9-9fe9-3e5bb2ea7d73/)

Имя: HADOOP_HOME Значение: C:\Hadoop:
![img](https://ucarecdn.com/23dd7e50-ed5f-4bcf-8916-a1ed3775c950/)

Имя: SPARK_HOME Значение: C:\Spark\spark-X.X.X-bin-hadoopX

![img](https://ucarecdn.com/2ce2adeb-0568-4551-a137-1eb907d8d9b9/)

Имя: JAVA_HOME Значение: C:\Program Files\Java\jdk-21

![img](https://ucarecdn.com/d6775c21-c8e5-4a7c-956f-031c6682e520/)


5) В этом же окне выбираем среду Path и нажимаем Изменить.

![img](https://ucarecdn.com/0b04dcbc-5112-4e13-93ce-ec63f2cfd4c4/)

Добавляем такие значения:
%SPARK_HOME%\bin 
%HADOOP_HOME%\bin  
%SPARK_HOME%\python 
%PYTHONPATH%
C:\Spark\spark-3.5.3-bin-hadoop3\python\lib\py4j-0.10.9.7-src.zip

![img](https://ucarecdn.com/70e45558-89ab-46cd-979a-a420d7da6556/)

![img](https://ucarecdn.com/d90873c2-d5b1-4f13-9dea-0e3ce27d8ed8/)

6) Открыть командную строку и выполнить команду: spark-submit --version

![img](https://ucarecdn.com/463de732-19d5-44b0-a670-bd84c8bb3d14/)

7) Создаем новый проект в PyCharm
8) Открываем настройки проекта

![img](https://ucarecdn.com/8dbdc080-bcbf-474e-829f-5565ec5fe6a0/)
9) добавить 2 архива из папки C:\Spark\spark-3.5.3-bin-hadoop3\python\libЭто папка из распакованного изначально архива Spark. 
Переходим в нее и добавляем 2 архива:

![img](https://ucarecdn.com/46c3f23c-59b5-4232-9aea-22c97bbe95d0/)

![img](https://ucarecdn.com/3fd7f356-d2b4-4d67-9738-a0a637f1262c/)

### Перезагрузить ПК

#### Запускаем в main.py

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[1]") \
 .appName('SparkByExamples.com') \
 .getOrCreate()

![img](https://ucarecdn.com/88f949c4-f27a-4196-906d-bc18b4b6c099/)