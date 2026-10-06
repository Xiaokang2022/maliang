# Changelog / 更新日志

> [!TIP]  
> This changelog has the following 7 types of updates, each of which is represented by 7 different colors  
> 此更新日志有以下 7 种类型的更新内容，分别用 7 种不同颜色来表示
>
> * 🟢 **Added / 新增**
> * 🔴 **Removed / 移除**
> * 🟡 **Changed / 变更**
> * 🔵 **Optimized / 优化**
> * 🟣 **Fixed / 修复**
> * 🟠 **Deprecated / 弃用**
> * 🟤 **Refactored / 重构**

## 🔖 `3.2.0`

🕓 *Release Date / 发布日期 : 2026-10-06*

🟢 **Added / 新增**

* Widgets now reset their `hover`/`active` state when the mouse leaves the canvas  
控件在鼠标离开画布时会自动重置其 `hover`/`active` 状态

🟡 **Changed / 变更**

* The minimum required Python version is changed from 3.10 to 3.11, and Python 3.15 is now supported  
最低 Python 版本要求由 3.10 变更为 3.11，并且现已支持 Python 3.15  
Issue: #153

🔵 **Optimized / 优化**

* Avoid unnecessary zooming of the canvas when only its position changes  
避免画布在仅位置变化时进行不必要的缩放

🟣 **Fixed / 修复**

* Fixed a bug where the coordinate passing of the widget `Line` was not supported on some Tcl/Tk versions  
修复了控件 `Line` 的坐标传递在部分 Tcl/Tk 版本上不受支持的 bug  
Issue: #154

* Fixed a bug where `PhotoImage` parsed the image data incorrectly when PIL was not installed on Tk 9.0+  
修复了 Tk 9.0+ 且未安装 PIL 时 `PhotoImage` 解析图像数据错误的 bug

🟤 **Refactored / 重构**

* Adjust the source code directory structure to the `src` layout  
调整源代码目录结构为 `src` 布局

* Improve the unit tests and the CI workflows, and fix the occasional crash and the failure of the window position assertions on the macOS runner  
完善单元测试与 CI 工作流，并修复 macOS 运行器上偶现的崩溃和窗口位置断言失败的问题  
Issue: #153

## 🔖 `3.1.5`

🕓 *Release Date / 发布日期 : 2025-09-27*

🟢 **Added / 新增**

