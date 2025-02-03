# 두 개의 숫자열

T = int(input())
 
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if(n>m):
        a,b = b,a
        n,m = m,n
    #항상 b, m가 더 큼
    result = 0
    for i in range(m-n+1):
        cal = 0
        sb = b[i:i+n]
        for j in range(n):
            cal += a[j] * sb[j]
        result = max(result,cal)
    print(f"#{test_case} {result}")