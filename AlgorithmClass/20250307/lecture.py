# 컴퓨터의 연산 과정
# 1. 각 수를 이진수로 변환한다.
# 2. 각 자리에 and, or 연산을 수행한다.
print(7 & 5)
print(7 | 5)

# 이진수 출력, 16진수 출력이 가능하다.
print(bin(7 & 5))
print(bin(10))
print(hex(10))

# int 의 10진수로의 변환이 가능하다.
print(int('1011', 2))
print(int('b', 16))

print(bin(0b11011110 & 0b11011))
print(bin(0x4A3 | 25))
print(hex(0x4A3 | 25))


decode_num = 1004
print(7070 ^ decode_num)
print(6258 ^ decode_num)


print(bin(0b1101 << 2))  # l-shift 했을 때 좌측에 자리가 없다면 우측 끝에 0이 추가된다. l-shift = 2배 커진다.
print(bin(0b1101 >> 2))  # r-shift 했을 때 우측에 자리가 없다면 우측 끝의 값이 삭제된다. r-shift = 2로 나눈 몫이 된다.

print(1 << 1)  # 0b10
print(1 << 2)  # 0b100
print(1 << 3)  # 0b1000
print(1 << 4)  # 0b10000

print(15 >> 1)  # 0b111
print(15 >> 2)  # 0b11
print(15 >> 3)  # 0b1
print(15 >> 4)  # 0

num = 1
for _ in range(5):
    print(num, bin(num))
    num = num << 1


# bit 연산은 어디에 쓰는 것인가?
# 1. 부분집합의 수를 바로 구할 수 있다.
arr = [1, 2, 3, 4]  # 16개
print(1 << len(arr))

for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
        # i 번째 부분집합에 특정 숫자가 포함되어 있는지 확인 가능 = i 의 idx 번째 bit 가 1인지 확인.
        if i & (1 << idx):
            print(arr[idx], end=' ')
    print()

arr = [1, 2, 3, 4, 5, 6]
for i in range(1 << len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
    if total == 10:
        print(f'부분집합: {subset}')


# 음수 표현 방법
print(bin(5))
print(bin(-5))


# not 연산
print(~4, bin(~4))
print(~(-4))