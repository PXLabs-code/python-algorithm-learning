# python-algorithm-learning

使用 Python 学习算法与数据结构，持续记录题解、笔记和学习进度。

## Notebook

Notebook 按“题目与思路在上、可运行代码在下”的结构编写，并包含正确性断言、边界测试和 `timeit` 效率测试。

| 内容 | GitHub | Google Colab |
| --- | --- | --- |
| 两数之和完整示例 | [打开 Notebook](notebooks/two_sum.ipynb) | [在线运行](https://colab.research.google.com/github/PXLabs-code/python-algorithm-learning/blob/main/notebooks/two_sum.ipynb) |
| 新题模板 | [复制模板](notebooks/problem_template.ipynb) | [在线运行](https://colab.research.google.com/github/PXLabs-code/python-algorithm-learning/blob/main/notebooks/problem_template.ipynb) |

## 本地测试

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

测试会验证算法的常见与边界输入、Notebook JSON 结构，并依次执行“两数之和”Notebook 的全部代码单元。GitHub Actions 会在每次推送和 Pull Request 时自动运行相同测试。
