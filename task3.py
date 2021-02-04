#!/usr/bin/python
#Assignment 01
def calc(): #function
    numbers = []  # list of numbers
    while True:     #while loop
        try:        # lets you test a block of code for errors
            number = int(input("Enter an number: "))  # get user input as int

            # abs: will return an absolute number, ex; -10 -> 10
            # if number is 0 it will return false and break loop
            # if absolture number is greater than 0
            if abs(number):
                numbers.append(number)  # append number to list
                continue  # will return to the start of the loop
            print("Ending loop!")
            break  # break loop
        except ValueError:
            print("Only numbers! Exiting")
            break
        except Exception as e:  # catch any exception and print (handle the error)
            print(e)

    # sum(iterable) -> return the sum of a list
    print(f"Sum of numbers {sum(numbers)}") #execute code


calc()  # call function