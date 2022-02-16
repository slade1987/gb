from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*a, **kwargs):
        mas = []
        for i in a:
            mas.append(i)
        if kwargs.values() != 0:
            for i in kwargs:
                mas.append(kwargs[i])
        for i in mas:
            if type(i) == float or type(i) == int:
                print(func(i), ' : ', i, " : ", type(i))
        print(f'Имя функции = {func.__name__}')

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


print(calc_cube(5, 54, 545.5, name=5, Fio=44, ss='ffdfd'))
