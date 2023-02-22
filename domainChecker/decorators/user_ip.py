import datetime as dt
import os


def get_ip(function):
    def wrapper(*args):
        def get_ip_func():
            os.system('curl ifconfig.me')

        function(*args)
        
        with open("/Users/lilko.petkov/Desktop/python_decorators/logs/ip_execution_log.txt", "a") as log_file:
            log_file.write(f"{dt.datetime.now()} - User IP: {get_ip_func()}")
            
        return "Response logged succesffully. "
    
    return wrapper
