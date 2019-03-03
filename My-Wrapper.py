from functools import wraps
import logging
import time
import traceback


def my_logging(original_function):

    logging.basicConfig(filename='Logs/{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):

        try:
            t1 = time.time()
            result = original_function(*args, **kwargs)
            t2 = time.time() - t1

        except Exception as e:
            logging.error(time.strftime('%m/%d/%Y, %H:%M:%S ',time.localtime()) + traceback.format_exc())
            raise e

        logging.info('[{}] {} ran for {} secs with args: {} and kwargs: {}'.format(time.strftime('%m/%d/%Y, %H:%M:%S ',time.localtime()),original_function.__name__, t2,*args, **kwargs))

        return result
    return wrapper


@my_logging
def display_info(name, age):

    time.sleep(1)
    print('Display info ran with arguments {} {}'.format(name, age))


display_info('John', 29)