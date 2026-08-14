<h1 align="center">maliang</h1>

<p align="center"><img src="docs/logo.png" alt="Logo" title="Logo" /></p>

<p align="center"><a href="README.md">English</a> · <a href="README.zh-Hans.md">简体中文</a> · 繁體中文</p>

<p align="center"><a title="官方網站" href="https://xiaokang2022.github.io/maliang/">https://xiaokang2022.github.io/maliang/</a></p>

<p align="center">
一個基於 <code>tkinter</code> 且控件都由畫布繪製的羽量級 UI 框架
</p>

<p align="center">
<a href="https://github.com/Xiaokang2022/maliang/releases"><img alt="版本" title="版本" src="https://img.shields.io/github/v/release/Xiaokang2022/maliang?label=%e7%89%88%e6%9c%ac&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPQoid2hpdGUiIGQ9Ik0xIDcuNzc1VjIuNzVDMSAxLjc4NCAxLjc4NCAxIDIuNzUgMWg1LjAyNWMuNDY0IDAgLjkxLjE4NCAxLjIzOC41MTNsNi4yNSA2LjI1YTEuNzUgMS43NSAwIDAgMSAwIDIuNDc0bC01LjAyNiA1LjAyNmExLjc1IDEuNzUgMCAwIDEtMi40NzQgMGwtNi4yNS02LjI1QTEuNzUyIDEuNzUyIDAgMCAxIDEgNy43NzVabTEuNSAwYzAgLjA2Ni4wMjYuMTMuMDczLjE3N2w2LjI1IDYuMjVhLjI1LjI1IDAgMCAwIC4zNTQgMGw1LjAyNS01LjAyNWEuMjUuMjUgMCAwIDAgMC0uMzU0bC02LjI1LTYuMjVhLjI1LjI1IDAgMCAwLS4xNzctLjA3M0gyLjc1YS4yNS4yNSAwIDAgMC0uMjUuMjVaTTYgNWExIDEgMCAxIDEgMCAyIDEgMSAwIDAgMSAwLTJaIj48L3BhdGg+PC9zdmc+" /></a>
<a href="https://pypistats.org/packages/maliang"><img alt="下載" title="下載" src="https://img.shields.io/pypi/dm/maliang?label=%e4%b8%8b%e8%bc%89&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTIuNzUgMTRBMS43NSAxLjc1IDAgMCAxIDEgMTIuMjV2LTIuNWEuNzUuNzUgMCAwIDEgMS41IDB2Mi41YzAgLjEzOC4xMTIuMjUuMjUuMjVoMTAuNWEuMjUuMjUgMCAwIDAgLjI1LS4yNXYtMi41YS43NS43NSAwIDAgMSAxLjUgMHYyLjVBMS43NSAxLjc1IDAgMCAxIDEzLjI1IDE0WiI+PC9wYXRoPjxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNy4yNSA3LjY4OVYyYS43NS43NSAwIDAgMSAxLjUgMHY1LjY4OWwxLjk3LTEuOTY5YS43NDkuNzQ5IDAgMSAxIDEuMDYgMS4wNmwtMy4yNSAzLjI1YS43NDkuNzQ5IDAgMCAxLTEuMDYgMEw0LjIyIDYuNzhhLjc0OS43NDkgMCAxIDEgMS4wNi0xLjA2bDEuOTcgMS45NjlaIj48L3BhdGg+PC9zdmc+" /></a>
<a href="https://github.com/Xiaokang2022/maliang/actions"><img alt="檢查和測試" title="檢查和測試" src="https://img.shields.io/github/actions/workflow/status/Xiaokang2022/maliang/python-package.yml?label=%e6%aa%a2%e6%9f%a5%e5%92%8c%e6%b8%ac%e8%a9%a6&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTggMGE4IDggMCAxIDEgMCAxNkE4IDggMCAwIDEgOCAwWk0xLjUgOGE2LjUgNi41IDAgMSAwIDEzIDAgNi41IDYuNSAwIDAgMC0xMyAwWm00Ljg3OS0yLjc3MyA0LjI2NCAyLjU1OWEuMjUuMjUgMCAwIDEgMCAuNDI4bC00LjI2NCAyLjU1OUEuMjUuMjUgMCAwIDEgNiAxMC41NTlWNS40NDJhLjI1LjI1IDAgMCAxIC4zNzktLjIxNVoiPjwvcGF0aD48L3N2Zz4=" /></a>
<a href="https://codecov.io/gh/Xiaokang2022/maliang"><img alt="代碼覆蓋率" title="代碼覆蓋率" src="https://img.shields.io/codecov/c/github/Xiaokang2022/maliang?label=%e4%bb%a3%e7%a2%bc%e8%a6%86%e8%93%8b%e7%8e%87&logoColor=white&logo=codecov" /></a>
<br/>
<a href="https://github.com/Xiaokang2022/maliang/watchers"><img alt="關注" title="關注" src="https://img.shields.io/github/watchers/Xiaokang2022/maliang?label=%e9%97%9c%e6%b3%a8&style=flat&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTggMmMxLjk4MSAwIDMuNjcxLjk5MiA0LjkzMyAyLjA3OCAxLjI3IDEuMDkxIDIuMTg3IDIuMzQ1IDIuNjM3IDMuMDIzYTEuNjIgMS42MiAwIDAgMSAwIDEuNzk4Yy0uNDUuNjc4LTEuMzY3IDEuOTMyLTIuNjM3IDMuMDIzQzExLjY3IDEzLjAwOCA5Ljk4MSAxNCA4IDE0Yy0xLjk4MSAwLTMuNjcxLS45OTItNC45MzMtMi4wNzhDMS43OTcgMTAuODMuODggOS41NzYuNDMgOC44OThhMS42MiAxLjYyIDAgMCAxIDAtMS43OThjLjQ1LS42NzcgMS4zNjctMS45MzEgMi42MzctMy4wMjJDNC4zMyAyLjk5MiA2LjAxOSAyIDggMlpNMS42NzkgNy45MzJhLjEyLjEyIDAgMCAwIDAgLjEzNmMuNDExLjYyMiAxLjI0MSAxLjc1IDIuMzY2IDIuNzE3QzUuMTc2IDExLjc1OCA2LjUyNyAxMi41IDggMTIuNWMxLjQ3MyAwIDIuODI1LS43NDIgMy45NTUtMS43MTUgMS4xMjQtLjk2NyAxLjk1NC0yLjA5NiAyLjM2Ni0yLjcxN2EuMTIuMTIgMCAwIDAgMC0uMTM2Yy0uNDEyLS42MjEtMS4yNDItMS43NS0yLjM2Ni0yLjcxN0MxMC44MjQgNC4yNDIgOS40NzMgMy41IDggMy41Yy0xLjQ3MyAwLTIuODI1Ljc0Mi0zLjk1NSAxLjcxNS0xLjEyNC45NjctMS45NTQgMi4wOTYtMi4zNjYgMi43MTdaTTggMTBhMiAyIDAgMSAxLS4wMDEtMy45OTlBMiAyIDAgMCAxIDggMTBaIj48L3BhdGg+PC9zdmc+" /></a>
<a href="https://github.com/Xiaokang2022/maliang/forks"><img alt="復刻" title="復刻" src="https://img.shields.io/github/forks/Xiaokang2022/maliang?label=%e5%be%a9%e5%88%bb&style=flat&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTUgNS4zNzJ2Ljg3OGMwIC40MTQuMzM2Ljc1Ljc1Ljc1aDQuNWEuNzUuNzUgMCAwIDAgLjc1LS43NXYtLjg3OGEyLjI1IDIuMjUgMCAxIDEgMS41IDB2Ljg3OGEyLjI1IDIuMjUgMCAwIDEtMi4yNSAyLjI1aC0xLjV2Mi4xMjhhMi4yNTEgMi4yNTEgMCAxIDEtMS41IDBWOC41aC0xLjVBMi4yNSAyLjI1IDAgMCAxIDMuNSA2LjI1di0uODc4YTIuMjUgMi4yNSAwIDEgMSAxLjUgMFpNNSAzLjI1YS43NS43NSAwIDEgMC0xLjUgMCAuNzUuNzUgMCAwIDAgMS41IDBabTYuNzUuNzVhLjc1Ljc1IDAgMSAwIDAtMS41Ljc1Ljc1IDAgMCAwIDAgMS41Wm0tMyA4Ljc1YS43NS43NSAwIDEgMC0xLjUgMCAuNzUuNzUgMCAwIDAgMS41IDBaIj48L3BhdGg+PC9zdmc+" /></a>
<a href="https://github.com/Xiaokang2022/maliang/stargazers"><img alt="星標" title="星標" src="https://img.shields.io/github/stars/Xiaokang2022/maliang?label=%e6%98%9f%e6%a8%99&color=gold&style=flat&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTggLjI1YS43NS43NSAwIDAgMSAuNjczLjQxOGwxLjg4MiAzLjgxNSA0LjIxLjYxMmEuNzUuNzUgMCAwIDEgLjQxNiAxLjI3OWwtMy4wNDYgMi45Ny43MTkgNC4xOTJhLjc1MS43NTEgMCAwIDEtMS4wODguNzkxTDggMTIuMzQ3bC0zLjc2NiAxLjk4YS43NS43NSAwIDAgMS0xLjA4OC0uNzlsLjcyLTQuMTk0TC44MTggNi4zNzRhLjc1Ljc1IDAgMCAxIC40MTYtMS4yOGw0LjIxLS42MTFMNy4zMjcuNjY4QS43NS43NSAwIDAgMSA4IC4yNVptMCAyLjQ0NUw2LjYxNSA1LjVhLjc1Ljc1IDAgMCAxLS41NjQuNDFsLTMuMDk3LjQ1IDIuMjQgMi4xODRhLjc1Ljc1IDAgMCAxIC4yMTYuNjY0bC0uNTI4IDMuMDg0IDIuNzY5LTEuNDU2YS43NS43NSAwIDAgMSAuNjk4IDBsMi43NyAxLjQ1Ni0uNTMtMy4wODRhLjc1Ljc1IDAgMCAxIC4yMTYtLjY2NGwyLjI0LTIuMTgzLTMuMDk2LS40NWEuNzUuNzUgMCAwIDEtLjU2NC0uNDFMOCAyLjY5NFoiPjwvcGF0aD48L3N2Zz4=" /></a>
<a href="https://github.com/Xiaokang2022/maliang/issues"><img alt="議題" title="議題" src="https://img.shields.io/github/issues/Xiaokang2022/maliang?label=%e8%ad%b0%e9%a1%8c&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTggOS41YTEuNSAxLjUgMCAxIDAgMC0zIDEuNSAxLjUgMCAwIDAgMCAzWiI+PC9wYXRoPjxwYXRoIGZpbGw9IndoaXRlIiBkPSJNOCAwYTggOCAwIDEgMSAwIDE2QTggOCAwIDAgMSA4IDBaTTEuNSA4YTYuNSA2LjUgMCAxIDAgMTMgMCA2LjUgNi41IDAgMCAwLTEzIDBaIj48L3BhdGg+PC9zdmc+" /></a>
<a href="https://github.com/Xiaokang2022/maliang/pulls"><img alt="拉取請求" title="拉取請求" src="https://img.shields.io/github/issues-pr/Xiaokang2022/maliang?label=%e6%8b%89%e5%8f%96%e8%ab%8b%e6%b1%82&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTEuNSAzLjI1YTIuMjUgMi4yNSAwIDEgMSAzIDIuMTIydjUuMjU2YTIuMjUxIDIuMjUxIDAgMSAxLTEuNSAwVjUuMzcyQTIuMjUgMi4yNSAwIDAgMSAxLjUgMy4yNVptNS42NzctLjE3N0w5LjU3My42NzdBLjI1LjI1IDAgMCAxIDEwIC44NTRWMi41aDFBMi41IDIuNSAwIDAgMSAxMy41IDV2NS42MjhhMi4yNTEgMi4yNTEgMCAxIDEtMS41IDBWNWExIDEgMCAwIDAtMS0xaC0xdjEuNjQ2YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0w3LjE3NyAzLjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0Wk0zLjc1IDIuNWEuNzUuNzUgMCAxIDAgMCAxLjUuNzUuNzUgMCAwIDAgMC0xLjVabTAgOS41YS43NS43NSAwIDEgMCAwIDEuNS43NS43NSAwIDAgMCAwLTEuNVptOC4yNS43NWEuNzUuNzUgMCAxIDAgMS41IDAgLjc1Ljc1IDAgMCAwLTEuNSAwWiI+PC9wYXRoPjwvc3ZnPg==" /></a>
<a href="https://github.com/Xiaokang2022/maliang/discussions"><img alt="討論" title="討論" src="https://img.shields.io/github/discussions/Xiaokang2022/maliang?label=%e8%a8%8e%e8%ab%96&logo=data:image/svg+xml;charset=utf-8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij48cGF0aCBmaWxsPSJ3aGl0ZSIgZD0iTTEuNzUgMWg4LjVjLjk2NiAwIDEuNzUuNzg0IDEuNzUgMS43NXY1LjVBMS43NSAxLjc1IDAgMCAxIDEwLjI1IDEwSDcuMDYxbC0yLjU3NCAyLjU3M0ExLjQ1OCAxLjQ1OCAwIDAgMSAyIDExLjU0M1YxMGgtLjI1QTEuNzUgMS43NSAwIDAgMSAwIDguMjV2LTUuNUMwIDEuNzg0Ljc4NCAxIDEuNzUgMVpNMS41IDIuNzV2NS41YzAgLjEzOC4xMTIuMjUuMjUuMjVoMWEuNzUuNzUgMCAwIDEgLjc1Ljc1djIuMTlsMi43Mi0yLjcyYS43NDkuNzQ5IDAgMCAxIC41My0uMjJoMy41YS4yNS4yNSAwIDAgMCAuMjUtLjI1di01LjVhLjI1LjI1IDAgMCAwLS4yNS0uMjVoLTguNWEuMjUuMjUgMCAwIDAtLjI1LjI1Wm0xMyAyYS4yNS4yNSAwIDAgMC0uMjUtLjI1aC0uNWEuNzUuNzUgMCAwIDEgMC0xLjVoLjVjLjk2NiAwIDEuNzUuNzg0IDEuNzUgMS43NXY1LjVBMS43NSAxLjc1IDAgMCAxIDE0LjI1IDEySDE0djEuNTQzYTEuNDU4IDEuNDU4IDAgMCAxLTIuNDg3IDEuMDNMOS4yMiAxMi4yOGEuNzQ5Ljc0OSAwIDAgMSAuMzI2LTEuMjc1Ljc0OS43NDkgMCAwIDEgLjczNC4yMTVsMi4yMiAyLjIydi0yLjE5YS43NS43NSAwIDAgMSAuNzUtLjc1aDFhLjI1LjI1IDAgMCAwIC4yNS0uMjVaIj48L3BhdGg+PC9zdmc+" /></a>
</p>

