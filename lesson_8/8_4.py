def val_checker(func):
    def sec_val_cheker(sec_func):
        def wraper(args):
            if type(args) != int or type(args) != float:
                raise  ValueError
            elif func(args) == False:
                raise ValueError
            print(sec_func(args))
        return wraper
    return sec_val_cheker



@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

try:
    calc_cube('asfdasdf')
except ValueError:
    print("Что то пошло не так")

