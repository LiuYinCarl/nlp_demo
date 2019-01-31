import win32com
from win32com.client import Dispatch, constants


def start_app(app, filepath):
    print(filepath)
    # w = win32com.client.Dispatch('Word.Application')
    # 或者使用下面的方法，使用启动独立的进程：
    w = win32com.client.DispatchEx('Word.Application')
    # w = win32com.client.DispatchEx(app)

    # 前台运行，显示，不警告
    w.Visible = True
    w.DisplayAlerts = False

    # 打开新的文件
    doc = w.Documents.Open(FileName=filepath)
