import random

def descending_array():
    N=int(input("Enter length of an array: "))
    A = []
    for i in range(int(N)):
        m = random.randint(0, 2)
        A.append(m)
    print("Array: ", A)
    A.sort(reverse=True)
    print("Descending array: ", A)

if __name__=="__main__":
    descending_array()