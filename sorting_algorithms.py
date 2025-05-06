"""
排序算法模块

这个模块包含了各种排序算法的实现。
目前实现的算法：
1. 快速排序 (quick_sort)
2. 归并排序 (merge_sort)
3. 插入排序 (insertion_sort)
"""

def quick_sort(arr):
    """
    快速排序算法实现
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # 选择中间元素作为基准值
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """
    归并排序算法实现
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    """
    if len(arr) <= 1:
        return arr
    
    # 将数组分成两半
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # 递归排序两半
    left = merge_sort(left)
    right = merge_sort(right)
    
    # 合并两个有序数组
    return merge(left, right)

def merge(left, right):
    """
    合并两个有序数组
    
    Args:
        left (list): 左半部分有序数组
        right (list): 右半部分有序数组
    
    Returns:
        list: 合并后的有序数组
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def insertion_sort(arr):
    """
    插入排序算法实现
    
    Args:
        arr (list): 待排序的列表
    
    Returns:
        list: 排序后的列表
    """
    # 创建输入数组的副本
    arr = arr.copy()
    
    # 从第二个元素开始遍历
    for i in range(1, len(arr)):
        key = arr[i]
        # 将key插入到已排序的序列中
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr

def test_sorting_algorithm(sort_func, test_array):
    """
    测试排序算法的辅助函数
    
    Args:
        sort_func (callable): 排序函数
        test_array (list): 测试数组
    
    Returns:
        tuple: (原始数组, 排序后数组)
    """
    sorted_array = sort_func(test_array.copy())
    return test_array, sorted_array

if __name__ == "__main__":
    # 测试用例
    test_array = [3, 6, 8, 10, 1, 2, 1]
    
    # 测试快速排序
    print("\n测试快速排序:")
    original, sorted_result = test_sorting_algorithm(quick_sort, test_array)
    print("原始数组:", original)
    print("排序后数组:", sorted_result)
    
    # 测试归并排序
    print("\n测试归并排序:")
    original, sorted_result = test_sorting_algorithm(merge_sort, test_array)
    print("原始数组:", original)
    print("排序后数组:", sorted_result)
    
    # 测试插入排序
    print("\n测试插入排序:")
    original, sorted_result = test_sorting_algorithm(insertion_sort, test_array)
    print("原始数组:", original)
    print("排序后数组:", sorted_result)