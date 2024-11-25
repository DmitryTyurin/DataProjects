#!/bin/bash

echo "Отчет о логе веб-сервера" >> report.txt
echo "========================" >> report.txt

requests=$(wc -l < access.log)
echo -e "\nОбщее количество запросов: $requests" >> report.txt

uniq_ip=$(awk '{print $1}' access.log | sort -u | wc -l)
echo "Количество уникальных IP-адресов: $uniq_ip" >> report.txt


methods_count=$(awk '{ gsub("\"", "", $6); print $6 }' access.log | sort | uniq -c)
echo -e "\nКоличество запросов по методам:" >> report.txt
echo "$methods_count" >> report.txt

url=$(awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -n 1)
echo -e "\nСамый популярный URL: $url" >> report.txt

echo "Отчёт сохранён в файл report.txt."