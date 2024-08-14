
# ? MULTITHREADING = Used to perform multiple task concurrently(multitasking). Good for I/O bound tasks like reading files or fetching data from API's threading. Thread(target=my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")

def take_out_trash(nameoftrash):
    time.sleep(5)
    print(f"You took out the {nameoftrash}")

def get_mail(iphonepackage):
    time.sleep(6)
    print(f"You got the {iphonepackage}")

chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash, args=("Dustbin",))
chore2.start()

chore3 = threading.Thread(target=get_mail, args=("Iphone",))
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All choices are completed")