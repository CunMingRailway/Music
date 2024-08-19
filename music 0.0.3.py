#初始化
import os
import threading
import subprocess
import logging
age = ' '
print('访问 bilibili.com ，了解最新的Music版本和更新！')
print('Music v0.0.3 键入Help 获取帮助...')
print('Copyright © 2024 chenshuda artroom. All rights reserved.')
#循环判断用户输入的语句
while True:  
    print('>>>')
    a = input()
    #使用if else 语句做出判断和反应
    if a == 'help':
        print('1. 显示：在窗口显示文本')
        print('2. 获取输入：在窗口请求文本')
        print('3. 创建变量：创建一个新变量')
        print('4. 加运算：将两个数的加运算结果显示在屏幕上')
        print('5. 减运算：将两个数的减运算结果显示在屏幕上')
        print('6. 乘运算：将两个数的乘运算结果显示在屏幕上')
        print('7. 除运算：将两个数的除于运算结果显示在屏幕上')
        print('8. 整运算：将两个数的整除运算结果显示在屏幕上')
        print('9. 取运算：将两个数的取余运算结果显示在屏幕上')
        print('10. 取变：使用一个变量的值运行其他命令')
        print('11. 关于：显示你当前的Music版本信息及声明')
        print('12. 跳出环境：回到上一层的命令运行环境')
        print('13.退出Music: 退出Music中文模拟终端')
        print('14. 新建循环：以一定次数循环执行其他命令')
        print('15. 整化：将一个以字符串类型储存的数字转化为数字类型')
        print('想获取更多帮助？请查看Music的官方帮助文档！')
    elif a == '显示：':
        code = input()
        print(code)
    
    elif a == '获取输入：':
        shuru = input()
        print(shuru)
    elif a == '创建变量：':
        name = input()
        age = input()
    elif a == '加运算：':
        jia1 = input()
        jia2 = input()
        
        jia1 = int(jia1)
        jia2 = int(jia2)
        print(jia1 + jia2)

    elif a == '减运算：':
        jian1 = input()
        jian2 = input()
        
        jian1 = int(jian1)
        jian2 = int(jian2)
        print(jian1 - jian2)
    
    elif a == '乘运算：':      
        cheng1 = input()
        cheng2 = input()
        
        cheng1 = int(cheng1)
        cheng2 = int(cheng2)
        print(cheng1 * cheng2)
    elif a == '除运算：':
        chu1 = input()
        chu2 = input()
        
        chu1 = int(chu1)
        chu2 = int(chu2)
        print(chu1 / chu2)
    elif a == '取运算：':
        qv1 = input()
        qv2 = input()
        
        qv1 = int(qv1)
        qv2 = int(qv2)
        print(qv1 % qv2)
    elif a == '整运算：':
        zheng1 = input()
        zheng2 = input()

        zheng1 = int(zheng1)
        zheng2 = int(zheng2)
        print(zheng1 // zheng2)
    elif a == '取变：':
        #在取变环境下判断语句
        print('切换到新环境......')
        if age == ' ':
            logging.error('There is no value assigned to the variable!')
            break
        while True:  
            print('>>>>')
            a = input()
            if a == 'help-取':
                print('1. 显示：在窗口显示文本')
                print('4. 加运算：将两个数的加运算结果显示在屏幕上')
                print('5. 减运算：将两个数的减运算结果显示在屏幕上')
                print('6. 乘运算：将两个数的乘运算结果显示在屏幕上')
                print('7. 除运算：将两个数的除于运算结果显示在屏幕上')
                print('8. 整运算：将两个数的整除运算结果显示在屏幕上')
                print('9. 取运算：将两个数的取余运算结果显示在屏幕上')
                print('15. 整化：将一个以字符串类型储存的数字转化为数字类型并储存在变量中')
                print('注意：在该环境下运行运算命令，会导致变量的值从字符串变成数字类型！')
            elif a == '显示：':
                    print(age)
            elif a == '加运算：':
                if str.isdigit(age) == True: 
                    
                    jia2 = input()
        
                    age = int(age)
                    jia2 = int(jia2)
                    print(age + jia2)
                else:
                    logging.critical('The value of a variable is not an integer!')
                    break
            elif a == '减运算：':
                if str.isdigit(age) == True:    
                    jian2 = input()
        
                    age = int(age)
                    jian2 = int(jian2)
                    print(age - jian2)
                else:
                    logging.critical('The value of a variable is not an integer!')
                    break
            elif a == '乘运算：':      
                if str.isdigit(age) == True:    
                    cheng2 = input()
        
                    age = int(age)
                    cheng2 = int(cheng2)
                    print(age * cheng2)
                else:
                    logging.critical('The value of a variable is not an integer!')
                    break
            elif a == '除运算：':
                if str.isdigit(age) == True:   
                    chu2 = input()
        
                    age = int(age)
                    chu2 = int(chu2)
                    print(age / chu2)
                else:
                    logging.critical('The value of a variable is not an integer!')
                    break
            elif a == '取运算：':
                if str.isdigit(age) == True:       
                    qv2 = input()
        
                    age = int(age)
                    qv2 = int(qv2)
                    print(age % qv2)
                else:
                    logging.critical('The value of a variable is not an integer!')
                    break
            elif a == '整运算：':
                if str.isdigit(age) == True:       
                    qv2 = input()
                    zheng2 = input()

                    age = int(age)
                    zheng2 = int(zheng2)
                    print(age // zheng2)
                else:
                    logging.critical('The value of a variable is not an integer!')
                    break
            elif a == '跳出环境':
                 print('返回......')
                 break
            
            elif a == '整化：':
                age = int(age)

            else:
                print(a + '  不是在取变量环境下可执行的命令，请键入 Help-取 查看该环境所支持的命令。')
    elif a == '关于':
        print('Music v0.0.2是一个基于Python的模拟中文终端，能在中文的输入环境下运行命令')  
        print('内部版本：bu0002')
        print('作者：陈殊达美术工作室')
        print('著作权信息：Copyright © 2024 chenshuda artroom. All rights reserved.')          
    elif a == '跳出环境':
        print('当前没有进入新的运行环境')
    elif a == '退出Music':
        print('再见！')
        TimeoutError(1)
        break
    elif a == '新建循环：':
        #环境初始化
        a2 = input()
        print('进入新环境......')
        a2 = int(a2)
        while True:  
            print('>>>>')
            a = input()
            #使用 if-else语句检测并执行命令
            if a == 'help':
                print('1. 显示：在窗口显示文本')
                print('2. 获取输入：在窗口请求文本')
                print('3. 创建变量：创建一个新变量')
                print('4. 加运算：将两个数的加运算结果显示在屏幕上')
                print('5. 减运算：将两个数的减运算结果显示在屏幕上')
                print('6. 乘运算：将两个数的乘运算结果显示在屏幕上')
                print('7. 除运算：将两个数的除于运算结果显示在屏幕上')
                print('8. 整运算：将两个数的整除运算结果显示在屏幕上')
                print('9. 取运算：将两个数的取余运算结果显示在屏幕上')
            elif a == '显示：':
                for i in range (a2):    
                    code = input()
                    print(code)
    
            elif a == '获取输入：':
                for i in range(a2):
                    shuru = input()
                    print(shuru)
            elif a == '创建变量：':
                for i in range(a2):
                    name = input()
                    age = input()
            elif a == '加运算：':
                for i in range(a2):    
                    jia1 = input()
                    jia2 = input()
        
                    jia1 = int(jia1)
                    jia2 = int(jia2)
                    print(jia1 + jia2)
            elif a == '减运算：':
                for i in range(a2):    
                    jian1 = input()
                    jian2 = input()
        
                    jian1 = int(jian1)
                    jian2 = int(jian2)
                    print(jian1 - jian2)
     
            elif a == '乘运算：':      
                for i in range(a2):
                    cheng1 = input()
                    cheng2 = input()
        
                    cheng1 = int(cheng1)
                    cheng2 = int(cheng2)
                    print(cheng1 * cheng2)
            elif a == '除运算：':
                for i in range(a2):
                    chu1 = input()
                    chu2 = input()
        
                    chu1 = int(chu1)
                    chu2 = int(chu2)
                    print(chu1 / chu2)
            elif a == '取运算：':
                for i in range(a2):
                    qv1 = input()
                    qv2 = input()
        
                    qv1 = int(qv1)
                    qv2 = int(qv2)
                    print(qv1 % qv2)
            elif a == '整运算：':
                for i in range(a2):    
                    zheng1 = input()
                    zheng2 = input()

                    zheng1 = int(zheng1)
                    zheng2 = int(zheng2)
                    print(zheng1 // zheng2)
            elif a == '退出循环':
                print('退出......')
                break
            else:
                print('  不是可执行的命令，请键入 Help 查看所有支持的命令。')
    elif a == '整化：':
        shuru = input()
        int(shuru)
#提示输入错误
    else:
        print(a + '  不是可执行的命令，请键入 Help 查看所有支持的命令。')
    
        

    