from functools import wraps
import logging
import time


def my_logging(original_function):

    logging.basicConfig(filename='Logs/{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info('{} ran with args: {} and kwargs: {}'.format(original_function.__name__,*args, **kwargs))

        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):

    @wraps(original_function)
    def wrapper(*args, **kwargs):

        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1

        print('{} ran in: {} secs'.format(original_function.__name__, t2))

        return result

    return wrapper


@my_logging
@my_timer
def display_info(name, age):

    time.sleep(1)
    print('Display info ran with arguments {} {}'.format(name, age))


display_info('John', 29)