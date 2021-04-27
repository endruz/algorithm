# [0938. 二叉搜索树的范围和](https://leetcode-cn.com/problems/range-sum-of-bst)

难度：简单

---

## 题目

给定二叉搜索树的根结点 `root`，返回值位于范围 `[low, high]` 之间的所有结点的值的和。

示例 1：

![示例 1](images/bst1.jpg "示例 1")

```txt
输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32
```

示例 2：

![示例 2](images/bst2.jpg "示例 2")

```txt
输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23
```

提示：

- 树中节点数目在范围 `[1, 2 * 10^4]` 内
- `1 <= Node.val <= 10^5`
- `1 <= low <= high <= 10^5`
- 所有 `Node.val` **互不相同**