* Add a new extension package: [`maliang-table`](https://github.com/Xiaokang2022/maliang-table)  
新增了一个扩展包：[`maliang-table`](https://github.com/Xiaokang2022/maliang-table)

🟣 **Fixed / 修复**

* Fix typos in the parameters of some functions in submodules `color.rgb` and `color.hsl`  
修复子模块 `color.rgb` 和 `color.hsl` 中一些函数的参数的错别字

* Fixed a typo in the instance variable `initial_image` of the class `virtual.Image`  
修复了类 `virtual.Image` 的实例变量 `initial_image` 的错别字

🟤 **Refactored / 重构**

* Improve code for readability and maintainability  
改善代码，提高可读性和可维护性

## 🔖 `3.1.4`

🕓 *Release Date / 发布日期 : 2025-08-02*

🔵 **Optimized / 优化**

* Share the style data of the object `Style`, reducing memory consumption and speeding up widget building  
共享对象 `Style` 的样式数据，减少内存消耗并提升控件构建速度  
Issue: #129

🟤 **Refactored / 重构**

* Improve code for readability and maintainability  
改善代码，提高可读性和可维护性

## 🔖 `3.1.3`

🕓 *Release Date / 发布日期 : 2025-06-29*

🟢 **Added / 新增**

* Added method `exists` to all widgets  
为所有控件新增了方法 `exists`  
Issue: #125

🟣 **Fixed / 修复**

* Fixed a bug where the value of the widget `SpinBox` could cause unexpected results when the value was large  
修复了控件 `SpinBox` 在值比较大时会导致意外结果的 bug  
Issue: #122

* Fixed a bug where the widget `Canvas` would be updated unexpectedly  
修复了控件 `Canvas` 会被意外更新的 bug  
Issue: #124

🔵 **Optimized / 优化**

* Reduced the amount of memory used by the widget after calling the `destroy` method  
降低了控件在调用方法 `destroy` 后所占用的内存量

## 🔖 `3.1.2`

🕓 *Release Date / 发布日期 : 2025-06-17*

🟢 **Added / 新增**

* Some widgets have added the ability to automatically and dynamically update the size  
一些控件可以自动地动态更新大小  
Issue: #119 (*Partially Resolved*)

* Added parameter `font` to function `get_text_size`  
函数 `get_text_size` 增加了参数 `font`

🟣 **Fixed / 修复**

* Fixed a bug where the widgets `Text` and `Image` would unexpectedly modify the mouse style (`3.1.1` regression)  
修复了控件 `Text` 和 `Image` 会意外修改鼠标样式的 bug（`3.1.1` 回归）

## 🔖 `3.1.1`

🕓 *Release Date / 发布日期 : 2025-06-16*

🟢 **Added / 新增**

* Keyboard <kbd>Tab</kbd> and <kbd>Shift</kbd>+<kbd>Tab</kbd> are supported to manipulate widgets, and <kbd>Enter</kbd> is used to simulate clicking on a widget with focus  
支持通过键盘 <kbd>Tab</kbd> 和 <kbd>Shift</kbd>+<kbd>Tab</kbd> 来操控控件，并通过 <kbd>Enter</kbd> 来模拟点击具有焦点的控件  
Issue: #70

* Add method `region` to class `virtual.Widget` to get the display area of the current widget  
类 `virtual.Widget` 新增方法 `region` 来获取当前控件的显示区域

* Add method `center` to class `virtual.Widget` to get the center coordinates of the display area of the current widget  
类 `virtual.Widget` 新增方法 `center` 来获取当前控件的显示区域的中心坐标

* Add parameter `wrap_length` to function `utility.get_text_size`  
函数 `utility.get_text_size` 新增参数 `wrap_length`

* Improve some type hints  
完善部分类型提示

🟣 **Fixed / 修复**

* Fix a bug where the widget `Tooltip` did not work for the widget `Text` and `Image`  
修复控件 `Tooltip` 无法对控件 `Text` 和 `Image` 生效的 bug  
Issue: #77

* Fix some incorrect type hints  
修复部分错误的类型提示

## 🔖 `3.1.0`

🕓 *Release Date / 发布日期 : 2025-06-10*

🟢 **Added / 新增**

* Some animation classes can take effect on multiple objects at the same time  
一些动画类可以对多个对象同时生效  
Issue: #106

* Add method `lift` to class `virtual.Widget`  
类 `virtual.Widget` 新增方法 `lift`  
Issue: #116

* Add the ability for widget `Text` to set the length of character wrapping  
给控件 `Text` 增加能够设置自动换行的字符长度的功能  
Issue: #97

* Some functionalities for operating widgets using the keyboard have been implemented  
实现了一些使用键盘操作控件的功能  
Issue: #70 (*Partially Resolved*)

🟣 **Fixed / 修复**

* Fix a bug that generating unexpected warnings  
修复了生成非预期警告的 bug  
Issue: #117

* Fix an exception caused by inconsistent state parameters when updating nested widgets  
修复更新嵌套控件时状态参数不一致导致的异常  
Issue: #113

* Fix a wrong type hint  
修复一个错误的类型提示

🔵 **Optimized / 优化**

* Reduce memory usage and improve responsiveness  
降低内存使用量并提高事件响应速度

## 🔖 `3.0.5`

🕓 *Release Date / 发布日期 : 2025-05-10*

🔵 **Optimized / 优化**

* Improve the performance of functions `color.rgb.blend` and `color.hsl.blend`  
提高了函数 `color.rgb.blend` 和 `color.hsl.blend` 的性能

* Optimize part of the import, increasing the import speed  
优化部分导入，提高导入速度

## 🔖 `3.0.4`

🕓 *Release Date / 发布日期 : 2025-04-09*

🟣 **Fixed / 修复**

* Fix a bug where the cursor still flashes when widget `InputBox` is disabled  
修复了控件 `InputBox` 在禁用后光标仍然闪烁的 bug  
Issue: #92

* Fix an issue where the widget `InputBox` is freezing in some cases when entering text  
修复了控件 `InputBox` 在高度设置比较大的时候，限制文本长度将导致程序卡死的 bug  
Issue: #100

* Fix a bug where the text of widget `InputBox` will extend beyond the text box  
修复了控件 `InputBox` 的文本会超出文本框边界的 bug  
Issue: #101

* Partially fix a bug that cause the window to flicker when it started  
部分修复了窗口在启动时会闪烁的 bug  
Issue: #102

## 🔖 `3.0.3`

🕓 *Release Date / 发布日期 : 2025-03-20*

🟢 **Added / 新增**

* Add a read-only property `children` to virtual widget class `Widget` to access its child widgets  
增加了一个只读的属性 `children` 给虚拟控件类 `Widget` 来访问它的子控件

* Add a basic class `TkFileChooser` to accommodate module `tkinter`  
增加了一个基础的类 `TkFileChooser` 来适配模块 `tkinter`  
Pull Request: #82 Contributor: @3190

🟣 **Fixed / 修复**

* Fix the bug that the `ComboBox` widget can not close the selection box without selecting it after clicking to open it  
修复了控件 `ComboBox` 在点击打开选项列表后不选中选择框就无法关闭的 bug  
Issue: #87 Pull Request: #89 Contributor: @shu-shu-1

* Fix some typos  
修正了一些错字

## 🔖 `3.0.2`

🕓 *Release Date / 发布日期 : 2025-03-05*

🟣 **Fixed / 修复**

* `animation.animations.MoveTkWidget` will produce an incorrect displacement for `tkinter` widgets with a parameter `anchor` that is not equal to `"nw"`  
`animation.animations.MoveTkWidget` 会对参数 `anchor` 不等于 `"nw"` 的 `tkinter` 控件产生错误的位移  
Issue: #81

## 🔖 `3.0.1`

🕓 *Release Date / 发布日期 : 2025-02-26*

🟢 **Added / 新增**

* Add initialization parameter `ignore` to the widget `InputBox` to ignore partially inserted characters  
控件 `InputBox` 新增初始化参数 `ignore` 来忽略部分插入的字符  
Issue: #78

🟣 **Fixed / 修复**

* Fix a bug where pasting multiple lines of text in the widget `InputBox` would cause the text to overflow  
修复了在控件 `InputBox` 中粘贴多行文本会导致文本溢出的 bug  
Issue: #78

* Fix a type hint error  
修复了一个类型提示错误

* Fixed an issue where the metadata information of the distributed package was incorrect  
修复了分发包的元数据信息存在错误的问题

## 🔖 `3.0.0`

🕓 *Release Date / 发布日期 : 2025-01-26*

🟢 **Added / 新增**

* Add methods `get` and `set` to some widgets  
给一些控件增加方法 `get` 和 `set`

* A new parameter `auto_detect` has been added to the method `bind` of the widgets to determine whether to automatically check the location of the decision  
新参数 `auto_detect` 已添加到控件的方法 `bind` 中，以确定是否自动检查决策的位置

* Add methods `modified` and `transparent` to class `Tk`  
给类 `Tk` 增加了方法 `modified` 和 `transparent`  
Pull Request: #65 Contributor: @CodeCrafter-TL

🟣 **Fixed / 修复**

* Fix a bug where calling function `apply_theme` in non-Windows systems caused unnecessary warnings  
修复了在非 Windows 系统中调用函数 `apply_theme` 导致不必要警告的错误

* Fix a bug where the optional package `darkdetect` can not be imported on some Windows platforms  
修复了在某些 Windows 平台无法导入包 `darkdetect` 的问题

* Fix a bug where the widgets `ComboBox` and `OptionButton` can be obscured by other widgets  
修复了控件 `ComboBox` 和 `OptionButton` 可能被其他控件遮挡的问题

🟡 **Changed / 变更**

* Improve the color style of the widget `SegmentedButton` and its related widgets  
改进控件 `SegmentedButton` 及其相关控件的颜色样式

🟤 **Refactored / 重构**

* Change some code written with module `platform` to module `sys` to provide better type hints  
将部分用模块 `platform` 写的代码改用模块 `sys` 重写来提供更好的类型提示

## 🔖 `3.0.0rc6`

🕓 *Release Date / 发布日期 : 2025-01-13*

🟢 **Added / 新增**

* Add disabled mouse cursor styles  
新增控件禁用状态时的鼠标样式

* Add function `create_smoke` to create translucent rectangular areas  
新增函数 `create_smoke` 来创建半透明的矩形区域

* Add widget virtual composition class `virtual.Style` to control the style of a widget  
新增控件虚拟组成类 `virtual.Style` 来控制一个控件的样式

* Add a new submodule `standard.styles`  
新增模块 `standard.styles`

* Add method `set` to class `Style` to quickly modify the style of the widget  
类 `Style` 新增方法 `set` 来快速修改控件样式

* Add a new experimental image element `Smoke`  
增加了一个实验性的图片元素 `Smoke`

* Add an experimental parameter `zoom_all_items` to `Canvas`  
增加了一个实验性参数 `zoom_all_items` 给 `Canvas`

* Add method `skip` to class `Animation` to skip some loops  
增加了方法 `skip` 来跳过类 `Animation` 的一些循环

* Add the ability to use the with statement to the containers  
容器控件现在可以使用 with 语句来临时创建并删除了

* Add a new theme `"acrylic2"` to function `apply_theme`  
函数 `apply_theme` 新增配置选项 `"acrylic2"`

* `Canvas` now supports automatic get the default master  
`Canvas` 现在可以自动获取默认的父控件了

* Now can specify the style to modify a theme  
现在修改单个控件的主题时可以指定某个主题了  

🟣 **Fixed / 修复**

* Fix a bug where classes `Tk` and `Toplevel` may not work on Linux platforms  
修复了类 `Tk` 和类 `Toplevel` 可能无法在 Linux 平台上无法运行的 bug

* Fix class `animations.MoveWindow` may report an error when passing in certain parameters  
修复了类 `animations.MoveWindow` 传入某些参数时可能报错的 bug

* Fix a bug where widgets would flicker unexpectedly when changing colors  
修复了修改控件颜色时会意外闪烁的 bug

* Fix a bug where the animation did not completely stop when the `Element` was destroyed  
修复了元素删除时其动画不会停止的 bug

* Fix a bug where widgets don't scale their nested widgets in some cases  
修复了控件在某些情况下不会缩放其嵌套控件的 bug

* Fix a bug where the coordinates of the Image element were incorrectly detected  
修复了元素 `Image` 的坐标被错误检测的 bug

* Fix a bug where the registered theme processing event was not deleted when the root window was deleted  
修复了当根窗口被删除时其注册的样式处理事件没有被删除的 bug

* Fixed a bug where the function `get_text_size` return value is inaccurate  
修复了函数 `get_text_size` 返回值在某些情况下不不准确的 bug

* Fix a bug where deleting a `Canvas` would not automatically delete the `Widget`, resulting in the widget's animation not automatically terminating  
修复了删除 `Canvas` 不会自动删除 `Widget` 的错误，从而导致 Widget 的动画不会自动终止

* Fix a bug where style switch of `containers.Tk` does not automatically take effect on child windows  
修复了类 `containers.Tk` 的样式切换时不会应用于子窗口的 bug

* Fix a bug where some of methods of containers.Tk do not work on non-Windows systems  
修复 `containers.Tk` 的部分方法无法在非 Windows 平台上生效的 bug

* Fix the bug that function `load_font` can not take effect in some cases under the Linux platform  
修复了某些情况下函数 `load_font` 无法在 Linux 平台上生效的 bug

* Fix a bug where function `apply_theme` do not take effect when the parameter is `"mica"`  
修复了函数 `apply_theme` 在 Windows 平台上输入参数 `"mica"` 时无效的 bug

* Fix a bug where the icon of the window can not be set on the Linux platform  
修复了在 Linux 平台下窗口的图标无法设置的 bug

* A new method `group` has been added to the `RadioBox` widget to combine other radio widgets  
控件 `RadioBox` 新增方法 `group` 来绑定其它单选框控件

* Fix a bug where an error is reported when auto-calculating styles in the disabled state due to the inability to process empty strings  
修复了控件在禁用状态自动计算状态时因传入空字符串而报错的 bug

* Fix a bug where the selected part of the text box has a border  
修复了文本框在选中文本时有一个边框的 bug

* Fix a bug where Canvas initialization failed in some cases  
修复了某些情况下画布在初始化时会失败的 bug

* Fix a bug where the window size would change when the title bar is hidden  
修复了隐藏窗口标题栏时窗口大小会改变的 bug

* Fix a bug where an error is reported when disabling widgets with `Image` elements  
修复了禁用含图片元素的控件时会报错的 bug

* Fix a bug where the default font on macOS platform is not recognized by `matplotlib`  
修复了在 macOS 平台上的默认字体无法被 `matplotlib` 包识别的 bug

🔵 **Optimized / 优化**

* Change some `update_idletasks` to `update` to improve speed performance  
修改了部分 `update_idletasks` 为 `update` 来提升性能

🔴 **Removed / 移除**

* Removed class `Frame` and its styles  
移除了类 `Frame` 及其样式

* Removed the **original** subpackage `theme`  
移除了**原来的**子包 `theme`

🟤 **Refactored / 重构**

* Refactor subpackage `color`  
重构了子包 `color`

* Refactor submodule `animation`  
重构了子包 `animation`

* Refactor submodule `configs`  
重构了子模块 `configs`

* Refactor submodule `containers`  
重构了子模块 `containers`

* Refactor style control mechanism  
重构了样式控制机制

* Refactor subpackage `style` and renamed to `theme`  
重构子包 `style` 并重命名为 `theme`

* Refactor widget `RadioButton` and renamed to `RadioBox`  
重构控件 `RadioButton` 并重命名为 `RadioBox`

* Refactor widget `CheckButton` and renamed to `CheckBox`  
重构控件 `CheckButton` 并重命名为 `CheckBox`

## 🔖 `3.0.0rc5`

🕓 *Release Date / 发布日期 : 2024-12-19*

🟢 **Added / 新增**

* A new property `is_active` has been added to the class `Animation` to represent the state of the animation  
类 `Animation` 新增了一个属性 `is_active` 表征动画的状态

* Class `virtual.Widget` has a new method `is_nested` to determine if the widget is nested  
类 `virtual.Widget` 新增了一个方法 `is_nested` 来判断该控件是否为嵌套控件

* Added the global configuration option `enable_animation` to enable the color gradient animation of the widget  
新增全局配置选项 `enable_animation` 来设置控件颜色渐变动画是否启用

* New widget: `OptionButton`  
新增控件：选项按钮（`OptionButton`）

* New widget: `ComboBox`  
新增控件：下拉框（`ComboBox`）

* New widget: `Spinner`  
新增控件：旋转条（`Spinner`）

* Classes `Tk` and `Toplevel` added the parameter `icon` to set the icon of the window  
类 `Tk` 和 `Toplevel` 新增了参数 `icon` 来设置窗口的图标

* Class `texts.SingleLineText` added a new parameter `limit_width` to show the maximum width of the text display  
类 `texts.SingleLineText` 新增了参数 `limit_width` 来显示文本显示的最大宽度

🟣 **Fixed / 修复**

* Fixed a bug where the parameter `end` of the class `Animation` was called with an error causing the animation to terminate  
修复了类 `Animation` 的参数 `end` 被调用时产生错误导致动画终止的 bug

* Fixed a bug where the default root window could not be obtained in some cases  
修复了某些情况下无法获取默认根窗口的 bug

* Fixed a bug where the content of the class `virtual.Text` could not be changed when the parameter `limit` was negative  
修复了类 `virtual.Text` 的参数 `limit` 为负数时，内容无法更改的 bug

* Fixed a bug where the method `detect` for nested widgets had inaccurate results  
修复了嵌套控件的方法 `detect` 结果不准确的 bug

* Fixed a bug where the method `update` of nested widgets sometimes did not take effect  
修复了嵌套控件的方法 `update` 有时不生效的 bug

* Fixed a bug where nested widgets could not be disabled  
修复了嵌套控件无法禁用的 bug

* Fixed a bug where the placeholder character of the widget `InputBox` would sometimes be displayed at the same time as the text content  
修复了控件 `InputBox` 的占位字符有时会和文本内容同时显示的 bug

* Fixed a bug where the parameter `through` of the widget `SpinBox` was passed incorrectly  
修复了控件 `SpinBox` 的参数 `through` 传递不正确的 bug

* Fixed a bug where the `anchor` parameter of the widget `SpinBox` did not take effect  
修复了控件 `SpinBox` 的参数 `anchor` 不生效的 bug

* Fixed a bug where the text of the widget `SpinBox` was obscured by the numeric adjustment button  
修复了控件 `SpinBox` 的文本被数值调节按钮遮挡的 bug

🔵 **Optimized / 优化**

* Invisible widgets are no longer handled by the event handling mechanism  
不可见的控件现在不会被事件处理机制处理了

## 🔖 `3.0.0rc4`

🕓 *Release Date / 发布日期 : 2024-11-17*

🟢 **Added / 新增**

* The fine-grained scaling of widgets has been improved, and the position and size of the widgets can now be scaled separately by the new parameters of the method  `zoom` of widgets, as described in the documentation  
提高了控件缩放的细粒度，现在可以通过控件的 `zoom` 方法的新参数分别缩放控件的位置和大小，具体参数见文档

* Added parameters to the widget `SpinBox` to control the size of each time the value is modified and the format in which the value is displayed, see the documentation  
控件 `SpinBox` 新增参数来控制每次修改值时的大小以及值显示的格式，具体参数见文档

* The widget `InputBox` adds the ability of key <kbd>Del</kbd> to delete text  
控件 `InputBox` 新增 <kbd>Del</kbd> 键的功能来删除文本

🔵 **Optimized / 优化**

* The function `controllers.controller_generator` now warn when a parameter passed to function is inappropriate  
现在传递给函数 `controllers.controller_generator` 的参数不合适时会发出警告

* Now use the descriptor to get the default root window dynamically  
现在使用描述器来动态获取默认的根窗口

* The time error of the animation has been reduced  
减小了动画的时间误差

* Improved type hints  
改善类型提示

* Improved code style  
改善代码风格

🟣 **Fixed / 修复**

* Fixed a bug where the widget `SegmentedButton` would show the wrong position when using the `anchor` parameter  
修复了控件 `SegmentedButton` 使用参数 `anchor` 时会显示错位的 bug

* Fixed a bug where nested widgets could not be destroyed gracefully  
修复了嵌套控件无法正常删除的 bug

* Fixed a bug where it was not possible to delete a widget with a lower creation order widget  
修复了无法用创建顺序靠后的控件去删除创建顺序靠前的控件的 bug

* Fixed a bug where the widget `InputBox` could produce an error when deleting text  
修复了控件 `InputBox` 在删除文本时可能产生错误的 bug

* Fixed a bug where the widget `InputBox` could produce an error when using the experimental Select All feature  
修复了控件 `InputBox` 在使用实验性全选功能时可能产生错误的 bug

* Fixed a bug where the widget `SpinBox` would produce an error when using the built-in adjustment value feature  
修复了控件 `SpinBox` 在使用自带的调节值功能时会产生错误的 bug

🟤 **Refactored / 重构**

* Refactored submodule `core.constants` and renamed to `core.configs`  
重构子模块 `core.constants` 并重命名为 `core.configs`

* Refactoring the entire event handling mechanism to now bind and handle events almost exactly like native `tkinter`  
重构整个事件处理机制，现在几乎可以完全像原生 `tkinter` 那样绑定和处理事件了

🔴 **Removed / 移除**

* Removed useless submodule `standard._auxiliary`  
移除了无用子模块 `standard._auxiliary`

* The function `toolbox.set_mouse_position` has been removed and will be moved to a different project in the future  
移除了函数 `toolbox.set_mouse_position`，后续会将其移动到其它项目中

## 🔖 `3.0.0rc3`

🕓 *Release Date / 发布日期 : 2024-10-24*

🟢 **Added / 新增**

* New widget, tooltip (`Tooltip`)  
新增控件，工具提示框（`Tooltip`）

* All widgets have a new initialization parameter, `anchor`, to specify the anchor location  
所有控件都新增了初始化参数 `anchor` 来指定锚点位置

* New methods `bind`, `unbind`, `bind_on_update` and `unbind_on_update` for all widgets  
所有控件新增方法 `bind`、`unbind`、`bind_on_update` 和 `unbind_on_update`

🔵 **Optimized / 优化**

* The function `get_text_size` now can calculate multiple lines of text correctly  
函数 `get_text_size` 可以正确计算多行文本了

* The function `get_text_size` added the parameter `master`, which can improve performance when used  
函数 `get_text_size` 增加了参数 `master`，当使用该参数时可以提升性能

* Some code outputs an error message in stderr when it causes a problem, rather than no output at all (e.g., when a function in a theme switching thread throws an error)  
部分代码产生问题时会在标准错误输出中输出错信息，而不是不产生任何输出（如主题切换线程中的函数引发错误时）

🟣 **Fixed / 修复**

* Fixed a bug where setting the style identity to a class would cause an error  
修复了样式标识设置为类会导致错误的 bug

* Fixed a bug where the size would not be calculated correctly when the font was italicized or bold, causing the widget to display incorrectly  
修复了字体为斜体或者粗体时，大小不会被正确计算，导致控件显示不正确的 bug

* Fixed a bug that font loading may fail in some cases under Windows  
修复 Windows 系统下，部分情况下字体加载可能失败的 bug

* Fixed a bug where the results of the functions `rgb.contrast` and `hsl.contrast` were incorrect  
修复了函数 `rgb.contrast` 和 `hsl.contrast` 的结果不正确的 bug

🟡 **Changed / 变更**

* Parameter names for some functions have been changed (the original name violates lint)  
部分函数的参数名称发生的改变（原名称违背了 lint）

🔴 **Removed / 移除**

* Removed some of the redundant parameters of the class `Text`  
移除了类 `Text` 的部分冗余参数

* Removed unused classes and functions  
移除了未使用的类和函数

## 🔖 `3.0.0rc2`

🕓 *Release Date / 发布日期 : 2024-09-16*

🟢 **Added / 新增**

* Implemented the ability to play videos, see <https://github.com/Xiaokang2022/tkintertools-media>  
实现了播放视频的功能，见：<https://github.com/Xiaokang2022/tkintertools-media>

* Added a parameter called `anchor` to `Image`  
`Image` 增加了一个名为 `anchor` 的参数

* Added some aliases  
增加了一些别名

* Added method `resize` to class `PhotoImage`  
类 `PhotoImage` 增加了方法 `resize`

* Added a `callback` parameter to the `set` method of the relevant widget to control whether the callback function is also called when the method is called  
相关控件的 `set` 方法增加了参数 `callback` 来控制当该方法被调用时回调函数是否被调用

🟡 **Changed / 变更**

* Changed default value of parameter `anchor` of `Text`  
修改了 `Text` 的参数 `anchor` 的默认值

* Changed the API of `SegmentedButton`  
修改了 `SegmentedButton` 的 API

🟣 **Fixed / 修复**

* Fixed a bug where widget `SegmentedButton` had incorrect function bindings  
修复 `SegmentedButton` 的函数绑定不正确的 bug

* Fixed a bug where disabling styles would not recalculate  
修复了禁用样式不会重复计算的 bug

* Fixed a bug where fonts could not be loaded on Linux OS  
修复了字体加载函数在 Linux 操作系统上不生效的 bug

* Fixed a bug where the return value of method `alpha` of class `Tk` was incorrect  
修复 `Tk` 的方法 `alpha` 的返回值不正确的 bug

* Fixed a bug where some methods of class `Tk` were called and the window style was lost  
修复了类 `Tk` 的某些方法被调用时会导致窗口丢失样式的 bug

* Fixed some incorrect type hints and missing parameters  
修复了一些不正确的类型提示和丢失的参数

* Fixed a bug where the widget `Image` must be forced to initialize the image parameter, otherwise an error may be reported  
修复了控件 `Image` 必须强制指定图片，否则会报错的 bug

🔵 **Optimized / 优化**

* Optimized method `shutdown` of class `Tk`  
优化了类 `Tk` 的方法 `shutdown`

* The font loading function has been optimized so that parameter `private` has a certain effect on Linux systems  
字体加载函数被优化使得其 `private` 参数能在 Linux 操作系统上产生一定的作用

* Class `MoveTkWidget` has been optimized to prevent it from getting widget data that is not up to date  
类 `MoveTkWidget` 被优化以防止其获取到的控件数据不是最新的

* Improved doc string  
改善了文档字符串

🔴 **Removed / 移除**

* Removed initialization parameter `transient` of class `Toplevel`  
移除了类 `Toplevel` 的初始化参数 `transient`

## 🔖 `3.0.0rc1`

🕓 *Release Date / 发布日期 : 2024-08-08*

🟢 **Added / 新增**

* The widget `Text` added methods `get` and `set` to get and modify its text content  
控件 `Text` 添加了 `get` 和 `set` 方法，用于获取和修改其文本内容

* Added widget `Image`  
添加了控件：`Image`

* Added container widget `Frame` to assist with layout  
添加了容器控件 `Frame` 以协助布局

* The container widget `Canvas` has added the method `clear` to clear everything drawn inside it  
容器控件 `Canvas` 添加了 `clear` 方法，以清除其中绘制的所有内容

* Widgets can now be nested within widgets  
控件现在可以嵌套在控件中了

* The submodule `tools` added a function `get_text_size` to get the size of the text  
子模块 `tools` 添加了一个函数 `get_text_size` 用于获取文本的大小

* Added the incomplete Select All function, which can select all, but due to the imperfection of the function of selecting the text with the mouse, the Select All function cannot select the undisplayed text  
新增了不完整的全选功能，可以全选，但由于鼠标选择文本的功能不完善，导致全选功能无法选择未显示的文本

* `virtual.Widget` has a new method called `detect` to determine the range based on the data of the widget itself  
`virtual.Widget` 新增了一个名为 `detect` 的方法，其根据控件本身的数据确定的范围来进行检测

* Added `HalfRoundedRectangular` shape class  
添加了形状类 `HalfRoundedRectangular`

* Added widget: `ToggleButton`  
添加了控件：`ToggleButton`

* Added widget: `SegmentedButton`  
添加了控件：`SegmentedButton`

* Added widget: `SpinBox`  
添加了控件：`SpinBox`

* The subpackage `standard` added an internal submodule `_auxiliary` to define some auxiliary widgets  
子包 `standard` 添加了一个内部子模块 `_auxiliary` 来定义一些辅助控件

* The `GOLDEN_RATIO` constant has been added  
增加了常量 `GOLDEN_RATIO`

* Added experimental implementations of widgets `OptionButton` and `ComboBox`  
添加了控件 `OptionButton` 和 `ComboBox` 的实验性实现

🔴 **Removed / 移除**

* The code for the `matplotlib` related interface part is separated  
将 `matplotlib` 相关接口部分的代码分离了

* Due to some conflicts, the binding and handling of the mouse double-click event has been removed  
由于存在一些冲突，删除了鼠标双击事件的绑定和处理

🟡 **Changed / 变更**

* Re-change the text defaults of the widget to an empty string  
将控件的文本默认值重新更改为空字符串

* Rename the widgets `Entry` and `Information` to `InputBox` and `Text`, respectively  
将控件 `Entry` 和 `Information` 分别重命名为 `InputBox` 和 `Text`

* The "Feature" suffix has been added to the class names of several `Feature` classes to prevent them from being indistinguishable from the `Widget` class in the error message  
“Feature” 后缀已添加到多个 `Feature` 类的类名中，以防止它们与错误消息中的 `Widget` 类无法区分

🔵 **Optimized / 优化**

* Optimized decision detection for `Oval` and `SemicircularRectangle`  
优化了 `Oval` 和 `SemicircularRectangle` 的检测判定方法

* The `Switch` widget added more animations  
`Switch` 添加了更多动画

* `Shape` scaling has been improved: the scale has been changed from direct scaling to calculating the position to prevent the proportions of some parts from being broken  
改进了 `Shape` 的缩放：缩放已从直接缩放更改为计算位置后缩放，以防止某些部分的比例被破坏

* All widgets that involve text now do not need to be forced to specify the size at initialization, and it automatically calculates the size of text without line breaks  
现在，所有涉及文本的控件都不需要在初始化时强制指定大小，它会自动计算没有换行符的文本的大小

* Optimized the `RoundedRectangle` subclass of the `Shape` class  
优化了 `Shape` 的子类 `RoundedRectangle`

* Improved the docstrings, error messages, and warning messages  
改善了文档字符串、错误消息和警告消息

🟣 **Fixed / 修复**

* Fixed a bug where `IconButton` was missing style files  
修复 `IconButton` 缺少样式文件的 bug

* Fixed a bug where the `Slider` could be activated unexpectedly when disabled  
修复 `Slider` 在禁用时可能会意外激活的 bug

* Fixed a bug where text had no effect on modifying its properties after scaling  
修复了文本在缩放后修改其属性不起作用的 bug

* Fixed a bug where some widgets with default values could repeatedly call the method `set`, causing the widget appearance to be misaligned  
修复了某些具有默认值的控件可能会重复调用方法 `set` 从而导致控件外观错位的 bug

* Fixed a bug where some highly custom widgets would report an error when zooming  
修复了某些高度自定义的控件在缩放时会报错的 bug

🟤 **Refactored / 重构**

* Refactored the `style` subpackage, reformatted the style file, and now supports two ways to import themes. That is, import as a JSON file, or directly import using a Python file  
重构了 `style` 子包，重新格式化了样式文件，现在支持两种导入主题的方式。即使用 JSON 文件导入，或直接使用 Python 文件导入

* Removed the original JSON format style file, and added `theme` subpackage to store the style data as a Python file, so as to solve the bug that the default style file is lost in project packaging  
移除了原有的 JSON 格式样式文件，并添加了 `theme` 子包，将样式数据存储为 Python 件，从而解决了项目打包时默认样式文件丢失的 bug

## 🔖 `3.0.0.beta4`

🕓 *Release Date / 发布日期 : 2024-07-20*

🟢 **Added / 新增**

* The widget `Entry` has a new parameter `placeholder` to display the prompt information  
控件 `Entry` 新增了参数 `placeholder` 来实现提示信息的显示

* Added parameter `show` to the widget `Entry` to mask characters (e.g. password box)  
控件 `Entry` 新增了参数 `show` 来实现字符的掩盖（如密码框）

* The new parameter `align` has been added to the widget `Entry` to achieve a similar effect to the `text-align` of tags in *HTML*, i.e. the left, right, and center layout of the text  
控件 `Entry` 新增了参数 `align` 来实现于 *HTML* 里的标签的 `text-align` 类似的效果，即文本的靠左、靠右和居中布局

* The widget `Entry` has been added to move the text prompt by pressing the left and right keys on the keyboard  
控件 `Entry` 新增了通过按下键盘的左右键来移动文本提示符的功能

* Added text selection to the widget `Entry`  
控件 `Entry` 新增了文本选中的功能

* The widget `Entry` has added shortcuts to copy (<kbd>Ctrl</kbd>+<kbd>C</kbd>), paste (<kbd>Ctrl</kbd>+<kbd>V</kbd>) and cut (<kbd>Ctrl</kbd>+<kbd>X</kbd>)  
控件 `Entry` 新增了快捷键复制（<kbd>Ctrl</kbd>+<kbd>C</kbd>）、粘贴（<kbd>Ctrl</kbd>+<kbd>V</kbd>）和剪切（<kbd>Ctrl</kbd>+<kbd>X</kbd>）的功能

* Added widget slider (`Slider`)  
新增了控件滑动条（`Slider`）

* Added widget icon button (`IconButton`)  
新增了控件图标按钮（`IconButton`）

* Added some missing docstrings  
增加了部分缺失的文档字符串

🟡 **Changed / 变更**

* The color of the widget `Entry` has been changed slightly under Windows 10 to enhance the look  
控件 `Entry` 在 Windows 10 操作系统下的颜色略有改变，以提升观感

* The position of the text of the widget `Entry` in the text box has been slightly corrected to improve the look  
控件 `Entry` 的文本在文本框中的位置被稍微修正了一下，以提升观感

🟣 **Fixed / 修复**

* Fixed a bug where deleting text from the widget `Entry` in some cases would cause the program to loop in an endless loop  
修复了控件 `Entry` 某些情况下删除文本会导致程序死循环的问题

🔵 **Optimized / 优化**

* Improved the readability of some codes  
增强了部分代码的可读性

🔴 **Removed / 移除**

* Widget `Entry` removed the parameters `justify` and `anchor`  
控件 `Entry` 移除了参数 `justify` 和 `anchor`

* Removed the 3D part of the code and related theme files  
移除了 3D 部分代码以及相关主题文件

## 🔖 `3.0.0.beta3`

🕓 *Release Date / 发布日期 : 2024-06-17*

🟢 **Added / 新增**

* The docstrings for a portion of the code has been added  
添加了一部分代码的文本字符串

* `animation.animations` has added class `MoveTkWidget` to move a tkinter widget  
`animation.animations` 新增类 `MoveTkWidget` 来移动一个 tkinter 控件

* `core.containers.Canvas` added the parameter `name` to bind the theme  
`core.containers.Canvas` 新增参数 `name` 来绑定主题

* `core.containers.Canvas` added method `_zoom_children` to scale the tkinter widget of the Place layout  
`core.containers.Canvas` 新增方法 `_zoom_children` 来实现对 Place 布局的 tkinter 控件的缩放

* Introduce the optional third-party package `pillow` and add a new class `PhotoImage` in `toolbox.enhanced` to improve image scaling performance  
引入可选的第三方包 `pillow` 并在 `toolbox.enhanced` 新增类 `PhotoImage` 以提高图片缩放的性能

* Introduce an optional third-party package `matplotlib` and add a new module `mpl` to `toolbox` to achieve compatibility with `matplotlib` related interfaces  
引入可选的第三方包 `matplotlib` 并在 `toolbox` 中新增模块 `mpl` 来实现对 `matplotlib` 相关接口的兼容

* `toolbox.tools` adds the function `get_hwnd` to fetch the HWND of the widget  
`toolbox.tools` 新增函数 `get_hwnd` 来实现控件的 HWND 的获取

* `toolbox.tools` adds a new function `embed_window` to embed a widget into another widget, which only works on Windows  
`toolbox.tools` 新增函数 `embed_window` 来将一个控件嵌入到另外一个控件中，仅在 Windows 系统中有效

* `toolbox.tools` adds a new function `screen_size` to get the width and height of the screen  
`toolbox.tools` 新增函数 `screen_size` 来获取屏幕的宽度和高度

* `toolbox.tools` adds a new function `set_mouse_position` to set the mouse position, which only works on Windows  
`toolbox.tools` 新增函数 `set_mouse_position` 来设置鼠标的位置，仅在 Windows 系统中有效

* `toolbox.tools` adds a new function `_forward_methods` to implement the forwarding of class methods  
`toolbox.tools` 新增函数 `_forward_methods` 来实现类方法的转发

* Introduce optional third-party packages `pywinstyles`, `win32material` and `hPyT`, and add many new parameters to `style.manager.customize_window` to implement the corresponding interfaces  
引入可选的第三方包 `pywinstyles`、`win32material` 和 `hPyT` 并在 `style.manager.customize_window` 新增许多参数来实现对应的接口

🔴 **Removed / 移除**

* Remove function `color.rgb._str_to_hex`, this function is useless  
移除函数 `color.rgb._str_to_hex`，此函数无用

* Remove class `core.containers.Dialog`, this class is useless  
移除类 `core.containers.Dialog`，此类无用

* Removed the class `core.containers.ChildWindow` and there is a better way to replace it  
移除类 `core.containers.ChildWindow`，已有其它更好的替换方式

* Remove redundant code from `three.engine` in preparation for the next refactoring  
移除 `three.engine` 中的冗余代码，为下个版本重构做准备

🟡 **Changed / 变更**

* `animation.animations.Gradient` renamed to `GradientItem`  
`animation.animations.Gradient` 更名为 `GradientItem`

* The value of `core.constants.SIZE` has been changed from -24 to -20 (a value close to the system text size)  
`core.constants.SIZE` 的值从 -24 更改为 -20（与系统文本大小接近的值）

* The default size of most widgets has been reduced to accommodate the font size change  
大部分控件的默认大小缩小了，以配合字体大小的变更

* `style.theme` is renamed to `manager` to avoid having the same name as the theme folder  
`style.theme` 更名为 `manager`，避免跟主题文件夹 theme 重名

* The rules for storing theme files have been completely changed, as shown in the module docstring for `style.parser`  
主题文件存放规则完全更改，具体见 `style.parser` 的模块文档字符串

* `style.theme.custom_window` renamed to `style.manager.customize_window`  
`style.theme.custom_window` 更名为 `style.manager.customize_window`

* `three.engine.Side` renamed to `three.engine.Plane`  
`three.engine.Side` 更名为 `three.engine.Plane`

🔵 **Optimized / 优化**

* Now the third-party package `darkdetect` is no longer required, but optional. When this package is missing, some features will be unavailable  
现在第三方包 `darkdetect` 不是必需的了，而是可选的。当缺少此包，将导致部分功能不可用

🟣 **Fixed / 修复**

* Fixed some incorrect docstrings  
修正了部分错误的文档字符串

* Fixed an issue where the subject response event was not removed when the window was closed  
修复了窗口关闭时未删去主题响应事件的问题

* Fixed an issue where the widget style did not change completely in some cases when the widget was disabled  
修复了控件禁用时，部分情况下控件样式未完全更改的问题

🟤 **Refactored / 重构**

* `core.virtual` refactoring to remove redundant code and optimize existing code  
`core.virtual` 重构，删去冗余代码，优化已有代码

* `style` refactored  
`style` 重构

## 🔖 `3.0.0.beta2`

🕓 *Release Date / 发布日期 : 2024-06-03*

🟢 **Added / 新增**

* The docstrings for a portion of the code has been added  
添加了一部分代码的文本字符串

* Modules have added a special variable `__all__`  
模块都增加了特殊变量 `__all__`

* Subpackage `color` Added module `hsl` to support HSL color coding  
子包 `color` 新增模块 `hsl` 以支持 HSL 颜色码

* The submodule `constants` adds the function `reset` to reset all constants to default  
子模块 `constants` 新增函数 `reset` 来重置所有常量为默认值

* The submodule `theme` of the sub-package `style` has added the function `set_color_theme` to use the external theme  
子包 `style` 的子模块 `theme` 新增函数 `set_color_theme` 来使用外部主题

* Added subpackage `toolbox` and function `load_font` to introduce external font files  
新增子包 `toolbox` 以及函数 `load_font` 来引入外部字体文件

* Submodule `enhanced` of sub-package `toolbox` adds class `PhotoImage`  
子包 `toolbox` 的子模块 `enhanced` 新增类 `PhotoImage`

* The submodule `tools` class `_Trigger` has been further enhanced by the addition of methods `lock` and `unlock` and related properties  
子模块 `tools` 的类 `_Trigger` 新增方法 `lock` 和 `unlock` 以及相关属性，来进一步增强它的功能

* The submodule `images` has added a class `StillImage` to support png type static images  
子模块 `images` 新增类 `StillImage` 来支持 png 类型的静态图片

* Virtual Picture Base Class `virtual.Image` implements the relevant methods  
虚拟图片基类 `virtual.Image` 实现了相关方法

* The virtual widget base class `virtual.Widget` added new methods `appear` and `disappear` to hide and reproduce the widget as a whole  
虚拟控件基类 `virtual.Widget` 新增了方法 `appear` 和 `disappear` 来实现控件整体的隐藏和再现

🟡 **Changed / 变更**

* The classes `Message`, `ColorChooser`, and `FontChooser` of the submodule `dialogs` have been renamed `TkMessage`, `TkColorChooser`, and `TkFontChooser`, respectively  
子模块 `dialogs` 的类 `Message`、`ColorChooser` 和 `FontChooser` 分别更名为 `TkMessage`、`TkColorChooser` 和 `TkFontChooser`

* The function `tkintertools.style.theme.use_theme` is renamed to `set_color_mode`  
函数 `tkintertools.style.theme.use_theme` 更名为 `set_color_mode`

* The rotation event of the class `Space` of the subpack `three` has been changed from the original left-mouse button to the middle mouse button  
子包 `three` 的类 `Space` 的旋转事件由原来的鼠标左键触发更改为鼠标中键触发

🔵 **Optimized / 优化**

* Optimized the implementation of the function `custom_window` of the submodule `theme` to prevent it from taking effect in some cases  
优化了子模块 `theme` 的函数 `custom_window` 的实现方式，防止某些情况下无法生效

* All container widgets have been optimized to prevent the functionality from working under certain conditions  
所有容器控件都得到了优化，防止某些条件下会出现相关功能未生效的情况

* All virtual widgets are perfected with initialization parameters  
所有虚拟控件都完善了初始化参数

🟤 **Refactored / 重构**

* Core code refactoring, from module `core.py` to sub-package `core`  
核心代码重构，由模块 `core.py` 重构为子包 `core`

* Subpackage `three` refactoring  
子包 `three` 重构

## 🔖 `3.0.0.beta1`

🕓 *Release Date / 发布日期 : 2024-05-17*

🟢 **Added / 新增**

* The docstrings for a portion of the code has been added  
添加了一部分代码的文本字符串

* Added the animation class `MoveItem` to move items on the canvas  
增加了动画类 `MoveItem` 来移动画布上的 Item

* The animation base class `Animation` adds the initialization parameter `derivation` to control whether the parameters of the callback function are derived  
动画基类 `Animation` 增加了初始化参数 `derivation` 来控制回调函数的参数是否求导

* The subpackage `color` adds the module `colormap` to speed up the conversion of color names to their corresponding RGB codes  
子包 `color` 增加了模块 `colormap` 来加速颜色名称到其对应 RGB 码的转换速度

* The subpackage `color` adds the functions `contrast`, `convert`, `blend` and `gradient` to complete the color processing mechanism  
子包 `color` 新增函数 `contrast`、`convert`、`blend` 和 `gradient` 来完善颜色处理机制的功能

* The subpackage `style` adds the module `theme` to control the overall theme of the application  
子包 `style` 新增模块 `theme` 来控制应用程序整体的主题

* Added method `disabled` to the widget class to disable it. If a style with a disabled state is defined in the stylesheet, the defined style is used, otherwise the style in the disabled state is automatically generated based on the current style (color to background color conversion by a factor of 0.618)  
控件类新增方法 `disabled` 来使其处于禁用状态。若在样式表中定义了禁用状态的样式，则会使用定义的样式，否则根据当前样式自动生成禁用状态的样式（色彩向背景色转换 0.618 倍）

* The widget `RadioButton` has a new initialization parameter `default` to control its default state  
控件 `RadioButton` 新增初始化参数 `default` 来控制其默认的状态

* Experimental support for color strings in RGBA format has been added to the Color subpackage  
颜色子包新增对 RGBA 格式的颜色字符串的实验性支持

🟣 **Fixed / 修复**

* Fixed an bug where the animation classes `MoveWidget` and `MoveComponent` were not moving objects to the correct position when they were called repeatedly  
修复了动画类 `MoveWidget` 和 `MoveComponent` 在被反复调用的情况下无法将对象移动到正确位置的问题

* Fixed an bug where the animation class `ScaleFontSize` did not scale the font size correctly  
修复了动画类 `ScaleFontSize` 无法正确缩放字体大小的问题

* Fixed and enhanced a bug with the centering function of container widgets such as `Toplevel`  
修复并增强了容器控件 `Toplevel` 等在居中功能上的问题

🔵 **Optimized / 优化**

* Optimized the way to get the style file, the widget can set a relative name to reduce the amount of code, and the relative name starts with a decimal point  
优化了样式文件的获取方式，小组件可以设置相对名称来减少代码量，相对名称以小数点开头

* The theme mechanism is optimized, there is no longer a need to write a tag in the style file, and the mapping relationship between the color parameters of the item and the keywords of the style file can be written in the definition of `Shape`, so as to reduce the redundant content in the style file and improve the compatibility between the style files  
主题机制优化，样式文件中不再需要写出 tag，可在 `Shape` 的定义中写明 Item 的颜色参数与样式文件关键字的映射关系，以此缩减样式文件中的冗余内容，提高各样式文件之间的兼容性

* Optimized the appearance of some widgets  
优化部分控件外观

* Improved cross-platform compatibility  
提高了跨平台的兼容性

* Improved 3D submodule compatibility with the new version of `tkintertools`  
提高了 3D 子模块对新版 `tkintertools` 兼容性

* Change the constants `FONT` and `SIZE` to dynamic values, so that font modifications can take effect globally  
将常量 `FONT` 和 `SIZE` 改成动态取值，便于字体修改可以全局生效

🟡 **Changed / 变更**

* The animation class `Gradient` no longer converts an empty color string to black when it accepts it, but simply throws an exception  
动画类 `Gradient` 在接受空颜色字符串时不再将其转化为黑色，而是直接抛出异常

* The implementation code for the 3D subpackage has been moved from file `three/__init__.py` to file `three/engine.py`  
3D 子包的实现代码从文件 `three/__init__.py` 移动到了文件 `three/engine.py`

* The submodule `style` has been changed to the sub-package `style` and its contents have been reorganized  
子模块 `style` 变更为子包 `style`，其内容进行了重新的整理

🔴 **Removed / 移除**

* Remove the useless class from the submodule `images` of the subpackage `standard`  
移除子包 `standard` 的子模块 `images` 中无用的类

* Remove the function `color` from the color subpack (There are other better implementations)  
移除颜色子包中的函数 `color`（已有其他更好的实现）

🟤 **Refactored / 重构**

* Some of the code has been refactored  
重构了部分代码

## 🔖 `3.0.0.alpha7`

🕓 *Release Date / 发布日期 : 2024-05-05*

🟤 **Refactored / 重构**

* Introducing a pure Python-based third-party module, `darkdetect`, to implement theme dynamic following system and multi-OS dark theme support  
引入纯 Python 实现的第三方模块 `darkdetect`，以实现主题动态跟随系统以及多操作系统暗黑主题的支持

* Added text class widget  
新增文本类控件

* Fixed a few bugs and added a lot of content to the framework  
修复些许 bug，框架内增加大量内容

* Some basic dialogs have been added  
增加了部分基本对话框

## 🔖 `3.0.0.alpha6`

🕓 *Release Date / 发布日期 : 2024-04-30*

🟤 **Refactored / 重构**

* The framework has been further upgraded to allow you to build widgets for complex elements  
框架进一步升级，可以构建复杂元素的控件了

* A lot of bugs have been fixed, and a lot of content has been improved within the framework  
修复大量 bug，框架内完善大量内容

* The animation sub-module has been added to build high-precision and complex animations  
新增动画子模块，可以构建高精度复杂动画了

* Color gradient animations are added to widgets, and special animations are added to some widgets, such as switch switches  
控件增加颜色渐变动画，部分控件增加特殊动画，如开关切换等

* Some widgets have been improved  
完善部分控件

## 🔖 `3.0.0.alpha5`

🕓 *Release Date / 发布日期 : 2024-04-16*

🟤 **Refactored / 重构**

* The framework has been upgraded to allow you to build multi-element widgets  
框架升级，可以构建多元素的控件了

* A lot of bugs have been fixed, and a lot of content has been improved within the framework  
修复大量 bug，框架内完善大量内容

* The theme binding method has been changed to improve the degree of automation, free hands as much as possible, and reduce the amount of code for users  
主题绑定方式更改，提高自动化程度，尽可能解放双手，减少用户的代码量

* UI evolution to reduce aliasing and improve clarity  
UI 进化，减小锯齿感，提升清晰度

* Some standard widgets have been added  
增加部分标准控件

## 🔖 `3.0.0.alpha4`

🕓 *Release Date / 发布日期 : 2024-04-05*

🟤 **Refactored / 重构**

* The 3D submodule of `tkintertools 2` was successfully ported to `tkintertools 3`  
成功将 `tkintertools 2` 的 3D 子模块移植到 `tkintertools 3` 上

* A lot of bugs have been fixed, and a lot of content has been improved within the framework  
修复大量 bug，框架内完善大量内容

* Added a theme mechanism that allows two sets of themes that can be switched between light and dark  
新增主题机制，允许明暗两套可切换的主题

* The UI has been updated to provide both Windows 10 and Windows 11 style dark and bright themes  
UI 更新，提供 Windows 10 和 Windows 11 风格的暗黑与明亮两套主题

* Highly customizable widgets are now available  
可高度定制化控件了

## 🔖 `3.0.0.alpha3`

🕓 *Release Date / 发布日期 : 2024-02-20*

🟤 **Refactored / 重构**

* Fixed a few bugs and added a lot of content to the framework  
修复些许 bug，框架内增加大量内容

* The designer is in development mode  
设计器已进入开发状态

## 🔖 `3.0.0.alpha2`

🕓 *Release Date / 发布日期 : 2024-02-18*

🟤 **Refactored / 重构**

* Fixed a few bugs and added a lot of content to the framework  
修复些许 bug，框架内增加大量内容

* Added some widgets  
新增一些控件

* The background color of the container widget automatically follows the parent widget  
容器控件的背景色自动跟随父控件

## 🔖 `3.0.0.alpha1`

🕓 *Release Date / 发布日期 : 2024-02-17*

🟤 **Refactored / 重构**

* The widget framework has been built, the details are not yet completed, and some widgets have been built for testing  
控件框架搭建完成，细节部分还未完成，已构建部分控件用于测试

* Customizable widgets are now available  
可定制化控件了

* Fixed a few bugs and added a lot of content to the framework  
修复些许 bug，框架内增加大量内容

* Improved `Canvas`'s scaling mechanism  
完善了 `Canvas` 的缩放机制

* Added some widgets  
新增一些控件

## 🔖 `3.0.0.dev9`

🕓 *Release Date / 发布日期 : 2023-02-16*

🟤 **Refactored / 重构**

* The widget framework is almost complete, and the details are not yet complete  
控件框架基本完成，细节部分还未完成

## 🔖 `3.0.0.dev8`

🕓 *Release Date / 发布日期 : 2023-02-15*

🟤 **Refactored / 重构**

* Container widget `tkintertools.Canvas` has completed support for `tkinter._CanvasItemId`, as well as a host of other improvements  
容器控件 `tkintertools.Canvas` 已完成对 `tkinter._CanvasItemId` 的支持，以及其它大量改进

## 🔖 `3.0.0.dev7`

🕓 *Release Date / 发布日期 : 2023-02-04*

🟤 **Refactored / 重构**

* Container widget `tkintertools.Canvas` has been adapted to three layouts: `Pack`, `Place`, and `Grid`, with `Place` being strengthened  
容器控件 `tkintertools.Canvas` 已完成对三种布局方式 `Pack`、`Place` 和 `Grid` 的适配，其中 `Place` 被加强

## 🔖 `3.0.0.dev6`

🕓 *Release Date / 发布日期 : 2024-01-19*

🟤 **Refactored / 重构**

* The window nesting feature is added under the Windows platform  
Windows 平台下新增窗口嵌套功能

* Added controls for window border color, title bar background color, and title bar foreground color under the Windows platform  
Windows 平台下新增对窗口边框颜色、标题栏背景色和标题栏前景色的控制

## 🔖 `3.0.0.dev5`

🕓 *Release Date / 发布日期 : 2023-09-26*

🟤 **Refactored / 重构**

* Basic functions are being refactored...  
基本功能重构中……

## 🔖 `3.0.0.dev4`

🕓 *Release Date / 发布日期 : 2023-09-24*

🟤 **Refactored / 重构**

* Basic functions are being refactored...  
基本功能重构中……

## 🔖 `3.0.0.dev3`

🕓 *Release Date / 发布日期 : 2023-09-21*

🟤 **Refactored / 重构**

* Basic functions are being refactored...  
基本功能重构中……

## 🔖 `3.0.0.dev2`

🕓 *Release Date / 发布日期 : 2023-09-21*

🟤 **Refactored / 重构**

* Basic functions are being refactored...  
基本功能重构中……

## 🔖 `3.0.0.dev1`

🕓 *Release Date / 发布日期 : 2023-09-20*

🟤 **Refactored / 重构**

* Basic functions are being refactored...  
基本功能重构中……

## 🔖 `3.0.0.dev0`

🕓 *Release Date / 发布日期 : 2023-09-19*

🟤 **Refactored / 重构**

* Start a refactoring of the new version of `tkintertools 3` to solve the problems that can't be solved in `tkintertools 2` and bring more and better features!  
开启全新版本 `tkintertools 3` 的重构，以解决 `tkintertools 2` 中无法解决的问题，并带来更多更棒的功能！

## 🔖 `2.6.21`

🕓 *Release Date / 发布日期 : 2024-01-01*

🟡 **Changed / 变更**

* The class `Text` in submodule `tools_3d` was renamed `Text3D` to distinguish `Text` in `main`  
子模块 `tools_3d` 中的类 `Text` 更名为 `Text3D` 以区分 `main` 中的 `Text`

🔵 **Optimized / 优化**

* Improved Type Hints  
完善了类型提示

🟣 **Fixed / 修复**

* Fixed a bug where the parameter `proportion` of the function `color` was invalid  
修复了函数 `color` 的参数 `proportion` 失效的问题

* Fixed a bug where the `configure` parameter of the `Switch` class was incorrect  
修复了类 `Switch` 的方法 `configure` 参数取值错误的问题

🔴 **Removed / 移除**

* `Animation` has removed the `color` parameter (can be implemented with the `callback` parameter)  
动画类 `Animation` 移除了参数 `color`（可用参数 `callback` 代替实现）

## 🔖 `2.6.20`

🕓 *Release Date / 发布日期 : 2023-12-26*

🔵 **Optimized / 优化**

* The pause and resume functionality of the image class `PhotoImage` is encapsulated in the methods `pause` and `play`  
图片类 `PhotoImage` 的暂停和继续播放功能被封装为方法 `pause` 和 `play`

* Optimized the way the `PhotoImage` class gets the total number of frames of a gif image, and now you can get the total number of frames by method `get_total_frames`  
优化类 `PhotoImage` 获取 gif 图片总帧数的方式，现在可以通过方法 `get_total_frames` 得到总帧数

* The `color` function no longer manually obtains a gradient with a specified regularity, but instead specifies a control function through the parameter `controller`  
函数 `color` 不再通过手动方式得到指定规律的渐变色，而是通过参数 `controller` 指定一个控制函数

🟡 **Changed / 变更**

* The original method of `play` used for `PhotoImage` to start playback has been renamed to `start` to avoid conflicts with the method of `play` to continue playback  
图片类 `PhotoImage` 原来用于开始播放的方法 `play` 更名为 `start` 避免与继续播放的方法 `play` 起冲突

* The constant `CONTROL` was renamed `CONTROLLER`  
常量 `CONTROL` 更名为 `CONTROLLER`

🟣 **Fixed / 修复**

* Fixed some incorrect type hints  
修复了一些错误的类型提示

## 🔖 `2.6.19`

🕓 *Release Date / 发布日期 : 2023-12-17*

🟣 **Fixed / 修复**

* Fixed a bug where GIFs could not be played  
修复 gif 动图无法播放的问题

🔵 **Optimized / 优化**

* `PhotoImage` has optimized the mechanism of playing GIFs, and if there is no pre-parsing before playback, it will be automatically parsed during playback  
图片类 `PhotoImage` 关于播放 gif 动图的机制得到优化，若播放前没有预解析，则会自动进行播放时解析

* Some codes have been optimized  
优化了部分代码

## 🔖 `2.6.18`

🕓 *Release Date / 发布日期 : 2023-12-10*

🟣 **Fixed / 修复**

* Fixed a bug where the actual font size of 3D text with the same font size setting was inconsistent in different locations  
修复在不同位置的但字体大小设定相同的 3D 文本的实际字体大小不一致的 bug

🟡 **Changed / 变更**

* Class `Canvas_3D` was renamed `Canvas3D`, and Class `_3D_Object` was renamed to `_Object3D`  
类 `Canvas_3D` 更名为 `Canvas3D`，类 `_3D_Object` 更名为 `_Object3D`

🔵 **Optimized / 优化**

* Some codes have been optimized  
优化了部分代码

## 🔖 `2.6.17`

🕓 *Release Date / 发布日期 : 2023-12-07*

🔵 **Optimized / 优化**

* Corrected some incorrect English words  
修改了部分错误的英文单词

🟡 **Changed / 变更**

* The font unit changes from points to pixels  
字体单位由磅更改为像素

* Reduced the display position offset of tooltip widgets  
减小了提示框控件的显示位置偏移

🟣 **Fixed / 修复**

* Fixed a bug where tooltip widgets could appear in very wrong places  
修复了提示框控件有可能显示在非常错误的位置的问题

* Fixed a bug where the widget class `Entry` was in a non-centered state and the canvas was shrunk, entering an endless loop when entering text, causing the window to not respond  
修复了控件类 `Entry` 在非居中状态，且画布缩小之后，输入文本时进入死循环，导致窗口未响应的问题

* Fixed a bug where widget color properties were sometimes unchangeable  
修复了控件颜色属性某些时候不可更改的问题

## 🔖 `2.6.16`

🕓 *Release Date / 发布日期 : 2023-12-01*

🟢 **Added / 新增**

* The `ToolTip` class has added a `delay` parameter to enhance functionality  
类 `ToolTip` 新增参数 `delay` 来增强功能

🔵 **Optimized / 优化**

* The function `askfont` has been optimized so that the font selection dialog can now be opened without the need for a parent container widget  
对函数 `askfont` 进行了优化，现在无需父容器控件也可以打开字体选择对话框

🟡 **Changed / 变更**

* The values of some constants have been modified  
部分常量的值进行了修改

🔴 **Removed / 移除**

* Removed the function `SetProcessDpiAwareness` and the constant `PROCESS_SYSTEM_DPI_AWARE`  
移除函数 `SetProcessDpiAwareness` 和常量 `PROCESS_SYSTEM_DPI_AWARE`

🟣 **Fixed / 修复**

* Fixed the bug that the font size of the menu bar was abnormal  
修复菜单栏字体大小异常的问题

* Fixed the bug that images could not be loaded  
修复图片无法加载的问题

## 🔖 `2.6.15`

🕓 *Release Date / 发布日期 : 2023-11-26*

🟢 **Added / 新增**

* A new method for the `Animation` class is called `shutdown` to terminate the current animation  
类 `Animation` 新增方法 `shutdown` 来终止当前动画

* The geometry class `Cuboid` and the geometry class `Tetrahedron` of submodule `tools_3d` have been initialized to increase the degree of freedom in style configuration  
子模块 `tools_3d` 的类 `Cuboid` 和类 `Tetrahedron` 新增一些初始化参数来提高样式配置的自由度

* The constants `TCL`, `PROPORTION`, `SEQLENGTH`, and `NUM` are added  
新增常量 `TCL`、`PROPORTION`、`SEQLENGTH` 和 `NUM`

* The `color` function adds the parameters `seqlength` and `num` to enhance the functionality  
函数 `color` 新增参数 `seqlength` 和 `num` 来增强功能

🔵 **Optimized / 优化**

* The parameter support for the function `color` has been expanded to support color names such as red, skyblue, and cyan2  
函数 `color` 的参数支持的范围扩大，可以支持诸如 red、skyblue 和 cyan2 等颜色名称

* Some functions can be called without the need for a parent widget  
部分函数无需父控件即可调用

🟣 **Fixed / 修复**

* Fixed a bug where the function `color` would get an incorrect result in rare cases  
修复了函数 `color` 在罕见情况下会得到错误结果的问题

## 🔖 `2.6.14`

🕓 *Release Date / 发布日期 : 2023-11-17*

🟢 **Added / 新增**

* The `CheckButton` widget class adds a `font` parameter to modify its font  
控件类 `CheckButton` 新增参数 `font` 来修改其字体

🟡 **Changed / 变更**

* Modify the name of some color constants and the parameters related to some colors  
修改部分颜色常量的名称和部分颜色相关的参数

* The widget class `Progressbar` is renamed to `ProgressBar`  
控件类 `Progressbar` 更名为 `ProgressBar`

🟣 **Fixed / 修复**

* Fixed the bug that the color of the `Switch` of the widget class was displayed incorrectly  
修复控件类 `Switch` 颜色显示错误的问题

* Fixed a bug where the initial color of the `CheckButton` of the widget class would not be displayed immediately  
修复控件类 `CheckButton` 初始颜色不会立刻显示的问题

* Fixed the bug that the text style of the widget class `Entry` was not updated after calling the method `set`  
修复控件类 `Entry` 在调用方法 `set` 之后文本样式没有更新的问题

## 🔖 `2.6.13`

🕓 *Release Date / 发布日期 : 2023-11-17*

🟢 **Added / 新增**

* The submodule `tools_3d` adds markup text-related functions and corresponding parameters to the class `Point`: `markuptext`, `markupdelta`, `markupfont`, `markupfill`, and `markupjustify`  
子模块 `tools_3d` 的类 `Point` 新增标记文本相关功能以及对应参数：`markuptext`、`markupdelta`、`markupfont`、`markupfill` 和 `markupjustify`

* Submodule `tools_3d` adds a new class `Text` to implement 3D text that is always facing us (unlike markup text, which has a zoom function)  
子模块 `tools_3d` 新增类 `Text` 来实现始终朝向我们的 3D 文本（与标记文本不同，其有缩放功能）

🟡 **Changed / 变更**

* The class `Switch` has been partially refactored from a stand-alone class to a subclass that inherits from the base class `BaseWidget`, and a number of methods have been added that are compatible with `BaseWidget`  
类 `Switch` 部分重构，由独立类变更为继承基类 `BaseWidget` 的子类，添加了许多和 `BaseWidget` 兼容的方法

* Change the main code file name to main.py to avoid occupying the special file name \_\_main\_\_.py  
修改主代码文件名称为 main.py，避免占用特殊文件名 \_\_main\_\_.py

🟣 **Fixed / 修复**

* Fixed a bug where submodule `tools_3d` was reversed on Z coordinates, i.e., changing the spatial coordinate system from a left-handed coordinate system to a right-handed coordinate system  
修复子模块 `tools_3d` 在 Z 坐标上正负颠倒的问题，即，将空间坐标系由左手坐标系改为右手坐标系

## 🔖 `2.6.12`

🕓 *Release Date / 发布日期 : 2023-11-15*

🟢 **Added / 新增**

* Widget class `CheckButton` adds parameter `tick` to change its markup symbol  
控件类 `CheckButton` 新增参数 `tick` 来改变其标记符号

* The `Switch` widget class adds parameters `color_fill_slider` and `color_outline_slider` to change the appearance of its internal sliders  
控件类 `Switch` 新增参数 `color_fill_slider` 和 `color_outline_slider` 来更改其内部滑块的外观

🔵 **Optimized / 优化**

* Drastically changed the format of the docstring to solve the problem that the docstring was displayed out of order on PyCharm  
大幅度修改 docstring 的格式，以解决 docstring 在 PyCharm 上格式显示错乱的问题

* Remove redundant code  
移除冗余代码

* Optimized `tools_3d` submodule code to improve performance by 13.26%  
优化了 `tools_3d` 子模块代码，提高了 13.26% 的性能

🟣 **Fixed / 修复**

* Fixed a bug where when clicking on a widget, the widget behind it would also be triggered  
修复了点击控件时，其后面的控件也会被触发的问题

* Missing symbol '#' for function `color` return value  
函数 `color` 返回值缺少符号 “#”

* Fixed a bug where the canvas of the `tools_3d` submodule could not use widgets such as buttons  
修复 `tools_3d` 子模块的画布无法使用按钮等控件的问题

* Fixed a bug where the `Switch` of the Widget class could not control the `Switch` by clicking on the inner slider  
修复了控件类 `Switch` 点击内部滑块无法操控 `Switch` 的问题

## 🔖 `2.6.11`

🕓 *Release Date / 发布日期 : 2023-10-17*

🔵 **Optimized / 优化**

* Optimized the code of submodule `tools_3d`, introduced built-in module `array` instead of the underlying list to improve the calculation speed, and improved the overall performance by 11.66% !  
优化了子模块 `tools_3d` 的代码，引入内置模块 `array` 代替底层列表来提高计算速度，综合性能提升 11.66% ！

🔴 **Removed / 移除**

* Removed classes `_Point`, `_Line` and `_Side` from submodule `tools_3d`  
移除了子模块 `tools_3d` 中的类 `_Point`、`_Line` 和 `_Side`

## 🔖 `2.6.10`

🕓 *Release Date / 发布日期 : 2023-08-12*

🟢 **Added / 新增**

* Added file exceptions.py and exception classes `ScaleArgsValueError`, `ColorArgsValueError` and `WidgetStateModeError` to provide a description of some exceptions  
新增文件 exceptions.py 及异常类 `ScaleArgsValueError`、`ColorArgsValueError` 和 `WidgetStateModeError` 以提供部分异常的描述

* The widget `Progressbar` adds a indeterminate mode  
控件 `Progressbar` 新增不定模式

🟡 **Changed / 变更**

* The value of the constant `SWITCH_WIDTH` is changed from 0 to 60  
常量 `SWITCH_WIDTH` 的值从 0 更改为 60

* The parameter `width` of class `Switch` was changed from positional argument to keyword argument  
类 `Switch` 的参数 `width` 由位置参数更改为关键字参数

🔵 **Optimized / 优化**

* Change the way the output is formatted in all code from the "%" mode to the more efficient f-string mode  
将所有代码中格式化输出的方式由 “%” 方式更改为效率更高的 f-string 方式

* Optimized type hints for some code  
优化了部分代码的类型提示

🔴 **Removed / 移除**

* Remove the function `text` and use f-string instead  
移除函数 `text`，可使用 f-string 来对其进行代替

## 🔖 `2.6.9`

🕓 *Release Date / 发布日期 : 2023-08-09*

🟢 **Added / 新增**

* Added new widget switch (`Switch`)  
新增控件开关（`Switch`）

* Added widget Tip (`ToolTip`) and all virtual widgets added the parameter `tooltip`  
新增控件提示框（`ToolTip`），且所有虚拟控件新增参数 `tooltip`

* Added constants `DURATION`、`TOOLTIP_FG`、`TOOLTIP_BG`、`TOOLTIP_HIGHLIGHT_THICKNESS`、`TOOLTIP_HIGHLIGHT_BACKGROUND`、`COLOR_SWITCH_ON`、`COLOR_SWITCH_OFF`、`SWITCH_WIDTH`、`SWITCH_HEIGHT`、`SWITCH_RADIUS` and `SWITCH_ANIMATION_MS`  
新增常量 `DURATION`、`TOOLTIP_FG`、`TOOLTIP_BG`、`TOOLTIP_HIGHLIGHT_THICKNESS`、`TOOLTIP_HIGHLIGHT_BACKGROUND`、`COLOR_SWITCH_ON`、`COLOR_SWITCH_OFF`、`SWITCH_WIDTH`、`SWITCH_HEIGHT`、`SWITCH_RADIUS` 和 `SWITCH_ANIMATION_MS`

🟣 **Fixed / 修复**

* Fixed an issue where the text class widget called method `clear` was invalid  
修复了文本类控件调用方法 `clear` 无效的问题

* Fixed an issue where the class `Animation` automatically determined the parent widget of the widget to be moved  
修复了类 `Animation` 自动确定待移动控件的父控件时出现错误的问题

🟡 **Changed / 变更**

* The positional parameter `length` of class `CheckButton` was renamed `height`  
类 `CheckButton` 的位置参数 `length` 更名为 `height`

🔵 **Optimized / 优化**

* Optimized the method `wm_geometry` of class `Tk` to accommodate some specially formatted parameters  
优化了类 `Tk` 的方法 `wm_geometry` 以适应某些特殊格式的参数

🔴 **Removed / 移除**

* Removed class `Singleton` and function `move`  
移除了类 `Singleton` 和函数 `move`

## 🔖 `2.6.8`

🕓 *Release Date / 发布日期 : 2023-08-03*

🟢 **Added / 新增**

* If the user's Python includes a PIL library, PIL is automatically invoked when autoscaling images to extend the functionality of the class `PhotoImage`  
若使用者的 Python 包含有 PIL 库，则在自动缩放图片时自动调用 PIL 来扩展类 `PhotoImage` 的功能

* Added class `Animation` to achieve more efficient, convenient and functional animation effects  
新增类 `Animation` 来实现更加高效、更加方便和功能性更强的动画效果

* Added constant `CONTROL`  
新增常量 `CONTROL`

🟣 **Fixed / 修复**

* Fixed the bug that widgets `Entry` and `Text` would report an error when pasting text  
修复控件 `Entry` 和 `Text` 粘贴文本时会报错的 bug

🟡 **Changed / 变更**

* Modified the name of the constant `FRAMES` to `FPS`  
修改常量 `FRAMES` 的名称为 `FPS`

* The parameter `precision` of the method `zoom` of class `PhotoImage` was changed from positional argument to keyword argument  
类 `PhotoImage` 的方法 `zoom` 的参数 `precision` 由位置参数变更为关键字参数

🟠 **Deprecated / 弃用**

* The function `move` is about to be deprecated, please replace it with the new class `Animation`  
函数 `move` 即将被弃用，请用新类 `Animation` 来代替

* The class `Singleton` is about to be deprecated and singleton mode classes will no longer be available in subsequent releases  
类 `Singleton` 即将被弃用，后续版本中将不再提供单例模式类

## 🔖 `2.6.7`

🕓 *Release Date / 发布日期 : 2023-07-06*

🟢 **Added / 新增**

* The function `rotate` of the 3D submodule adds the keyword `axis` to provide the function of rotating around the axis  
3D 子模块的函数 `rotate` 新增关键字参数 `axis` 来提供绕轴旋转的功能

* Added constants `ROTATE_CENTER`, `ORIGIN_COORDINATE`, `ORIGIN_SIZE`, `ORIGIN_WIDTH`, `ORIGIN_FILL` and `ORIGIN_OUTLINE`  
新增常量 `ROTATE_CENTER`、`ORIGIN_COORDINATE`、`ORIGIN_SIZE`、`ORIGIN_WIDTH`、`ORIGIN_FILL` 和 `ORIGIN_OUTLINE`

* Class `Tk` and `Toplevel` Added keyword arguments `alpha`, `toolwindow`, `topmost` and `transparentcolor`  
类 `Tk` 和 `Toplevel` 新增关键字参数 `alpha`、`toolwindow`、`topmost` 和 `transparentcolor`

🟣 **Fixed / 修复**

* Fixed a bug where the class `Text` would report an error when scrolling with the mouse wheel  
修复了类 `Text` 在使用鼠标滚轮滚动时会报错的 bug

🔵 **Optimized / 优化**

* Optimized some code and type hints  
优化了部分代码和类型提示

* Optimized the internal implementation of the functions `translate` and `scale` to improve performance  
优化函数 `translate`、`rotate` 和 `scale` 内部的实现，提高了性能

* A large number of incomplete docstrings have been modified and improved  
修改和完善了大量的不完整的文档注释

🟡 **Changed / 变更**

* Change some methods of some classes to protection methods  
将部分类的部分方法更改为保护方法

🔴 **Removed / 移除**

* Removed abstract classes and abstract methods  
移除了抽象类和抽象方法

## 🔖 `2.6.6`

🕓 *Release Date / 发布日期 : 2023-07-01*

🟢 **Added / 新增**

* The classes `_Point`, `_Line`, `_Side`, and `Geometry` of the 3D submodule all have a new method `center` that returns the geometric center of the 3D object  
3D 子模块的类 `_Point`、`_Line`、`_Side` 和 `Geometry` 都新增一个方法 `center` 返回该 3D 对象的几何中心

* Added abstract class `_3D_Object` as the metabase class for classes `_Point`, `_Line`, and `_Side`  
新增抽象类 `_3D_Object` 来作为类 `_Point`、`_Line` 和 `_Side` 的元基类

🔵 **Optimized / 优化**

* Optimized parameter passing in 3D submodules, users do not need to ensure the transitivity of `list` at all times, and parameters that used to only use the `list` type are now `Iterable` type  
优化了 3D 子模块中的参数传递，使用者不需要时刻保证 `list` 的传递性，且原来只能使用 `list` 类型的参数现在为 `Iterable` 类型

* The way 3D objects are centered in the 3D submodule has changed, which has improved performance and reduced the amount of code  
3D 子模块中 3D 对象居中方式改变，相比原来性能提升了不少，代码量也减少了

* Corrected some incorrect type hints and improved some missing method comments  
改正了部分错误的类型提示，完善了部分缺少的方法注释

* In the 3D submodule, the distance between two points was originally calculated with the function `hypot`, and now the function `dist` is used directly to calculate the Euclidean distance between two points to improve performance  
3D 子模块中原来用函数 `hypot` 计算两点间距离，现在直接用函数 `dist` 计算两点间欧几里得距离，提高性能

* The position display of widgets of class `Point` has been optimized in the 3D submodule so that it is always at the forefront  
3D 子模块中优化了类 `Point` 的控件位置显示，让其始终保持在最前

* The calculation formula for the camera distance in the 3D submodule has been optimized to improve the performance by a bit  
3D 子模块中相机距离的计算公式优化，提高了一点性能

🟡 **Changed / 变更**

* The parameters `point1` and `point2` of class `Point` of the 3D submodule and its parent class `_Point` were renamed to `point_start` and `point_end` respectively  
3D 子模块的类 `Point` 及其父类 `_Point` 的参数 `point1` 和 `point2` 分别被重命名为 `point_start` 和 `point_end`

* The parameter `origin_color` of the class `Space` of the 3D submodule has been changed to four new parameters, namely `origin_size`, `origin_width`, `origin_fill` and `origin_outline`  
3D 子模块的类 `Space` 的参数 `origin_color` 被更改为四个新的参数，分别是 `origin_size`、`origin_width`、`origin_fill` 和 `origin_outline`

🔴 **Removed / 移除**

* The classes `Canvas_3D` and `Space` of the 3D submodule remove the parameters `dx` and `dy`, and the default field of view of the canvas remains centered, i.e. their center is now the original upper-left vertex  
3D 子模块的类 `Canvas_3D` 和 `Space` 移除参数 `dx` 和 `dy`，画布默认视野保持居中，也就是说，现在它们的中心位置才是原来的左上角顶点

## 🔖 `2.6.5`

🕓 *Release Date / 发布日期 : 2023-06-17*

🟢 **Added / 新增**

* The new class `Space` added to the submodule `tools_3d` can provide the ability to translate, rotate and scale 3D objects  
子模块 `tools_3d` 新增类 `Space` 可以提供对 3D 对象进行平移、旋转和缩放等操作的功能

🟣 **Fixed / 修复**

* Fixed a bug where class `Cuboid` and class `Tetrahedron` did not add instances to parent class `Canvas_3D`  
修复了类 `Cuboid` 和类 `Tetrahedron` 没有将实例添加到父类 `Canvas_3D` 的 bug

* Fixed a bug where an error was displayed when a 3D object appeared behind the camera position  
修复了当 3D 对象出现在相机位置后面时会显示错误的 bug

* Fixed some incorrect type hints  
修复了部分错误的类型提示

🔴 **Removed / 移除**

* Removed the constant `BACKGROUND` and no longer qualified the default background color of class `Canvas`  
移除常量 `BACKGROUND` 并且不再对类 `Canvas` 的默认背景颜色做限定

## 🔖 `2.6.4`

🕓 *Release Date / 发布日期 : 2023-06-12*

🟢 **Added / 新增**

* The class `tool_3d` submodule `Canvas_3D` has added the function `space_sort` to calculate and sort the actual position of space to support the correct display of geometry colors  
`tool_3d` 子模块的类 `Canvas_3D` 新增对空间实际位置进行计算和排序的函数 `space_sort`，以支持几何体颜色的正确显示

🟣 **Fixed / 修复**

* Fixed a bug where movement and rotation between points, lines, and sides in the 3D module are out of sync  
修复 3D 模块中的点、线与面之间移动和旋转不同步的 bug

* Fixed a bug where class `Canvas_3D` in the 3D module would be invalid when passing arguments to class `Canvas` in the original `tkinter` module  
修复 3D 模块中的类 `Canvas_3D` 在传递原 `tkinter` 模块中的类 `Canvas` 的参数时会无效的 bug

🟡 **Changed / 变更**

* The parameter `cfg_3d` of class `Canvas_3D` is changed to 3 specific parameters, namely camera distance `camera_distance`, picture abscissa deviation `dx` and screen ordinate deviation `dy`  
类 `Canvas_3D` 的参数 `cfg_3d` 被更改为 3 个具体的参数，分别为相机距离 `camera_distance`、画面横坐标偏差 `dx` 和画面纵坐标偏差 `dy`

* In the 3D submodule, the value of the camera distance constant is changed to 1000  
3D 子模块中相机距离常量的值更改为 1000

* Compatibility changes, because Python 3.7 is about to enter the end-of-life stage, and in order to improve program performance, Python3.7 is not compatible, but Python3.8 is compatible  
兼容性更改，由于 Python3.7 即将步入 end-of-life 阶段，且为了提高程序性能，现无法兼容 Python3.7，但能够兼容 Python3.8

## 🔖 `2.6.3`

🕓 *Release Date / 发布日期 : 2023-06-07*

🔵 **Optimized / 优化**

* The 3D object implementation varies with the size of the canvas  
3D 对象实现随画布大小变化而变化

* Make the default value of the corner radius more intelligent, 4 when the system is `Windows11`, `Linux`, `Mac`, and 0 for the rest  
使圆角半径的默认值更加智能，当系统为 `Windows11`、`Linux`、`Mac` 时为 4，其余情况为 0

* Added more type hints, especially for overloads  
添加了更多类型提示，尤其是对重载的提示

🟣 **Fixed / 修复**

* Fixed a bug where the parameter `keep` would affect the position of class `Canvas`  
修复参数 `keep` 会对类 `Canvas` 的位置产生影响的 bug

🟡 **Changed / 变更**

* Set the default value of the parameter `keep` of the class `Canvas_3D` in the 3D module to `True`, i.e. keep the canvas width and height scaled proportionally by default  
将3d模块中的类 `Canvas_3D` 的参数 `keep` 的默认值设为 `True`，即默认保持画布宽高缩放成比例

## 🔖 `2.6.2`

🕓 *Release Date / 发布日期 : 2023-05-30*

🟢 **Added / 新增**

* Added `tkintertools` sub-module `tools_3d` to support drawing 3D graphics  
新增 `tkintertools` 子模块 `tools_3d` 以支持绘制 3D 图形

## 🔖 `2.6.1`

🕓 *Release Date / 发布日期 : 2023-05-21*

🔵 **Optimized / 优化**

* Enhance the cross platform functionality of the module, which can run on the Windows and Linux platform  
提升模块的跨平台性，可在 Windows 和 Linux 平台上运行

* Optimized reference documentation for classes and functions  
优化了类和函数的参考文档

* Improved module compatibility to Python 3.7  
提升模块兼容性，向下兼容至 Python3.7

* Optimized test files, compatible with different operating systems, and fixed a small number of bugs  
优化了测试文件，兼容不同操作系统，修复少量 bug

* Optimize the methods of the widget checkbox `CheckButton`  
优化控件复选框 `CheckButton` 的各项功能

* The class `Canvas` adds parameters `x` and `y` to reduce redundant code  
类 `Canvas` 新增参数 `x` 和 `y` 以减少多余代码

🟣 **Fixed / 修复**

* Fixed a bug where widgets would misalign after calling the method `moveto`  
修复了控件在调用了方法 `moveto` 后会发生错位的 bug

🔴 **Removed / 移除**

* Remove Unused Constants `SCALE`  
删除无用常量 `SCALE`

## 🔖 `2.6.0`

🕓 *Release Date / 发布日期 : 2023-03-28*

🟢 **Added / 新增**

* New virtual canvas widget check box: `CheckButton`  
新增虚拟画布控件复选框：`CheckButton`

🟣 **Fixed / 修复**

* Solve the bug that the `Text` class `set` and `append` methods will not be updated immediately after use  
解决 `Text` 类 `set`、`append` 方法使用后不会立即更新的 bug

🔵 **Optimized / 优化**

* Optimize the parameters of some classes and functions  
优化部分类和函数的参数

## 🔖 `2.5.12`

🕓 *Release Date / 发布日期 : 2023-03-20*

🟢 **Added / 新增**

* Add a `image` parameter to all widgets to add a background image  
所有控件新增参数 `image` 来添加背景图片

🟣 **Fixed / 修复**

* Fixed a bug where the `move` function cannot move a window  
修复 `move` 函数无法移动窗口的 bug

🔵 **Optimized / 优化**

* Move the binding code of the associated keyboard from class `Tk` to class `Canvas`  
将关联键盘的绑定代码全部由类 `Tk` 移到类 `Canvas` 中

* Optimized some of the code to prevent bugs that shouldn't occur  
优化了部分代码，防止出现一些不应该出现的 bug

🔴 **Removed / 移除**

* Deleted function `font`  
删除了函数 `font`

## 🔖 `2.5.11`

🕓 *Release Date / 发布日期 : 2023-03-13*

🟢 **Added / 新增**

* Class `Canvas` adds parameter `keep` to extend function  
类 `Canvas` 新增参数 `keep` 以扩展功能

* Add the tool function `SetProcessDpiAwareness` to enhance the function  
新增工具函数 `SetProcessDpiAwareness` 以增强功能

* New tool function `font` is added to solve the problem of font size matching DPI level  
新增工具函数 `font` 以解决字体大小适配 DPI 级别的问题

🟣 **Fixed / 修复**

* Fixed the problem of inaccurate Python version requirements. The minimum module operation requirement should be Python 3.11  
修复 Python 版本要求不准确的问题，模块最低运行要求应为 Python3.11

* Fixed the problem that the `configure` method of `_BaseWidget` cannot get the normal effect when modifying the parameter `text` to an empty string  
修复了控件基类 `_BaseWidget` 的方法 `configure` 在将参数 `text` 修改为空字符串时无法得到正常效果的问题

🔵 **Optimized / 优化**

* Optimize the solution to the adaptive DPI problem  
优化解决适配 DPI 问题的方案

* Optimized the way font size fits DPI  
优化了字体大小适配 DPI 的方式

* The canvas widget will be scaled according to the scale of the canvas when it is placed, rather than after it is placed  
画布控件在放置时就会根据画布的缩放而缩放，而不是在放置后才进行缩放

## 🔖 `2.5.10`

🕓 *Release Date / 发布日期 : 2023-02-04*

🟢 **Added / 新增**

* Canvas virtual widget base class `_BaseWidget` Add instance attribute `command_ex` to extend functions  
画布虚拟控件基类 `_BaseWidget` 新增实例属性 `command_ex` 以扩展功能

* Function `move` adds parameter `end` to enhance function  
函数 `move` 新增参数 `end` 以增强功能

* New method of canvas virtual widget base class `moveto`  
画布虚拟控件基类新增方法 `moveto`

🟣 **Fixed / 修复**

* Fixed the bug that the class `Tk` cannot make the distance between the window and the screen 0  
修复了类 `Tk` 无法使窗口与屏幕距离为 0 的 bug

* Fixed the bug that the parameter `borderwidth` of the widget is invalid when it has rounded corners  
修复了控件在有圆角状态下参数 `borderwidth` 失效的 bug

🟡 **Changed / 变更**

* The initialization parameters of `Tk` class and `Toplevel` class have become more concise  
`Tk` 类和 `Toplevel` 类的初始化参数变得更加简洁了

🔵 **Optimized / 优化**

* The state change of the canvas virtual widget adds a previous state detection, greatly improving performance  
画布虚拟控件的状态改变加了个先前状态检测，大幅提高性能

* The performance of function `move` has been optimized  
函数 `move` 的性能得到了优化

## 🔖 `2.5.9`

🕓 *Release Date / 发布日期 : 2023-01-13*

🟢 **Added / 新增**

* Class `PhotoImage` new method `stop` is used to stop the playback of moving pictures  
类 `PhotoImage` 新增方法 `stop` 用于停止动图的播放

🟣 **Fixed / 修复**

* Fixed an incomplete parameter bug in the `moveto` method of the `Canvas` class  
修复 `Canvas` 类的方法 `moveto` 在参数上不完备的 bug

* Fixed a bug that sometimes causes multiple widgets to touch at the same time  
修复了有时候会产生多个控件同时触碰的 bug

* Fixed parameter error of class `PhotoImage`  
修复了类 `PhotoImage` 的参数错误

🔵 **Optimized / 优化**

* Optimize codes, simplify some codes and delete redundant parts  
优化代码，简化部分代码，删去冗余部分

🔴 **Removed / 移除**

* The redundant parameters `minsize` and `alpha` of the `Tk` and `Toplevel` classes have been deleted  
删除了 `Tk` 类和 `Toplevel` 类的冗余参数 `minsize` 和 `alpha`

## 🔖 `2.5.8`

🕓 *Release Date / 发布日期 : 2023-01-12*

🟣 **Fixed / 修复**

* Fixed a bug that the function `move` cannot perform the default move mode `flat`  
修复了函数 `move` 无法进行默认的移动模式 `flat` 的 bug

* Solve the bug that the cursor will flash faster and faster after pasting text for text widget  
解决文本类控件在粘贴文本后光标会越闪越快的 bug

🔵 **Optimized / 优化**

* `move` function has been optimized to improve applicability, accuracy and speed  
优化了 `move` 函数，提升了适用性、精度以及速度

* `Canvas` class adds compatibility methods `coords`, `move`, `moveto` and `bbox` to improve the DPI adaptation problem  
`Canvas` 类新增兼容方法 `coords`、`move`、`moveto` 和 `bbox`，完善了 DPI 的适配问题

* `Tk` Class Add Method `wm_minsize`, `wm_maxsize` to be compatible with DPI adaptation problems  
`Tk` 类新增方法 `wm_minsize`、`wm_maxsize` 以兼容 DPI 适配问题

* Optimize the `PhotoImage` class so that it can be used without globalization  
优化 `PhotoImage` 类，使之无需全局化，即可使用

* Overall optimization of code and reduction of code volume  
总体优化了代码，减少了代码量

## 🔖 `2.5.7`

🕓 *Release Date / 发布日期 : 2023-01-10*

🟢 **Added / 新增**

* The `move` function adds the parameter `frames`, which can change the number of frames of the animation when moving  
`move` 函数新增参数 `frames`，可改变移动时的动画的帧数

* `Tk` class adds the adaptation function to screen DPI, which can make the window clearer  
`Tk` 类新增对屏幕 DPI 的适配功能，可使窗口更加清晰

* New compatible version and compatible version conversion file  
新增兼容版本以及兼容版本转换文件

🟡 **Changed / 变更**

* Change the function names of functions `move_widget`, `correct_text` and `change_color` to `move`, `text` and `color` respectively  
分别将函数 `move_widget`、`correct_text` 和 `change_color` 的函数名变更为 `move`、`text` 和 `color`

* Corrected some parameters  
修正了些许参数

* Increase the default frame rate parameter of the move function to 30  
提高了移动函数的默认帧率参数至 30

🔵 **Optimized / 优化**

* Optimized the code structure of the `color` function and the `move` function to make it more concise  
优化了 `color` 函数和 `move` 函数的代码结构，使其更加简洁

## 🔖 `2.5.6`

🕓 *Release Date / 发布日期 : 2022-12-12*

🟣 **Fixed / 修复**

* Fixed the bug that the singleton mode class (`Singleton`) could not pass parameters during initialization  
修复了单例模式类（`Singleton`）在初始化时无法传递参数的 bug

* Fixed the bug that sometimes the font parameters of `_CanvasItemId` could not be found when scaling fonts in `Canvas` class  
修复 `Canvas` 类在缩放字体时，有时会找不到 `_CanvasItemId` 的字体参数的 bug

🟡 **Changed / 变更**

* The zoom method of the picture is changed from absolute zoom to relative absolute zoom  
图片的缩放方式由绝对缩放变更为相对的绝对缩放方式

🔵 **Optimized / 优化**

* Optimized the structure of the `PhotoImage` class  
优化了 `PhotoImage` 类的结构

* All useless codes (TODO marked) are deleted  
删除了所有无用的代码（TODO 标记的）

* The `fractions` module is introduced to improve the precision of image scaling and reduce the operation time  
引入了 fractions 模块并提高了图片缩放时的精度且减少了运算时间

🔴 **Removed / 移除**

* `Canvas` class deletes two redundant and overridden instance methods: `create_ bitmap` and `create_ window`  
`Canvas` 类删除了两个冗余的、重写的实例方法：`create_bitmap` 和 `create_window`

## 🔖 `2.5.5`

🕓 *Release Date / 发布日期 : 2022-12-11*

🟢 **Added / 新增**

* Added type prompt `Self` for the `self` parameter of instance methods of all classes  
为所有类的实例方法的 `self` 参数添加了类型提示 `Self`

🟣 **Fixed / 修复**

* Fixed the bug that the width and height will not change in some cases when scaling `Canvas` classes  
修复 `Canvas` 类缩放时，宽高在某些情况下不会改变的 bug

🟡 **Changed / 变更**

* Modified the access method of `Tk` class, `Toplevel` class and `Canvas` class protection attributes  
修改了 `Tk` 类、`Toplevel` 类、`Canvas` 类的保护属性的获取方式

* Greatly modified the canvas scaling mechanism, fully adapted to all situations, and accelerated the scaling speed  
大幅度地修改了画布缩放的机制，完全适应所有情况，并加快了缩放速度

🔵 **Optimized / 优化**

* Optimize the structure of all multiple loops and judgment statements, making the code more beautiful  
优化了所有多重循环加判断语句的结构，使代码更为美观

## 🔖 `2.5.4`

🕓 *Release Date / 发布日期 : 2022-12-08*

🟢 **Added / 新增**

* A new widget has been added: progress bar(`Progressbar`)  
增加了一个新的控件：进度条（`Progressbar`）

🟣 **Fixed / 修复**

* Fixed the bug that the screen size would be abnormal when creating `Canvas` of different sizes  
修复了新建不同大小的 `Canvas` 时，画面大小会异常的 bug

* Solved the bug that there is no change when the font size is scaled under certain conditions  
解决了字体大小进行缩放时，在某种条件下缩小没有变化的 bug

* Solved the bug that function `move_widget` cannot move `tkinter._CanvasItemId`  
解决了函数 `move_widget` 无法移动 `tkinter._CanvasItemId` 的 bug

🟡 **Changed / 变更**

* The binding mechanism of associated events has been modified so that `Canvas` classes can be created at any time  
修改了关联事件的绑定机制，使得 `Canvas` 类可以被随时创建

🔵 **Optimized / 优化**

* Some colors are beautified  
美化了部分颜色

* Optimized some codes in function `move_widget`  
优化了函数 `move_widget` 中的部分代码

## 🔖 `2.5.3`

🕓 *Release Date / 发布日期 : 2022-11-27*

🟢 **Added / 新增**

* Added singleton pattern(`Singleton`) class for inheritance  
增加了单例模式类（`Singleton`）供继承

* Add some methods (attributes) of `Tk`, `Toplevel` and `Canvas` to access some attributes that should not be directly accessed  
增加 `Tk`、`Toplevel`、`Canvas` 的一些方法(属性)来访问一些不应该被直接访问的属性

🟣 **Fixed / 修复**

* Solved the bug that the `destroy` method of the widget can only delete half of the widgets when traversing  
解决了控件的 `destroy` 方法在遍历使用时只能删除一半控件的 bug

🔵 **Optimized / 优化**

* `Canvas` class overrides `destroy` method to be compatible with the original `destroy` method  
`Canvas` 类重写 `destroy` 方法以兼容原 `destroy` 方法

* `Toplevel` class overrides `destroy` method to be compatible with the original `destroy` method  
`Toplevel` 类重写 `destroy` 方法以兼容原 `destroy` 方法

* Some codes of `Tk` and `Toplevel` are optimized, and the code amount of `Toplevel` widgets is greatly reduced  
优化了 `Tk`、`Toplevel` 的部分代码，`Toplevel` 控件的代码量大大缩减

🔴 **Removed / 移除**

* The `proportion_lock` parameter and its function of `Tk` and `Toplevel` are deleted  
删除了 `Tk`、`Toplevel` 的 `proportion_lock` 参数及其功能

## 🔖 `2.5.2`

🕓 *Release Date / 发布日期 : 2022-11-25*

🟢 **Added / 新增**

* Added mouse style for text type virtual widget  
添加了对文本类虚拟控件的鼠标样式

🟣 **Fixed / 修复**

* Solved the bug that the `set` and `append` methods of text virtual widgets may fail in some cases  
解决了文本类虚拟控件 `set`、`append` 方法某些时候会失效的 bug

* Solved the bug that the mouse style flickers when the mouse cursor moves over the button  
解决了鼠标光标移动到按钮上时的鼠标样式会闪烁的 bug

* Fixed the bug that the `read` parameter of the text box widget failed  
修复了文本框控件 `read` 参数失效的 bug

🔵 **Optimized / 优化**

* Change the mouse position detection order to further improve the running speed  
改变鼠标位置检测顺序，进一步提升运行速度

## 🔖 `2.5.1`

🕓 *Release Date / 发布日期 : 2022-11-23*

🟢 **Added / 新增**

* Added mouse style for button virtual widgets  
添加了对按钮虚拟控件的鼠标样式

🟣 **Fixed / 修复**

* Solved the bug that the input prompt position was not aligned after the input box was enlarged  
解决了输入框放大后输入提示符位置没对齐的 bug

* Solved the bug that text virtual widgets will lose focus after being pasted once  
解决了文本类虚拟控件粘贴一次后会失去焦点的 bug

* Fix a few errors in the module documentation  
修复模块文档中的少许错误

🟡 **Changed / 变更**

* Modified the mouse position determination mechanism and improved the running speed  
修改了鼠标位置判定机制，同时提升运行速度

🔵 **Optimized / 优化**

* Some redundant codes are deleted to improve the overall running speed  
删除了部分冗余代码，提升总体运行速度

## 📑 Older Logs / 旧日志

| Version / 版本 | Release Date / 发布日期 |                              Description / 描述                              |
| :------------: | :---------------------: | :--------------------------------------------------------------------------: |
|    `2.5.0`     |       2022-11-21        |               Upload the package to PyPI 🚀<br/>上传包到 PyPI 🚀               |
|    `2.4.15`    |       2022-11-18        | Drew and uploaded the first version of the logo<br/>绘制并上传了第一版的图标 |
|    `2.4.14`    |       2022-11-14        |                                                                              |
|    `2.4.11`    |       2022-11-13        |                                                                              |
|    `2.4.10`    |       2022-11-10        |                                                                              |
|    `2.4.2`     |       2022-11-05        |                                                                              |
|    `2.4.1`     |       2022-11-03        |                                                                              |
|    `2.4.0`     |       2022-11-02        |                                                                              |
|    `2.3.5`     |       2022-11-01        |                                                                              |
|    `2.3.1`     |       2022-10-25        |   Added project license (MulanPSL-2)<br/>添加了项目开源许可（MulanPSL-2）    |
|    `2.3.0`     |       2022-10-22        |                                                                              |
|    `2.2.4`     |       2022-10-20        |                                                                              |
|     `2.2`      |       2022-10-19        |                                                                              |
|     `1.4`      |       2022-09-21        |                                                                              |
|     `1.3`      |       2022-09-20        |                                                                              |
|     `1.0`      |       2022-09-10        |       The repository was created and uploaded 🎉<br/>创建并上传了仓库 🎉       |
|     `0.2`      |       2022-08-29        |               Modularize codes gradually<br/>逐渐模块化了代码                |
|     `0.1`      |       2022-07-23        |                  Where the dream begins!<br/>梦开始的地方！                  |
