from threading import Thread
from time import sleep, time


def hello():
    for i in range(5):
        print("Hello...", i + 1)
        sleep(0.3)


def hi():
    for i in range(5):
        print("Hi...", i + 1)
        sleep(0.3)


if __name__ == "__main__":
    t1 = Thread(target=hello)
    t2 = Thread(target=hi)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Bye...")

print("---------------------------------------------------")


def download(file_name, download_time):
    print("Downloading file", file_name)
    sleep(download_time)
    print("Download completed for", file_name)


if __name__ == "__main__":
    files = {"movie": 2, "song": 0.5, "pdf": 0.2, "document": 0.3}

    threads = []

    for file, download_time in files.items():
        t = Thread(target=download, args=(file, download_time))
        threads.append(t)

    start = time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time()

    print(f"Total time = {end - start:.2f} seconds")

    print("Bye...")
