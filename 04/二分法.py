# # 二分法，判断有序的数组
# lst = [1,2,3,44,55,66,77,88,999,1212]
# n = int(input(">>>:"))
# left = 0
# right = len(lst) - 1
# while left <= right:
#     mid = (left + right) // 2  # 整除，只取到整数
#     if n < lst[mid]:
#         right = mid - 1
#     elif n > lst[mid]:
#         left = mid + 1
#     else:
#         print("找到这个数了位置在",mid)
#         break
# else:
#     print("找不到这个数")

# 递归版本的算法
lst = [1,2,3,44,55,66,77,88,999,1212]
n = int(input(">>>:"))
left = 0
right = len(lst) - 1
def find(n, left, right):
    mid = (left + right) // 2
    if left > right:
        print("没找到")
        return 0
    if n > lst[mid]:
        left = mid + 1
    elif n < lst[mid]:
        right = mid - 1
    else:
        print(f"找到这个数了位置在{mid}")
        return 0
    find(n,left,right)
find(n, left, right)