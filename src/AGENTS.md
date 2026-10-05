# 源代码

## 指令

- `pip install -e .`: 切换到项目根目录时执行，以编辑模式安装模块到当前环境
- `pylint file.py`: 校验模块代码风格，不能出现 ERROR 级别问题，评分 9 分以上

## 版权声明

源代码中的文件，使用如下版权声明：

```python
# Copyright (c) 2023-20XX Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.
```

## 语法

- 使用最高 Python 3.15 并向下兼容 Python 3.11 的语法
- 类型注解通过 `typing-extensions` 模块兼容

## 代码风格

- 遵循 [PEP8](https://peps.python.org/pep-0008/) 规范
- 代码注释和文档字符串全用英文
- 函数和方法的参数和返回值需类型注解
- 导入模块而不是类或函数
- 允许少量使用 `# type: ignore` 注释来屏蔽类型检查器
- 函数或方法定义过长导致换行时，须换行所有参数而不是只换一行
- 非 `__init__.py` 文件须包含 `from __future__ import annotations`
