from multiprocessing import Process
from threading import Thread
from time import time


def calculate(n1, n2):
    sum = 0
    for n in range(n1, n2):
        sum += n * n

    return sum


if __name__ == "__main__":
    num = 50_000_000

    start = time()
    calculate(0, num)
    end = time()
    print(f"Time took in serial = {end - start:.2f} seconds")
    print("---------------------------------------------------------------")

    mid = num // 2

    start = time()
    t1 = Thread(target=calculate, args=(0, mid))
    t2 = Thread(target=calculate, args=(mid, num))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time()
    print(f"Time took in parallel threads = {end - start:.2f} seconds")
    print("---------------------------------------------------------------")

    start = time()
    p1 = Process(target=calculate, args=(0, mid))
    p2 = Process(target=calculate, args=(mid, num))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time()
    print(f"Time took in parallel process = {end - start:.2f} seconds")

    print("Bye...")
