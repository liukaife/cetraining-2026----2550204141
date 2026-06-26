"""
feature_demo.py
实验二：分支操作与新功能开发
在新分支 feature-add-function 中实现的新函数。
"""


def calculate_average(numbers):
    """
    计算列表的平均值。

    Args:
        numbers: 数字列表（int 或 float）

    Returns:
        float: 列表的平均值，若列表为空则返回 None

    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([])
        None
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    计算列表的中位数。

    Args:
        numbers: 数字列表（int 或 float）

    Returns:
        float: 列表的中位数，若列表为空则返回 None

    Examples:
        >>> calculate_median([1, 2, 3, 4, 5])
        3
        >>> calculate_median([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        return None
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2


def calculate_variance(numbers):
    """
    计算列表的方差（总体方差）。

    Args:
        numbers: 数字列表（int 或 float）

    Returns:
        float: 列表的方差，若列表长度小于 2 则返回 None

    Examples:
        >>> calculate_variance([1, 2, 3, 4, 5])
        2.0
    """
    if len(numbers) < 2:
        return None
    avg = sum(numbers) / len(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


if __name__ == "__main__":
    # 测试数据
    data = [1, 2, 3, 4, 5]

    print("测试数据:", data)
    print("平均值:", calculate_average(data))
    print("中位数:", calculate_median(data))
    print("方差:", calculate_variance(data))