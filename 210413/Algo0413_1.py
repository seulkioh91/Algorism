def Quick_sort(a):
    n=len(a)
    if n<=1:
        return a
    pivot = a[-1]
    g_left=[]
    g_right=[]
    for i in range(0,n-1):
        if a[i]<=pivot:
            g_left.append(a[i])
        else:
            g_right.append(a[i])
    return Quick_sort(g_left)+[pivot]+Quick_sort(g_right)

d=[8,12,1,9,102,25,32,98,31]
print(Quick_sort(d))
