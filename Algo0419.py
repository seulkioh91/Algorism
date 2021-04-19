# def euclid(x,y):
#     t = x % y            #x와 y 두 수의 나머지 t를 구한다
#     while t!=0:                # 반복문 조건 t !=0
#         y = x            # y값을 x에 
#         t = y            # t값을 y에
#         t = x%y          # x와 y의 나머지 t를 구한다.

#     return abs(y)                # return y 값을 반환

# euclid(12,8)
# euclid(221, 143)

def euclid(x,y):
  t = x % y
  while t != 0 :
    x,y = y,x 
    t = x%y

  return y

euclid(12,8)