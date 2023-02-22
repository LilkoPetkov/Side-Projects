import time
import datetime as dt
import os


def exec_time(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        end = time.time()
        
        with open("/Users/lilko.petkov/Desktop/python_decorators/logs/execution_log.txt", "a") as log_file:
            log_file.write(f"{dt.datetime.now()} - {function.__name__} took {end - start} to execute\n")
            
        return "Response logged succesffully. "
    
    return wrapper
