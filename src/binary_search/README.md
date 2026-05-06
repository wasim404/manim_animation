# Binary Search Visualization

使用 Manim 制作的二分搜索可视化动画项目。

本项目通过动画演示二分搜索的核心思想，包括精确查找、时间复杂度、`lower_bound`、`upper_bound`、右边界问题以及 LeetCode 34 题。

---

## 项目简介

二分搜索是算法学习中的基础内容，但很多人容易在边界处理上出错。

本项目希望通过可视化动画，展示二分搜索中 `left`、`right`、`mid` 的变化过程，帮助理解二分搜索的执行逻辑。

---

## 内容结构

1. 二分搜索引入
2. 顺序遍历与二分查找对比
3. 时间复杂度 `O(log n)` 推导
4. 二分查找精确值
5. `lower_bound` 模板
6. `upper_bound` 模板
7. 右边界问题
8. LeetCode 34 题解析

---

## 项目结构

```text
binary_search/
├── assets/
│   ├── headphone.svg
│   ├── leetcode_34.png
│   
│
├── snippets/
│   ├── binsearch.py
│   ├── leetcode34.py
│   ├── lower_bound_code.py
│   ├── mid_code.py
│   └── upper_bound.py
│
├── binary_search_scene.py
└── README.md