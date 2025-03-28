#一.异常处理
#   基本语法
'''
try：
	可能发生错误的代码
except[异常 as 别名:]：
	如果出现异常，执行的代码
[else:]         []表示可选
	未出现异常时执行的代码
[finally:]
	不管有没有异常都会执行
'''


# 1.异常捕获完整语法
try:
    result = 10/0
except(ZeroDivisionError,ValueError) as e:  # 捕获特定异常
    print(f"数学运算错误:{e}")
except Exception as e:  # 兜底异常捕获
    print(f"未知错误:{e}")
else:
    print("未发生异常时执行")
finally:
    print("无论是否异常都执行")
# result = 10/0

# 2.异常的传递
"""
演示异常的传递性
"""

#定义一个出现异常的方法
def func1():
    print( "func1开始执行")
    num = 1 / 0  #肯定有异常，除以0的异常
    print( "func1结束执行")
#定义一个无异常的方法调用上面的方法
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")
#定义一个方法，调用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常,异常信息是{e}")
main()



#二.模块
#   模块的导入方式
# [from 模块名] import [模块|类|变量|函数|*][as 别名]
# 常用的组合形式如：
# import 模块名
# from 模块名 import 类、变量、方法等
# from 模块名 import *
# import 模块名 as 别名
# from 模块名 import 功能名 as 别名

"""
演示Python的模块导入
"""

#使用import导入time模块使用sleep功能（函数)
import time #导入Python 内置的time模块(time.py这个代码文件>
print("你好")
time.sleep(3)#通过.就可以使用模块内部的全部功能（类、函数、变量）
print("我好")
#使用于from导入time的sleep功能(函数)
from time import sleep
print("你好")
sleep(1)
print("我好")
#使用*导入time模块的全部功能
from time import * #*表示全部
print("你好")
sleep(1)
print("我好")
#使用as给特定功能加上别名
from time import sleep as sl
print("你好")
sl(1)
print("我好")

# from可以省略，直接import即可
#
# as别名可以省略
#
# 通过" . "来确定层级关系
#
# 模块的导入一般写在代码文件的开头位置

#自定义模块...
#  a._main_变量的功能是?
# if _name_== “_main_”表示，只有当程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入
#
#  b.不同模块，同名的功能，如果都被导入，那么后导入的会覆盖先导入的
#
#  c._all_变帚可以控制import*的时候哪些功能可以被导入



#三.python包
# 包含__init__.py文件（可为空）
# 推荐加入__all__变量指定可导入子模块

#第三方包管理命令
# 操作	命令
# 安装包	pip install requests
# 指定镜像源安装	pip install -i https://pypi.tuna.tsinghua.edu.cn/simple package
# 导出依赖	pip freeze > requirements.txt
# 安装项目依赖	pip install -r requirements.txt










