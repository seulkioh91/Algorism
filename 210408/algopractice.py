# 선형탐색법

def Lsearch(x, y):
    for i in range(len(x)):
        if x[i] == y:
            return "%d번째의 요소가 일치" %i
            
    return "찾지 못했습니다."

x = [4,2,3,5,1]
y = 1
z = Lsearch(x,y)
print(z)