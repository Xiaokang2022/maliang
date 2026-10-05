# maliang

`maliang` 是基于 `tkinter` 模块且控件都由画布绘制的轻量级纯 Python UI 框架。

## 结构

- `src/`: 源代码（非平铺结构）
- `tests/`: 测试代码（单元测试）
- `docs/`: 文档，遵循开源项目 [`mkdocs`](https://github.com/mkdocs/mkdocs) 和 [`material`](https://github.com/squidfunk/mkdocs-material) 目录结构
- `.agents/`: 智能体相关文件
- `.github/`: GitHub 相关文件
- `README.md`: 自述文件
- `README.*.md`: 其它翻译的自述文件
- `LICENSE.txt`: 开源许可证
- `CHANGELOG.md`: 版本发布日志
- `CONTRIBUTING.md`: 贡献指南
- `CODE_OF_CONDUCT.md`: 行为准则
- `SECURITY.md`: 安全漏洞说明
- `CITATION.cff`: 引用信息
- `pyproject.toml`: 项目配置
- `mkdocs.yml`: 文档构建配置

## 维护

- 提交信息按照 [约定式提交](https://github.com/conventional-commits/conventionalcommits.org) 规范
- 版本号按照 [语义化版本](https://github.com/semver/semver) 规范
- 版本更新时须同步更新 `CHANGELOG.md`、`CITATION.cff`、`pyproject.toml`
- 临时分支合并后须删除

## 安全

- 禁止写入任何密码、密钥
- 禁止在非 Git 忽略的文件中写入任何环境信息
