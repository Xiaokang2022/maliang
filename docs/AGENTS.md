# 文档

## 指令

- `mkdocs build`: 构建文档
- `mkdocs serve --livereload`: 构建并预览当前文档站

## 语法

- Markdown 格式
- 支持 [Python-Markdown/markdown](https://github.com/Python-Markdown/markdown) 和 [facelessuser/pymdown-extensions](https://github.com/facelessuser/pymdown-extensions) 扩展语法。
- 通过 `#lang XXX` 格式进行内敛语法高亮，如 `#py print`
- 所有代码块须标注语言

## 标题

- H1: `# XXX`，无需数字开头，H1 有且仅有一个
- H2: `## 一、XXX`，中文数字开头
- H3: `### 1.1 XXX`，阿拉伯数字开头
- H4: `#### 1.1.1 XXX`，阿拉伯数字开头
- H5: 禁止使用，如需，改用列表或加粗
- H6: 禁止使用

标题间不建议留空，推荐：

```markdown
# Title

XXX

## Subtitle

XXX
```

不推荐：

```markdown
# Title

## Subtitle

XXX
```
