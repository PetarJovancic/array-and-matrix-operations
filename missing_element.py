import random

### Prvi nacin:
# def missing_element():
#     N=input("Enter length of an array: ")
#     A = []
#     m = random.randint(1,int(N))
#     for i in range(int(N)):
#         while m not in A:
#             A.append(m)
#         while m in A:
#             m = random.randint(1,int(N)+1)
#     print("Array: ",A)
#     if m not in A:
#         print("Missing element is: ",m)

### Drugi nacin:
def missing_element():
    N=int(input("Enter length of an array: "))
    A = random.sample(range(1, N+2), N)
    print("Array: ", A)
    m=list(range(1, N+2))
    print("Missing element is: ", [x for x in m if x not in A])

if __name__=="__main__":
    missing_element()