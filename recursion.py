# def fac(n):
#     if n==0:
#         return 1
#     return n*fac(n-1)

# print(fac(5))

def febo(n):
    if n<=1:
        return n
    return febo(n-1)+febo(n-2)

print(febo(7))

def sumof(n):
    if n<10:
        return n
    return n%10 + sumof(n//10)
print(sumof(1234))

def febo(n):
    if n<=1:
        return 1
    