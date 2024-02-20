"""Internal Module: Some utility functions"""


import typing

try:
    import winreg
except ImportError:
    winreg = None


def get_control_lst(
    controller: tuple[typing.Callable[[float], float], float, float],
    length: int,
) -> list[float]:
    """Get a list of floating-point numbers generated by a control function"""
    delta = controller[2] - controller[1]
    lst = [controller[0](controller[1] + i/length*delta)
           for i in range(1, length+1)]
    if (maximum := max(lst)) == 0:
        return [controller[0](controller[1])] * length
    return [value/maximum for value in lst]


def is_dark() -> bool | None:
    """Determine whether the operating system is a dark theme"""
    if winreg is None:
        return None
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize")
        return not winreg.QueryValueEx(key, "AppsUseLightTheme")[0]
    except FileNotFoundError:
        return None


def info(value: str) -> None:
    """Output a piece of information"""
    print(f"\033[36mInfo: {value}\033[0m")


def warning(value: str) -> None:
    """Output a warning"""
    print(f"\033[33mWarning: {value}\033[0m")


def error(value: str) -> None:
    """Output an error"""
    print(f"\033[31mError: {value}\033[0m")


# class Animation:
#     """动画"""

#     def __init__(
#         self,
#         widget,  # type: BaseWidget | tkinter.BaseWidget | int
#         ms,  # type: int
#         *,
#         controller=constants.CONTROLLER,
#         # type: tuple[typing.Callable[[float], float], float, float] | None
#         translation=None,  # type: tuple[float, float] | None
#         fps=constants.FPS,  # type: int
#         start=None,  # type: typing.Callable | None
#         step=None,  # type: typing.Callable | None
#         stop=None,  # type: typing.Callable | None
#         callback=None,  # type: typing.Callable[[float]] | None
#         canvas=None,  # type: tkinter.Canvas | None
#         loop=False,  # type: bool
#     ):  # type: (...) -> None
#         """
#         * `widget`: 进行动画的控件
#         * `ms`: 动画总时长（单位：毫秒）
#         * `controller`: 控制器，为元组 (控制函数, 起始值, 终止值) 的形式
#         * `translation`: 移动，x 方向位移，y 方向位移
#         * `fps`: 每秒帧数
#         * `start`: 动画开始前执行的函数
#         * `step`: 动画每一帧结束后执行的函数（包括开始和结束）
#         * `stop`: 动画结束后执行的函数
#         * `callback`: 回调函数，每一帧调用一次，传入参数为单帧占比
#         * `canvas`: 当 `widget` 是画布中的绘制对象时，应指定 `canvas`
#         * `loop`: 是否循环播放动画，默认不循环，循环时参数 `stop` 失效
#         """
#         self.widget = widget
#         self.master = canvas if isinstance(widget, int) else widget if isinstance(
#             widget, tkinter.Misc) else widget.master
#         self.start = start
#         self.step = step
#         self.stop = stop
#         self.loop = loop
#         self.translation = translation
#         self.sec = 1000 // fps  # 单帧间隔时间
#         self.count = ms * fps // 1000  # 总帧数
#         if self.count == 0:
#             self.count = 1  # 至少一帧
#         self.callback = callback
#         if controller is None:
#             controller = (lambda _: _), 0, 1
#         self.rate_lst = _get_control_lst(controller, self.count)
#         self.animation = ""  # 动画命令

#     def _run(self, _ind=0, _last_data=(0, 0)):
#         # type: (int, tuple[int, int]) -> None
#         """执行动画"""
#         if _ind == self.count:
#             if self.loop:
#                 return self._run()  # 循环播放动画
#             return None if self.stop is None else self.stop()

#         if self.translation is not None:
#             data = tuple(
#                 round(value * self.rate_lst[_ind]) for value in self.translation)
#             dx, dy = data[0] - _last_data[0], data[1] - _last_data[1]
#             self._translate(dx, dy)
#         else:
#             data = 0, 0

#         self.animation = self.master.after(self.sec, self._run, _ind+1, data)

#         if self.step is not None:
#             self.step()
#         if self.callback is not None:
#             self.callback(self.rate_lst[_ind])

#         return None

#     def _translate(self, dx, dy):  # type: (int, int) -> None
#         """平移"""
#         if isinstance(self.widget, (tkinter.Tk, tkinter.Toplevel)):  # 窗口
#             size, x, y = self.widget.geometry().split("+")
#             self.widget.geometry(f"{size}+{int(x) + dx}+{int(y) + dy}")
#         elif isinstance(self.widget, tkinter.Widget):  # tkinter 控件
#             place_info = self.widget.place_info()
#             origin_x, origin_y = float(place_info["x"]), float(place_info["y"])
#             self.widget.place(x=origin_x + dx, y=origin_y + dy)
#         elif isinstance(self.widget, BaseWidget):  # tkt 控件
#             self.widget.move(dx, dy)
#         elif isinstance(self.widget, int):  # int
#             self.master.move(self.widget, dx, dy)

#     def run(self):  # type: () -> None
#         """运行动画"""
#         if self.start is not None:
#             self.start()
#         self._run()

#     def shutdown(self):  # type: () -> None
#         """终止动画"""
#         if self.animation != "":
#             self.master.after_cancel(self.animation)
