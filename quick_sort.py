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

def main():
    # 测试用例
    test_array = [3, 6, 8, 10, 1, 2, 1]
    print("原始数组:", test_array)
    sorted_array = quick_sort(test_array)
    print("排序后数组:", sorted_array)

if __name__ == "__main__":
    main() 
