# 백만 장자 프로젝트

line = [10, 1, 1, 10, 1, 8, 1, 9]
line_invert = line[::-1]
profit = []
# range(len(line)) 으로 0~끝까지 list 만들어주기
# 밑에서 검색하다가 조건 안 맞으면 list에서 갯수만큼 빼주기
# 밑의 반복 변수 자체를 list로 설정. 하면 될듯?

for i in range(1, len(line)):
    for j in range(i + 1, len(line) + 1):
        if line[-i] > line[-j]:
            print('big')
        else:            
            break
