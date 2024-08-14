from multiprocessing import Process
import time
import math

results_a = []
results_b = []
results_c = []

def make_calculation_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))

def make_calculation_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))


def make_calculation_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))

if __name__ == '__main__':
    number_list = list(range(1000000))

    p1 = Process(target= make_calculation_one, args=(number_list,))
    p2 = Process(target= make_calculation_two, args=(number_list,))
    p3 = Process(target= make_calculation_three, args=(number_list,))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()

    print(end-start)

    temp_a = results_a
    temp_b = results_b
    temp_c = results_c

    start = time.time()
    make_calculation_one(number_list)
    make_calculation_two(number_list)
    make_calculation_three(number_list)
    end = time.time()

    print(end - start)
    print(temp_a == results_a)
    print(temp_b == results_b)
    print(temp_c == results_c)





#! PARALLEL VS SEQUENTIALIZATION RUNNING BUT USING MANAGER


from multiprocessing import Process, Manager
import time
import math

def make_calculation_one(numbers, results_a):
    for number in numbers:
        results_a.append(math.sqrt(number ** 3))

def make_calculation_two(numbers, results_b):
    for number in numbers:
        results_b.append(math.sqrt(number ** 4))

def make_calculation_three(numbers, results_c):
    for number in numbers:
        results_c.append(math.sqrt(number ** 5))

if __name__ == '__main__':
    number_list = list(range(1000000))
    manager = Manager()
    results_a = manager.list()
    results_b = manager.list()
    results_c = manager.list()

    p1 = Process(target=make_calculation_one, args=(number_list, results_a))
    p2 = Process(target=make_calculation_two, args=(number_list, results_b))
    p3 = Process(target=make_calculation_three, args=(number_list, results_c))

    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()

    print("Parallel processing time:", end - start)

    temp_a = list(results_a)
    temp_b = list(results_b)
    temp_c = list(results_c)

    results_a = []
    results_b = []
    results_c = []

    start = time.time()
    make_calculation_one(number_list, results_a)
    make_calculation_two(number_list, results_b)
    make_calculation_three(number_list, results_c)
    end = time.time()

    print("Sequential processing time:", end - start)
    print(temp_a == results_a)
    print(temp_b == results_b)
    print(temp_c == results_c)


#! MULTIPROCESSING WHEN USING PIPE

from multiprocessing import Process, Pipe

def worker(conn):
    conn.send("Hello from the worker process!")
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=worker, args=(child_conn,))
    p.start()
    p.join()
    message = parent_conn.recv()
    print(message)  # Output: Hello from the worker process!


#! MULTIPROCESSING WHEN USING PIPE BUT COMPLEX

from multiprocessing import Process, Pipe

def worker(conn, value):
    conn.send(value)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    
    processes = []
    for i in range(10):
        p = Process(target=worker, args=(child_conn, i))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    results = []
    while parent_conn.poll():
        results.append(parent_conn.recv())
    
    print(results)


    

# ! USING MULTIPROCESSINNG WITH A QUEUE


from multiprocessing import Process, Queue

def worker(queue, value):
    queue.put(value)

if __name__ == '__main__':
    queue = Queue()
    
    processes = []
    for i in range(10):
        p = Process(target=worker, args=(queue, i))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    results = []
    while not queue.empty():
        results.append(queue.get())

    print(results)






# ! USING MULTIPROCESSINNG WITH A QUEUE BUT COMPLEX

from multiprocessing import Process, Queue
from time import sleep

def worker(queue, id):
    
    sleep(id)
    queue.put(f"Message from Worker {id}")
    msg = queue.get()
    print(f"Worker {id} received: {msg}")


if __name__ == '__main__':
    queue = Queue()

    process = []

    for i in range(3):
        p = Process(target= worker, args= (queue, i))
        process.append(p)
        p.start()

    
    for i in range(3):
        msg = queue.get()
        print(f"Main worker {i} received : {msg}")
        queue.put(f"From Main process to worker: {i}")

    for  p in process:
        p.join()

    
    queue.close()




