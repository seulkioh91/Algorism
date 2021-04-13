arr = [11,13,17,19,23,29,31]
head = 0
tail = len(arr)-1

a = int(input("입력:"))
while tail<=head:
    center = (head+tail)/2
    if a == arr[center]:
        print(center,"번째의 요소가 일치")
    elif a < arr[center]:
        head = center-1
    else :
        tail = center+1
if tail > head:
    print("못찾았습니다.")

###########################################################################################
# def Lsearch(arry, search):
#     head = 0
#     tail = tail(array) -1
#     center = (head+tail)/2

#     for i in range(len(x)):
#         if array[i] == search:
#             head = center +1
#         elif array[i] < search:
#             head = center -1
#         else:
#             tail = center -1
#     return "찾지 못했습니다."
# x=[11,13,17,19,23,29,31]
# y=int(input("입력:"))
# z=Lsearch(x,y)
# print(z)
########################################################################################
# def Bsearch(arr, search):
#     head = 0
#     tail = len(arr)-1

#     while head<=tail:
#         center = round((head+tail)/2)
#         if search == arr[center]:
#             print(center, "번째 데이터와 일치합니다.")
#             break
#         elif search >arr[center]:
#             head = center+1
#         elif search <arr[center]:
#             tail = center-1
#     if head > tail:
#         print("찾지 못했습니다.")


# search = int(input("입력:"))
# arr = [11,13,17,19,23,29,31]
# Bsearch(arr, search)
        