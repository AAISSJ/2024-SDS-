import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())

# def fibo(num):
#     if num==0:
#         return 0
#     if num==1:
#         return 1 
#     return fibo(num-2)+fibo(num-1)

# print(fibo(N))

tmp = [0,1,1]
for i in range(3,N+1):
    tmp.append(tmp[i-1]+tmp[i-2])
print(tmp[N])
