def caching_fibonacci():
     cache = {}
     def fibonacci(n):
         if n <= 0:
             return 0
         if n == 1:
             return 1
         if n in cache:         # Якщо результат є - повераєм
             return cache[n]
         cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Або обчислили та зберегли в кеш
         return cache[n]
     return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))