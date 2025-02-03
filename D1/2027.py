# 대각선 출력하기

def diag():
    a = ['+', '+', '+', '+', '+']
    x = 0
    while x < len(a):
        a[x] = '#'
        for i in a:
            print(i, end = "")
        print("")
        a = ['+', '+', '+', '+', '+']
        x += 1

diag()

# 하드코딩 해도 됐던건데...