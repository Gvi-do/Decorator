from logo import get_logo
from Logo_2 import log_path

@log_path('foo.log')
def summa(a,b):
    return a + b

summa(2,5)


@get_logo
def summ(a,b):
    return a + b

summ(3,6)
