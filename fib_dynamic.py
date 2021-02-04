
def fibonacci(n):
    n1, n2 = 0, 1   
    if n <= 0:
        print(f"F{n} = {n}")
    elif n == 1:
        print(f"F{n} = {n}")
    else:
        print("Fibonacci sequence: ", end="")

        for _n in range(n):   
            print(n1, end=" ") 
            nth = n1 + n2
            n1, n2 = n2, nth
        print()


n = int(input("How many sequences? "))
fibonacci(n)
