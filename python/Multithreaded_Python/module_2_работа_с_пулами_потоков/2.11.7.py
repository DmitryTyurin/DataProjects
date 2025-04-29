# Описание задачи:
# Данная задача включает использование трёх заранее заданных списков, содержащих уникальные строковые значения. Вы должны создать программу, использующую многопоточность для параллельной обработки каждого элемента этих списков. Каждый список будет обрабатываться отдельно, с использованием разного размера пула потоков, что позволит демонстрировать масштабируемость и эффективность многопоточной обработки.
#
# # Списки вшиты в задачу, вставлять их в поле ответа не нужно.
#
# fifty = ['OF95RK', 'VH61DX', 'NB03WA', ...'OL41DZ']
# one_hundred = ['JF39XW', 'RO06QB', 'RW48XW', ...'ZE42EF']
# two_hundred = ['FP99WI', 'IJ21HS', 'SV16JN', ... 'EP11JG']
# Каждый элемент списка необходимо обработать отдельным потоком в пуле своего размера.
# Например, для списка fifty=[] использовать пул размером 50 потоков, т.к. в этом списке 50 элементов. Всего необходимо создать три пула для трёх списков(50, 100, 200).
#
# При обработке элемента списка программа должна выводить сообщение в формате:
#
# f"Элемент {elem} списка из пула размером {pool_size}"
# Это демонстрирует, какой элемент был обработан и какой размер пула потоков использовался для его обработки.

from concurrent.futures import ThreadPoolExecutor, wait

fifty = ["OF95RK", "VH61DX", "NB03WA", "OL41DZ"]
one_hundred = ["JF39XW", "RO06QB", "RW48XW", "ZE42EF"]
two_hundred = ["FP99WI", "IJ21HS", "SV16JN", "EP11JG"]


class ThreadPoolExample:
    def __init__(self, fifty: list, one_hundred: list, two_hundred: list):
        self.fifty = fifty
        self.one_hundred = one_hundred
        self.two_hundred = two_hundred
        self.mapping = {
            "fifty": (self.fifty, 50),
            "one_hundred": (self.one_hundred, 100),
            "two_hundred": (self.two_hundred, 200),
        }

    @staticmethod
    def process_element(elem: str, pool_size: int):
        return f"Элемент {elem} списка из пула размером {pool_size}"

    def process_with_threadpool(self, element_name: list, pool_size: int):
        with ThreadPoolExecutor(max_workers=pool_size) as executor:
            futures = [
                executor.submit(self.process_element, elem, pool_size)
                for elem in element_name
            ]
            wait(futures)

        for future in futures:
            if future.done():
                result = future.result()
                print(result)

    def run(self):
        for element_name, pool_size in self.mapping.values():
            self.process_with_threadpool(element_name, pool_size)


poll = ThreadPoolExample(fifty, one_hundred, two_hundred)
poll.run()
