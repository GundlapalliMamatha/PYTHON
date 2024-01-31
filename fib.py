fib_series = [0, 1]
for _ in range(8):  
    fib_series.append(fib_series[-1] + fib_series[-2])

print(fib_series)