import datetime

def log(func):
    def wrapper(*args, **kwargs):
        timestamp=datetime.datetime.now()
        function_name=func.__name__
        log_file=f'{timestamp}-{function_name}called\n'

        with open('log.txt','a',encoding='UTF-8') as file:
            file.write(log_file)

        return func(*args, **kwargs)
    return wrapper