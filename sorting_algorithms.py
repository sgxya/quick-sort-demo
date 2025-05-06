"""
排序算法模块

这个模块包含了各种排序算法的实现。
目前实现的算法：
1. 快速排序 (quick_sort)
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

# 为了方便测试，添加一个简单的测试函数
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
    original, sorted_result = test_sorting_algorithm(quick_sort, test_array)
    print("原始数组:", original)
    print("排序后数组:", sorted_result)