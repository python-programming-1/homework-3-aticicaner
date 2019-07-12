def collatz(num):
    if (num % 2 == 0):
        return num / 2
    elif (num % 2 == 1):
        return num * 3 + 1
    
print("enter a positive integer: ")

try:
    num_input = int(input())
    if(num_input < 0):
        print("Positive integers only")
    while(num_input > 1):
        num_input = int(collatz(num_input))
        print(num_input)
except:
    print("Please use numeric values for an integer")

