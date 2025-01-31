# Дописать корутину check_mail(server):
#
# Корутина должна принимать объект класса MailServer, созданный в main()
#
# Опрос должен проводиться каждую секунду, используйте метод класса для проверки наличия писем.
#
# Если метод check_for_new_mail() возвращает сообщение об ошибке, функция должна вывести это сообщение и остановить опрос. В противном случае, если новые письма есть, необходимо получить их с помощью метода fetch_new_mail() и вывести их на экран в формате: f"Новое письмо: {mail}". Если новых писем нет, вывести сообщение "Новых писем нет.".
#
# Дописать корутину main(), в которой создается экземпляр MailServer и запускается корутина check_mail(server).

import asyncio
import random

random.seed(1)


class MailServer:
    def __init__(self):
        self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"


async def check_mail(server):
    while True:
        result = await server.check_for_new_mail()

        if isinstance(result, str):
            print(result)
            break

        if result:
            mail = await server.fetch_new_mail()
            print(mail)
        else:
            print("Новых писем нет.")

        await asyncio.sleep(1)


async def main():
    server = MailServer()
    await check_mail(server)


asyncio.run(main())
