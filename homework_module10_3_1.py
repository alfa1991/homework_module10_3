import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()  # Блокируем поток для безопасного изменения баланса
            try:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
            finally:
                self.lock.release()  # Разблокируем после завершения операции
            time.sleep(0.001)  # Имитация задержки

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            self.lock.acquire()  # Блокируем поток для безопасного изменения баланса
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            finally:
                self.lock.release()  # Разблокируем после завершения операции
            time.sleep(0.001)  # Имитация задержки

# Создаем объект банка
bk = Bank()

# Создаем два потока для пополнения и снятия
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
