sequence = [0, 1]
def fibonacci(n):
    if n <= 0:
        return 0   
    elif n <= len(sequence):
        return sequence[n-1] 
    else:

        nth = fibonacci(n-1) + fibonacci(n-2)
        sequence.append(nth)  
        return nth 

n = int(input("How many sequences? "))

fibonacci(n)
print(sequence)
