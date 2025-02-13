# 반복 문자 지우기

def func(arr):  # 재귀함수 사용

    for i in range(len(arr) - 1):  # (들어오는 문자의 길이 - 1)만큼 반복해서 그 다음의 글자를 비교함
        if i < len(arr) - 1:  # 재귀함수가 동작하는 동안 arr 의 길이가 변하는데, 그 때 오류를 막기 위해 i가 범위를 넘을 경우 수행하지 않도록 함.
            if arr[i] == arr[i + 1]:  # 해당 순번의 문자와 그 다음 문자를 비교해서 같다면
                arr.pop(i + 1)
                arr.pop(i)  # 두 문자를 뽑아 버리고
                func(arr)  # 함수를 다시 실행
    return  # 아무것도 return 하지 않음
    # 이를 통해 arr 의 같은 글자를 모두 뽑아 버릴 수 있음.


T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    arr = list(input())  # 정보를 입력

    func(arr)  # 재귀함수를 사용

    result = len(arr)  # 가공된 arr 의 길이를 출력
    print(f'#{tc} {result}')
