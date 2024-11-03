from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import logging

#更改控制台名称
import platform
os_name = platform.system()
if os_name == "Windows":
    import ctypes
    kernel32 = ctypes.WinDLL('kernel32')
    hWnd = kernel32.GetConsoleWindow()
    kernel32.SetConsoleTitleW("提示窗口")
elif os_name == "Darwin":
    import subprocess
    new_title = "提示窗口"
    applescript = f'tell application "Terminal" to set custom title of front window to "{new_title}"'
    subprocess.call(["osascript", "-e", applescript])
else:
    print('抱歉，您的操作系统不支持运行Music！(1)')
    exit(1)

主窗口 = Tk()

print('加载中')
# 定义主窗口的内容
菜单按钮1 = Button(主窗口)
菜单按钮1["text"] = '新建'  # 新建按钮
菜单按钮1.pack()
菜单按钮2 = Button(主窗口)
菜单按钮2["text"] = '导入'  # 新建按钮
菜单按钮2.pack()
主窗口.title("Music功能菜单") # 设置标题

print('请勿关闭该窗口！否则程序将关闭！')




# 封装重复的函数
def OpenpythonFile(file_path):
    编辑窗口 = Tk()

    # 定义编辑窗口的内容
    插入Print = Button(编辑窗口)
    插入Print.pack()
    插入Print["text"] = '显示文本'
    插入int = Button(编辑窗口)
    插入int.pack()
    插入变量 = Button(编辑窗口)
    插入变量.pack()
    主窗口.title("Music控件")

    # 定义事件
    def importprint():
        code = simpledialog.askstring("Music", "请在这里输入你要显示的文字/变量：（如果是文本请把文本用引号括起来！）")
        with open(file_path, 'w') as file:
            file.write(f'print({code}) # 在窗口显示{code}（由Music生成）')
    def importint():
        code = simpledialog.askstring("Music", "请在这里输入你要转换成数字的文本/变量：（如果是文本请把文本用引号括起来！）")
        with open(file_path, 'w') as file:
            file.write(f'print({code}) # 在窗口显示{code}')
    def importstr():
        name = simpledialog.askstring("Music", "请在这里输入变量的名称：")
        code = simpledialog.askstring("Music", "请在这里输入你要显示的文字：")
        with open(file_path, 'w') as file:
            file.write(f'{name} = {code} # 代码由Music生成！')
    
    # 绑定事件 
    


# 写出事件并绑定
def newfile(e):  # 创建新建文件的事件
    messagebox.showinfo("message", "请输入正确的文件路径！")
    file_path = simpledialog.askstring("输入文件路径", "请在这里输入文件路径：")
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write('''# 代码由Music生成！''')
        except OSError as e:
            messagebox.showerror("错误", f"无法打开或写入文件，请在搜索引擎查询此字段：{e}")
        OpenpythonFile(file_path)

def importfile(e):  # 创建导入文件的事件
    messagebox.showinfo("message", "请输入正确的文件路径！")
    file_path = simpledialog.askstring("输入文件路径", "请在这里输入文件路径：")
    if file_path:
        try:
            with open(file_path, 'w') as file:
                pass
        except OSError as e:
            messagebox.showerror("错误", f"无法打开或写入文件，请在搜索引擎查询此字段：{e}")
        OpenpythonFile(file_path)

# 使用bind方法绑定鼠标左键点击事件
菜单按钮1.bind("<Button-1>", newfile)
菜单按钮2.bind("<Button-1>", importfile)

主窗口.mainloop()
