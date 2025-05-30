# Домен, к которому нужно конкатенировать имена файлов: https://parsinger.ru/3.3/3/img/
# Задание:
# Конкатенируйте имена файлов с доменом, чтобы получить полный URL каждого изображения.
# Выполните HTTP запрос к каждому изображению.
# Используя заголовок Content-Length из ответа сервера (response.headers.get('Content-Length')), определите размер каждого файла.
# Найдите изображение с наибольшим размером.
# Ожидаемый результат:
# В качестве результата вы должны выводить URL изображения с наибольшим размером.
# В поле ответа укажите имя файла этого изображения без расширения, только число (1000000000000009).
# Примечание:
# Задача предполагает, что вы не будете скачивать изображения, а только анализировать заголовки HTTP-ответа для определения их размера.

import requests
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

name_img = [
    "1663231240183817644.jpg",
    "1663231245165469794.jpg",
    "1663231252148267596.jpg",
    "16632460271311817.jpg",
    "1663260860165832550.jpg",
    "1663260862112644405.jpg",
    "1663260864114071369.jpg",
    "1663260869127473152.jpg",
    "1663260874115452216.jpg",
    "1663260877136512181.jpg",
    "1663260878140464277.jpg",
    "1663267600193799276.jpg",
    "1663267613117130673.jpg",
    "1663267619197170483.jpg",
    "1663267626154597739.jpg",
    "1663267648135114690.jpg",
    "166326765416196421.jpg",
    "1663267662118079649.jpg",
    "1663267668165066872.jpg",
    "1663267878176341940.jpg",
    "166326990115068678.jpg",
    "1663269922185881885.jpg",
    "1663269927127433209.jpg",
    "1663269942143420441.jpg",
    "1663269946174943071.jpg",
    "1663269964195277579.jpg",
    "1663269970148058649.jpg",
    "1663269974197750992.jpg",
    "166326997917397750.jpg",
    "1663270039138442380.jpg",
    "1663388012194470737.jpg",
    "166342371029995280.jpg",
    "1663423712288242036.jpg",
    "1663423715255612089.jpg",
    "1663423720221155166.jpg",
    "1663423722211139858.jpg",
    "1663423724211218483.jpg",
    "1663423728215479371.jpg",
    "1663423729298828299.jpg",
    "1663423732225964403.jpg",
    "1663424198111663025.jpg",
    "1663424199157537861.jpg",
    "1663424200184778832.jpg",
    "166342420214123494.jpg",
    "166342420317539591.jpg",
    "1663424204161674559.jpg",
    "1663424206188873432.jpg",
    "166342420813193185.jpg",
    "1663424209187179962.jpg",
    "1663424212162573102.jpg",
]


class DataRequest:
    def __init__(self, file_name_list: list):
        self.url = "https://parsinger.ru/3.3/3/img/"
        self.file_name_list = file_name_list
        self.size_list = []
        self.lock = Lock()
        self.executor = ThreadPoolExecutor(max_workers=100)

    def get_request(self, file_name: str):
        try:
            response = requests.get(f"{self.url}{file_name}")
            response.raise_for_status()

            if response.status_code == 200:

                if response.encoding != "utf-8":
                    response.encoding = "utf-8"

                size_img = int(response.headers.get("Content-Length"))
            else:
                size_img = 0

            self.size_list.append((file_name, size_img))

        except Exception as e:
            with self.lock:
                print(e)

    def create_executor(self):
        with self.executor as executor:
            futures = executor.map(self.get_request, self.file_name_list)

    def get_max_size(self):
        sorted_data = sorted(self.size_list, key=lambda x: x[1])

        max_file_name = sorted_data[-1][0]
        max_size = sorted_data[-1][1]

        print(f"Имя файла с максимальным размером: {max_file_name}")

    def run(self):
        import time

        start_time = time.perf_counter()

        self.create_executor()
        self.get_max_size()

        end_time = time.perf_counter()
        print(f"Время выполнения: {end_time - start_time} секунд")


data_request = DataRequest(name_img)
data_request.run()
