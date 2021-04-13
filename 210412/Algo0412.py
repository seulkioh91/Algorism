# # 선택 정렬 알고리즘
# arr = [12, 13, 11, 14, 10]

# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         indexMin = i         # 최소값 찾는 처리
#         for k in range(i+1, len(arr)):
#             if arr[k] < arr[indexMin]:
#                 indexMin = k
#         w = arr[i] # 교환하는 처리
#         arr[i] = arr[indexMin]
#         arr[indexMin] = w
#     return arr

# print(selection_sort(arr))

# [모범답안]
# def Ssort(array):
#     for i in range(len(array)):
#         indexMin = i #임시로 인덱스 0을 최소값으로 설정
#         for k in range(i+1, len(array)):
#             if array[k] < array[indexMin]: ## 0번째와 1번째 비교
#                 indexMin = k # 1번째가 작으면 1번째를 작은값(최소값)으로 설정
#         array[i], array[indexMin] = array[indexMin], array[i] #교환하는 처리
#     return array

# array = [12,13,11,14,10]
# print(Ssort(array))

# # [위소현님 답]
# array = [12,13,11,14,10]
# for i in range(len(array)):         # array길이만큼 돌린다
#     w = array[i]                    # 임시변수 w에 i(0번째) 임시 최소값 설정
#     indexMin = array.index(min(array[i:])) # 제일 작은 값 10
#     array[i] = array[indexMin]      # 10(최소값)을 0번째로 옮기기
#     array[indexMin] = w             # 임시 변수에 넣어두었던 값과 교환
# print(array)                        # array 출력

#단순교환법 = 버블정렬
array = [5,3,4,1,2]

def change(array):
for i in range(len(array)):
i = array
for j in range(len(array)<len(i)):
if array[i] < array[i-1]:
w = array[i-1]
array[i] = array[i-1]
w = array[i]
i=i-1
j=j+1
return array
print(change(array))
