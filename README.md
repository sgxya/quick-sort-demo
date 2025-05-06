# quick-sort-demo

这是一个 Python 实现的排序算法集合，包含了多种经典排序算法的实现。

## 支持的排序算法

目前实现了以下排序算法：

1. 快速排序 (Quick Sort)
   - 时间复杂度：平均 O(n log n)，最坏 O(n²)
   - 空间复杂度：O(log n)
   - 特点：原地排序，不稳定排序

2. 归并排序 (Merge Sort)
   - 时间复杂度：O(n log n)
   - 空间复杂度：O(n)
   - 特点：稳定排序

3. 插入排序 (Insertion Sort)
   - 时间复杂度：最好 O(n)，平均和最坏 O(n²)
   - 空间复杂度：O(1)
   - 特点：原地排序，稳定排序，对于小规模或基本有序的数据效率高

4. 冒泡排序 (Bubble Sort)
   - 时间复杂度：最好 O(n)，平均和最坏 O(n²)
   - 空间复杂度：O(1)
   - 特点：原地排序，稳定排序

## 使用方法

1. 导入排序模块：
```python
from sorting_algorithms import quick_sort, merge_sort, insertion_sort, bubble_sort
```

2. 使用示例：
```python
# 准备测试数据
arr = [3, 6, 8, 10, 1, 2, 1]

# 使用快速排序
sorted_arr = quick_sort(arr)
print("快速排序结果:", sorted_arr)

# 使用归并排序
sorted_arr = merge_sort(arr)
print("归并排序结果:", sorted_arr)

# 使用插入排序
sorted_arr = insertion_sort(arr)
print("插入排序结果:", sorted_arr)

# 使用冒泡排序
sorted_arr = bubble_sort(arr)
print("冒泡排序结果:", sorted_arr)
```

## 性能比较

各排序算法的性能特点：

| 算法 | 平均时间复杂度 | 最好情况 | 最坏情况 | 空间复杂度 | 稳定性 |
|------|----------------|----------|-----------|------------|--------|
| 快速排序 | O(n log n) | O(n log n) | O(n²) | O(log n) | 不稳定 |
| 归并排序 | O(n log n) | O(n log n) | O(n log n) | O(n) | 稳定 |
| 插入排序 | O(n²) | O(n) | O(n²) | O(1) | 稳定 |
| 冒泡排序 | O(n²) | O(n) | O(n²) | O(1) | 稳定 |

## 注意事项

- 所有排序函数都不会修改原始数组，而是返回一个新的已排序数组
- 对于小规模数据（n < 50），插入排序可能比快速排序和归并排序更快
- 对于接近有序的数据，插入排序的性能接近 O(n)
- 如果稳定性很重要，应选择归并排序、插入排序或冒泡排序
- 如果空间是主要考虑因素，应选择插入排序或冒泡排序
