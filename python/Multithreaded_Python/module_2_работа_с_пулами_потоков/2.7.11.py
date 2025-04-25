# Описание задачи:
# Ваша программа должна использовать многопоточность для конкурентной обработки задач.
# Каждый поток в должен запускать "задачу" с уникальным именем-идентификатором из списка ниже.
# unique_task_ids = ['StarExplorer42', 'QuantumLeap89', 'CyberWizard77',
#                    'GalacticVoyager66', 'MysticCoder11', 'NeuralNinja53',
#                    'QuantumRanger88', 'SpaceSurfer15', 'TimeTraveler23',
#                    'CosmicSage99']
# При инициализации потока должно быть создано сообщение с его именем.
# # Пример вывода
# Инициализация потока ThreadPoolExecutor-0_0
# Цель каждой задачи заключается в создании сообщения о работе потока.
# # Пример вывода
# Поток ThreadPoolExecutor-0_0 выполняет задачу StarExplorer42
# После завершения работы всех задач необходимо напечатать все созданные сообщения.

from concurrent.futures import ThreadPoolExecutor, wait
import threading
import time

unique_task_ids = [
    "StarExplorer42",
    "QuantumLeap89",
    "CyberWizard77",
    "GalacticVoyager66",
    "MysticCoder11",
    "NeuralNinja53",
    "QuantumRanger88",
    "SpaceSurfer15",
    "TimeTraveler23",
    "CosmicSage99",
]


class TaskExecutor:
    def __init__(self, task_ids: list[str]):
        self.task_ids = task_ids
        self.executor = ThreadPoolExecutor(
            max_workers=3, initializer=self.thread_initializer
        )
        self.result_lst = []

    def thread_initializer(self):
        thread_name = threading.current_thread().name

        message = f"Инициализация потока {thread_name}"
        self.result_lst.append(message)

        print(message)

    def thread_task(self, task_id):
        thread_name = threading.current_thread().name
        time.sleep(1)

        message = f"Поток {thread_name} выполняет задачу {task_id}"
        self.result_lst.append(message)

    def run(self):
        with self.executor as executor:
            futures = {
                executor.submit(self.thread_task, task_id) for task_id in self.task_ids
            }

            done, not_done = wait(futures)

            [print(message) for message in self.result_lst]


TaskExecutor(unique_task_ids).run()
