# Описание задачи:
# Напишите код для многопоточного мониторинга сетевых устройств. Код должен отслеживать статус каждого устройства и реагировать на изменения его состояния.
#
# Создание списка устройств:
#
# Вам дан список словарей devices, где каждый словарь содержит информацию о сетевом устройстве: его имя (name), IP-адрес (ip) и статус (status), который может быть True (устройство активно) или False (устройство неактивно).
# # Полный список словарей вшит в задачу, вставлять его в поле ответа не нужно
#
# devices = [
#     {"name": "Server1", "ip": "192.168.1.1", 'status': True},
#     {"name": "Router1", "ip": "192.168.1.2", 'status': True},
#     {"name": "Switch1", "ip": "192.168.1.3", 'status': False},
#     ...
#     ...
#     ...
#     {"name": "Server10", "ip": "192.168.1.28", 'status': True},
#     {"name": "Router10", "ip": "192.168.1.29", 'status': False},
#     {"name": "Switch10", "ip": "192.168.1.30", 'status': True}
# ]
#
#
# Реализация функции мониторинга:
#
# Функция monitor_device(device), которая принимает одно устройство из списка devices и выводит сообщение о начале мониторинга устройства, включая его имя, IP и текущий статус.
#
# Мониторинг устройства: Server1, с IP 192.168.1.1 статус: True
#
# print(f"Мониторинг устройства: {device['name']}, с IP {device['ip']} статус: {device['status']}")
# Реализация функции обратного вызова:
#
# Создайте функцию обратного вызова handle_device_status(future), которая будет вызываться после завершения мониторинга каждого устройства. Эта функция должна проверять статус устройства и, в зависимости от результата, выводить соответствующее сообщение:
#
# Если статус True, сообщите, что устройство активно и работает нормально.
# Устройство Router1 активно и работает нормально.
#
# print(f"Устройство {device['name']} активно и работает нормально.")
# Если статус False, измените статус на True, сообщите о неактивности устройства и о том, что оно было включено.
# Внимание: Устройство Router2 неактивно! Включаем устройство.
# print(f"Внимание: Устройство {device['name']} неактивно! Включаем устройство.")
#
# # и
#
# Устройство Router2 успешно включено!
# print(f"Устройство {device['name']} успешно включено!")
# Использование ThreadPoolExecutor:
#
# Используйте ThreadPoolExecutor для создания пула потоков любого размера. Отправьте на выполнение функцию мониторинга для каждого устройства в списке devices, используя метод submit().
# Добавьте функцию обратного вызова handle_device_status к каждому Future объекту, возвращаемому методом submit().
# Примерный вывод кода должен быть такой:
#
# Мониторинг устройства: Server1, с IP 192.168.1.1 статус: True
# Устройство Server1 активно и работает нормально.
# Мониторинг устройства: Router1, с IP 192.168.1.2 статус: True
# Устройство Router1 активно и работает нормально.
# ...
# ...
# ...
# Устройство Switch9 успешно включено!
# Внимание: Устройство Router10 неактивно!
# Включаем устройство.Устройство Switch10 активно и работает нормально.
# Устройство Router10 успешно включено!


from concurrent.futures import ThreadPoolExecutor
import threading
import time

devices = [
    {"name": "Server1", "ip": "192.168.1.1", "status": True},
    {"name": "Router1", "ip": "192.168.1.2", "status": True},
    {"name": "Switch1", "ip": "192.168.1.3", "status": False},
    {"name": "Server10", "ip": "192.168.1.28", "status": True},
    {"name": "Router10", "ip": "192.168.1.29", "status": False},
    {"name": "Switch10", "ip": "192.168.1.30", "status": True},
]


class MonitoringDevice:
    def __init__(self, devices: list):
        self.devices = devices
        self.executor = ThreadPoolExecutor(max_workers=5)

    @staticmethod
    def monitor_device(device: dict):
        name = device.get("name")
        ip = device.get("ip")
        status = device.get("status")

        print(f"Мониторинг устройства: {name}, с IP {ip} статус: {status}")
        return name, ip, status

    @staticmethod
    def handle_device_status(future):
        name, ip, status = future.result()

        if status:
            print(f"Устройство {name} активно и работает нормально.")
        if not status:
            print(f"Внимание: Устройство {name} неактивно! Включаем устройство.")
            status = True
            print(f"Устройство {name} успешно включено!")

    def run(self):
        with self.executor as executor:
            futures = [
                executor.submit(self.monitor_device, device) for device in self.devices
            ]

            for future in futures:
                future.add_done_callback(self.handle_device_status)


md = MonitoringDevice(devices)
md.run()
