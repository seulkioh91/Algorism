# n이하의 소수 찾기 (에라토스테네스의 체)

def solution(n):
    answer = []  # 소수를 담을 리스트
    number = [] # n이하의 수 중 소수를 파악할 리스트 / 소수가 아니면 -1을 표현(표시)
#1번째.. 기본 방 설정
    for i in range(n+1):
        number.append(i) # n까지의 모든 수를 number리스트에 담기 [1,2,3,4,5... n이하까지]
#2번째.. 소수 찾기. 아닌 방은 -1 넣기
    for i in range(2, n+1, 1): # i = 2부터
        if i == -1:
            continue
        j = 0
        for j in range(i + i, n + 1, i): 
            number[j] = -1 #소수가 아닌 방에는 -1을 담기
#3번째.. -1이 아닌 방의 개수 세기 (=소수의 개수)
    for i in range(2, n +1):
        if number[i] != -1: #값이 -1이 아닌 방 번호가 소수
            answer.append(number[i])
    return answer


print(solution(10))