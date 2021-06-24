# [0149. 直线上最多的点数](https://leetcode-cn.com/problems/max-points-on-a-line)

难度：困难

---

## 题目

给你一个数组 `points` ，其中 `points[i] = [xi, yi]` 表示 **X-Y** 平面上的一个点。求最多有多少个点在同一条直线上。

示例 1：

![示例 1](./images/plane1.jpg "示例 1")

```txt
输入：points = [[1,1],[2,2],[3,3]]
输出：3
```

示例 2：

![示例 2](./images/plane2.jpg "示例 2")

```txt
输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4
```

提示：

- `1 <= points.length <= 300`
- `points[i].length == 2`
- `-10^4 <= xi, yi <= 10^4`
- `points` 中的所有点 **互不相同**
