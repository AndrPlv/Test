from time import perf_counter, sleep
from random import randint

print("Введите диапозон для загаданного числа:")
d = [int(j) for j in input(">>> ").split()]

def logger(func):
    def greate(**arg):
        print("Ответ программы:")
        result = func(**arg)
        return result
    return greate

@logger
def test(input_x: int, x: int):
    if input_x == x:
        print("Верно! Ты отгадал")
        return True
    else:
        if input_x > x:
            print("Моё число меньше!")
            return False
        else:
            print("Моё число больше!")
            return False

x = randint(d[0],d[1])
time = perf_counter()
print(f"Я загадал число в диапозоне: от {d[0]} до {d[1]}")
sleep(3)
print("Время пошло")
while(True):
    print("Я думаю это число...")
    inp_x = int(input(">>> "))
    resul = test(input_x=inp_x,x=x)

    if resul:
        print(f'За {round(perf_counter() - time, 4)}')
        break
