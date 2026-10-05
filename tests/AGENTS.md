# 测试

## 指令

- `pytest .`: 执行当前目录下所有测试用例
- `pytest test_file.py`: 执行某个模块的测试用例

## 执行测试

使用 `pytest` 进行测试。如果处于集成开发环境中（如 VSCode），先尝试调用 IDE 的相关工具或接口进行测试来直观地看到结果。如果不行再选择通过切换到项目根目录并执行命令 `pytest -v .` 的方式进行测试。

## 约定

- 仅编写 UT，使用 `unittest` 框架编写，禁止使用其余第三方测试框架
- 测试文件和目录名称使用 `test_*` 格式
- 只要求测试用例是否全部通过，对代码覆盖率无要求
- 修复失败测试用例时，如果不是源代码存在问题，则禁止修改源代码
- 测试中的窗口一律通过 `tests.window()` 创建（共享根窗口的 `Toplevel`），禁止在测试中直接创建或销毁 `containers.Tk`：
  在 macOS 上反复创建并销毁 `Tk` 根窗口会让 Tk Aqua 引用已销毁的 Tcl 解释器，导致后续任意窗口的 `update()`
  崩溃（Tk 8.6 触发 `Tcl_Panic` 中止，Tk 9.0 段错误），即 CI 上 macOS 作业的偶现失败，详见 `tests/__init__.py`
  与 <https://github.com/python/cpython/issues/123204>

## 代码风格

测试代码在[源代码风格](../src/AGENTS.md#代码风格)基础上，没有以下约束：

- 无需限制单行最大字符数
- 无需在代码注释和文档字符串中使用英文
- 无需使用 `pylint` 校验代码风格
- 无需类型注解在函数和方法的参数和返回值
- 无需包含 `from __future__ import annotations` 导入
