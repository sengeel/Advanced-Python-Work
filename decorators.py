# import logging
# from abc import ABC, abstractmethod
# from math import sqrt
# from time import perf_counter


# def is_prime(number : int) -> bool:
#     if number < 2:
#         return False
#     for element in range(2, int(sqrt(number)) + 1):
#         if number % element == 0:
#             return False
        
#     return True


# class AbstractComponent(ABC):
#     @abstractmethod
#     def execute(self, upper_bound : int) -> int:
#         pass


# class ConcreteComponent(AbstractComponent):
#     def execute(self, upper_bound: int) -> int:
#         count = 0
#         for number in range(upper_bound):
#             if is_prime(number):
#                 count += 1
#         return count
    
# class AbstractDecorator(AbstractComponent):
#     def __init__(self, decorated : AbstractComponent) -> None:
#         self._decorated = decorated

# class BenchmarkDecorator(AbstractDecorator):
#     def execute(self, upper_bound: int ) -> int:
#         start_time = perf_counter()
#         value = self._decorated.execute(upper_bound)
#         end_time = perf_counter()
#         run_time = end_time - start_time
#         logging.info(
#             f"Execution of {self._decorated.__class__.__name__} took {run_time:.2f} seconds"
#         )
#         return value
    

# def main() -> None:
#     logging.basicConfig(level= logging.INFO)
#     component = ConcreteComponent()
#     benchmark_decorator = BenchmarkDecorator(component)
#     value =benchmark_decorator.execute(100000)
#     logging.info(f"Found {value} prime numbers.")


# if __name__ == '__main__':
#     main()


def mydecorator(function):

    def wrapper(*args, **kwargs):
        print("I'm decorating your function")
        return_value =  function(*args, **kwargs)
        return return_value


    return wrapper

@mydecorator
def hello(person):
    print(f"Hello {person}")
    return f"Hello {person}"

print(hello('person'))


def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}")
            return value
    return wrapper

@logged
def add(x , y):
    return x + y

print(add(10, 20))



import time


def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after -  before} seconds to execute!")
        return value
    return wrapper

@timed
def myfunction(x):
    results= 1
    for i in range(1,x):
        results *= i
    return results

myfunction(1000)