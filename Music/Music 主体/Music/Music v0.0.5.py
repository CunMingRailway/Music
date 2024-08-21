# 初始化  
from ast import main
import logging
import os

from distutils.cmd import Command   # type: ignore
age = ' '  
#根据文件内容执行操作
def execute_mpf_command(command, line):  
    if command == '显示：':
        code = input()
        print(code)
    
    elif command == '获取输入：':
        shuru = input()
        print(shuru)
    elif command == '创建变量：':
        global variables  
        name = execute_mpf_command(command, line + 1)
        value = execute_mpf_command(command, line + 2)  
        variables[name] = value  
        print(f"变量 {name} 已创建，其值为 {value}。")
    elif command == '加运算：':
        jia1 = input()
        jia2 = input()
        
        jia1 = int(jia1)
        jia2 = int(jia2)
        print(jia1 + jia2)

    elif command == '减运算：':
        jian1 = input()
        jian2 = input()
        
        jian1 = int(jian1)
        jian2 = int(jian2)
        print(jian1 - jian2)
    
    elif command == '乘运算：':      
        cheng1 = input()
        cheng2 = input()
        
        cheng1 = int(cheng1)
        cheng2 = int(cheng2)
        print(cheng1 * cheng2)
    elif command == '除运算：':
        chu1 = input()
        chu2 = input()
        
        chu1 = int(chu1)
        chu2 = int(chu2)
        print(chu1 / chu2)
    elif command == '取运算：':
        qv1 = input()
        qv2 = input()
        
        qv1 = int(qv1)
        qv2 = int(qv2)
        print(qv1 % qv2)
    elif command == '整运算：':
        zheng1 = input()
        zheng2 = input()

        zheng1 = int(zheng1)
        zheng2 = int(zheng2)
        print(zheng1 // zheng2)
    elif command == '关于':
        print('Music v0.0.4是一个基于Python的模拟中文终端，能在中文的输入环境下运行命令')  
        print('内部版本：bu0004')
        print('作者：陈殊达美术工作室')
        print('著作权信息：Copyright © 2024 chenshuda artroom. All rights reserved.')          
    elif command == '跳出环境':
        print('当前没有进入新的运行环境')
    elif command == '整化：':
        shuru = input()
        int(shuru)
#提示有位置的命令
    else:  
        print(f"未知命令：{command}")  
  
def read_and_execute_mpf_file(filename):  
    """读取并执行.mpf文件中的命令"""  
    try:  
        with open(filename, 'r', encoding='utf-8') as file:  
            command = None  
            for line in file:  
                line = line.strip()  
                if line == '-':  
                    if command:  
                        execute_mpf_command(command, '')  # 对于仅命令无值的情况  
                        command = None  
                elif line:  
                    if ':' in line:  
                        command, _ = line.split(':', 1)  
                        command = command.strip()  
                    else:  
                        if command:  
                            execute_mpf_command(command, line)  
    except FileNotFoundError:  
        print(f"文件 {filename} 未找到。")  
    except Exception as e:  
        print(f"读取或执行文件时发生错误：{e}")  
  
# 主程序  
if __name__ == "__main__":  
    print('欢迎使用Music MPF命令执行器')  
    filename = input("请输入要执行的.mpf文件名（包括路径）：")  
    read_and_execute_mpf_file(filename)