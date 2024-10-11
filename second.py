import re
from typing import Callable

def generator_numbers(text:str):
    return re.finditer(r'\d+\.?\d*',text)


def sum_profit(text:str, func:Callable):
    sum=0
    iter=func(text)
    while True:
        try:
           sum+=float(next(iter)[0])
        except StopIteration:
            break
    return sum

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__=='__main__':
    main()