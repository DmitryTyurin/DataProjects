# Напишите простой код, в котором Вы сначала определите имя главного потока по умолчанию, затем присвоите ему новое имя - My_main_thread, и после этого определите демонический признак главного потока.

import threading

main_thread = threading.main_thread().name
print(f"Имя главного потока по умолчанию: {main_thread}")

main_thread = "My_main_thread"
print(f"Новое имя главного потока: {main_thread}")

print(f"Демонический признак главного потока: {threading.main_thread().daemon}")
