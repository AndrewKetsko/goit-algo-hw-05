def caching_fibonacci():
    cached_fibonacci={}
    def fibonacci(n):
        if n<1:
            return 0
        if n==1:
            return 1
        if n in cached_fibonacci:
            return cached_fibonacci[n]
        
        cached_fibonacci[n]=fibonacci(n-1)+fibonacci(n-2)
        return cached_fibonacci[n]
    
    return fibonacci

def main():
    fib=caching_fibonacci()
    print(fib(4))
    print(fib(10))
    print(fib(5))

if __name__=='__main__':
    main()