<p align="center">
<a href="https://github.com/Xiaokang2022/maliang/pulse"><img src="https://repobeats.axiom.co/api/embed/b4832e0ac90defe97c7e11e0c9e926793ec7135c.svg" /></a>
</p>

<p align="center">
    <a href="https://star-history.dera.page/#Xiaokang2022/maliang&Date">
        <picture>
            <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=Xiaokang2022/maliang&type=Date&theme=dark" />
            <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=Xiaokang2022/maliang&type=Date" />
            <img src="https://star-history.dera.page/svg?repos=Xiaokang2022/maliang&type=Date" />
        </picture>
    </a>
</p>

## 📦 安裝

要安裝該包，你的 Python 版本必須 **`>=3.10`**。用以下命令進行安裝：

```shell
pip install maliang
```

### 🛠️ 依賴包

下面是該項目唯一必須需要的依賴包：

* [`typing-extensions`](https://github.com/python/typing_extensions): 提供額外的類型提示

### 🎨 可選包

下面的包都是可選的，不安裝也能讓該項目正常運行，但安裝它們可以爲你提供更多的功能：

* [`darkdetect`](https://github.com/albertosottile/darkdetect): 提供操作系統主題檢測
* [`pillow`](https://github.com/python-pillow/Pillow): 提供更多類型圖片的使用及優化圖片縮放速度
* [`pywinstyles`](https://github.com/Akascape/py-window-styles): 提供一些 Windows 系統的窗口效果
* [`hPyT`](https://github.com/Zingzy/hPyT): 提供更多 Windows 系統窗口的配置選項
* [`win32material`](https://github.com/littlewhitecloud/win32material): 提供更多 Windows 系統窗口的配置選項

**推薦**，這些包都應該安裝，用以下命令可以安裝全部的可選包：

```shell
pip install maliang[opt]
```

### 🧩 擴展包

除了基礎功能之外，我們還提供一些擴展包來實現某些特定的功能。目前已有的官方擴展包如下：

* [`maliang-mpl`](https://github.com/Xiaokang2022/maliang-mpl): 提供 `matplotlib` 包的相關支持
* [`maliang-media`](https://github.com/Xiaokang2022/maliang-media): 提供媒體文件的相關支持
* [`maliang-three`](https://github.com/Xiaokang2022/maliang-three): 提供簡單 3D 繪圖的相關支持
* [`maliang-table`](https://github.com/Xiaokang2022/maliang-table): 提供表格控制項的相關支持

用以下命令可以安裝全部的官方擴展包：

```shell
pip install maliang[ext]
```

此外，你還可以在 [這裡](https://xiaokang2022.github.io/maliang/t%26d/third-party/) 找到所有已被我們收集到的第三方擴展包。

> [!WARNING]  
> 上面提到的包並不包含在本專案的原始程式碼中，如果你使用了它們並想要再分發，請遵循它們的開源協定！

## 👀 更多

### ℹ️ 關於

本專案的徽標取自開源專案：[`fluentui-emoji`](https://github.com/microsoft/fluentui-emoji)，名稱取自中國童話故事：[*《神筆馬良》*](https://baike.baidu.com/item/%E7%A5%9E%E7%AC%94%E9%A9%AC%E8%89%AF/14821387)

### 🖼️ 畫廊

下面是一些可以用該項目實現的演示，它們可能是用該專案的最新版本構建的，也可能是用舊版構建的，但無論怎樣，它們的代碼都可以在演示存儲庫 [`maliang-demos`](https://github.com/Xiaokang2022/maliang-demos) 中找到！

> [!TIP]  
> 請點擊 **“展開”** 來查看畫廊

<details><summary><b>展開</b></summary>

![preview_1](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo9-1.png?raw=true)

![preview_2](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo9-2.png?raw=true)

![preview_3](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo9-3.png?raw=true)

![preview_4](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo9-4.png?raw=true)

![preview_5](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo0-1.png?raw=true)

![preview_6](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo0-2.png?raw=true)

![preview_7](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo1-1.png?raw=true)

![preview_8](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo1-2.png?raw=true)

![preview_9](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo2.png?raw=true)

![preview_10](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo3.png?raw=true)

![preview_11](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo4-1.png?raw=true)

![preview_12](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo4-2.png?raw=true)

![preview_13](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo5-1.png?raw=true)

![preview_14](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo5-2.png?raw=true)

![preview_15](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo6-1.png?raw=true)

![preview_16](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo7-1.png?raw=true)

![preview_17](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo7-2.png?raw=true)

![preview_18](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo8-1.png?raw=true)

![preview_19](https://github.com/Xiaokang2022/maliang-demos/blob/main/preview/demo10-1.png?raw=true)

![project_1](https://github.com/Xiaokang2022/Intelligent-Magic-Cube/blob/main/preview.png?raw=true)

![project_2](https://github.com/Xiaokang2022/Chess/blob/master/preview.png?raw=true)

![project_3](https://github.com/Xiaokang2022/Super-Gobang/blob/main/preview.png?raw=true)

![project_4](https://github.com/Xiaokang2022/TodoList/blob/master/preview.png?raw=true)

</details>

### 🔗 連結

這裡是一些可能對您有幫助的連結：

* 📑 項目許可: [*MIT License*](LICENSE.txt)
* 📘 更新日誌: [*CHANGELOG.md*](CHANGELOG.md)
* 📕 安全策略: [*SECURITY.md*](SECURITY.md)
* 📗 貢獻指南: [*CONTRIBUTING.md*](CONTRIBUTING.md)
* 📙 行爲準則: [*CODE_OF_CONDUCT.md*](CODE_OF_CONDUCT.md)
* 📚 教程和文檔: [Tutorials & Documents](https://xiaokang2022.github.io/maliang-docs/) ([Mirror](https://maliang-docs.netlify.app/))
* ❤️ 贊助我們: [Sponsor](https://xiaokang2022.github.io/maliang/Sponsor/)
* 🚀 存儲庫鏡像源:
[Gitee](https://gitee.com/Xiaokang2022/maliang),
[GitCode](https://gitcode.com/Xiaokang2022/maliang)

### 😉 貢獻者

非常感謝下面這些人的貢獻：

[![貢獻者](https://contrib.rocks/image?repo=Xiaokang2022/maliang)](https://github.com/Xiaokang2022/maliang/graphs/contributors)