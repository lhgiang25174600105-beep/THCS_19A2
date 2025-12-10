# dãy Fibonacci 
# F(n) = 1 khi n = 1 
# F(n) = 2 khi n = 2
# F(n) = F(n-1) + F(n-2) khi n>2
n = int(input("Nhập số nguyên dương n: "))
def tim_so_fibonacci(n):
    if (n==1 or n==2):
        return 1
    else: 
        return tim_so_fibonacci(n-1) + tim_so_fibonacci(n-2)
if n<0:
    print("Yêu cầu nhập số nguyên dương")
else:
    print(tim_so_fibonacci(n))