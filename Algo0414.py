#소수판별코드

def is_prime(a):
    b = range(2, a)
    c = 0
    for i in b:
        if a%i == 0:
            c +=1
    if c>0:
        print('{}는 소수가 아니다.'.format(a))
        d=False
    else:
        print("{}는 소수이다.".format(a))
        d=True
    return d

is_prime(31)


# N이하의 수들 중 소수를 찾는 코드

a = range(1,101) #100까지
prime_numbers = [] #소수 list를 공집합으로 우선 만들고
for i in a: #1부터 100까지 중,
    c = is_prime(i) #i가 소수이면 c는 True, 아니면 False
    if c == True: #c가 True이면
        prime_numbers.append(i) #b에다가 i를 추가
print(prime_numbers)