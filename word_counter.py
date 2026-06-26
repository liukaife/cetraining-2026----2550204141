"""
单词频率统计工具
功能：统计一个文本文件中每个单词出现的次数
作者：刘凯飞
学号：2550204141
"""

import re
from collections import Counter


def count_words(file_path: str) -> dict:
    """
    统计文本文件中每个单词出现的次数。

    参数:
        file_path (str): 文本文件的路径

    返回:
        dict: 以单词为键、出现次数为值的字典，按次数降序排列

    说明:
        - 单词定义为连续的字母字符（忽略大小写差异）
        - 数字和标点符号不计入单词
        - 所有单词统一转换为小写进行统计
    """
    word_counter = Counter()

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # 使用正则表达式提取每行中的英文单词（仅字母字符）
                words = re.findall(r'[a-zA-Z]+', line)
                # 统一转为小写以便不区分大小写
                words_lower = [w.lower() for w in words]
                word_counter.update(words_lower)

    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 未找到，请检查路径是否正确。")
        return {}
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return {}

    # 按出现次数降序排列
    sorted_result = dict(word_counter.most_common())
    return sorted_result


def print_word_frequencies(word_dict: dict, top_n: int = None) -> None:
    """
    格式化打印单词频率统计结果。

    参数:
        word_dict (dict): count_words() 返回的字典
        top_n (int, 可选): 只打印前 N 个高频单词，默认打印全部
    """
    if not word_dict:
        print("没有统计到任何单词。")
        return

    items = list(word_dict.items())
    if top_n:
        items = items[:top_n]

    print(f"{'单词':<20} {'次数':>8}")
    print("-" * 30)
    for word, count in items:
        print(f"{word:<20} {count:>8}")


def save_results(word_dict: dict, output_path: str) -> None:
    """
    将统计结果保存到指定的输出文件。

    参数:
        word_dict (dict): count_words() 返回的字典
        output_path (str): 输出文件的路径
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"{'单词':<20} {'次数':>8}\n")
            f.write("-" * 30 + "\n")
            for word, count in word_dict.items():
                f.write(f"{word:<20} {count:>8}\n")
        print(f"统计结果已保存至：{output_path}")
    except Exception as e:
        print(f"保存文件时发生错误：{e}")


def get_top_words(word_dict: dict, n: int = 10) -> list:
    """
    获取出现频率最高的 N 个单词。

    参数:
        word_dict (dict): count_words() 返回的字典
        n (int): 需要返回的高频单词数量，默认为 10

    返回:
        list: 包含 (单词, 次数) 元组的列表
    """
    items = list(word_dict.items())
    return items[:n]


def get_word_count(word_dict: dict, word: str) -> int:
    """
    查询某个特定单词的出现次数。

    参数:
        word_dict (dict): count_words() 返回的字典
        word (str): 要查询的单词

    返回:
        int: 该单词的出现次数，若未出现则返回 0
    """
    return word_dict.get(word.lower(), 0)


# ========== 主程序入口 ==========
if __name__ == "__main__":
    # 示例用法：统计当前目录下 example.txt 文件的单词频率
    import sys

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "example.txt"

    print(f"正在统计文件：{input_file}")
    result = count_words(input_file)

    if result:
        total_words = sum(result.values())
        unique_words = len(result)
        print(f"\n总单词数：{total_words}，不重复单词数：{unique_words}\n")
        print_word_frequencies(result, top_n=20)

        # 输出前 10 个高频单词
        print("\n=== 前 10 个高频单词 ===")
        for word, count in get_top_words(result, 10):
            print(f"  {word}: {count} 次")

        # 保存结果
        save_results(result, "word_count_result.txt")