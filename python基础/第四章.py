#一.函数初体验
name = 'itheima'
length = len(name)
print(length)


#二.基础函数定义与调用
# 1. 无参数、无返回值函数
#   定义函数:打印欢迎信息
def greet():
    print("欢迎光临!")

greet() #调用函数

# 2. 带参数的函数
#   定义函数:计算两数之和
def add(x, y):
    result = x + y
    return result

print(add(1, 2))


#三.返回值与None类型
# 1.返回多个值
def calculate(a, b):
    return a + b, a - b, a * b  # 返回元组

add, sub, mul = calculate(10, 5)
print(f"加: {add}, 减: {sub}, 乘: {mul}")  # 输出: 加: 15, 减: 5, 乘: 50

# # 2. 无返回值的函数默认返回None
# def no_return():
#     print("此函数没有return语句")
#
# result = no_return()
# print(result)

# 3. 主动返回None
def check_even(num):
    """
    检查一个数字是否为偶数。

    参数:
        num (int): 要检查的数字。

    返回值:
        bool or None: 如果数字是偶数，返回 True；如果不是偶数，返回 None。

    """
    if num % 2 == 0:
        return True
    else:
        return None  # 显式返回None

print(check_even(7))  # 输出: None





#四.函数说明文档
def power(base, exponent):
    """
    计算一个数的幂
    :param base: 基数(整数或浮点数)
    :param exponent: 指数(整数)
    :return: base**exponent  base的exponent次幂(整数或浮点数)
    """
    return base ** exponent

# 查看说明文档
help(power)    #显示定义的注释


#五.嵌套调用与作用域
# 1.函数嵌套调用
def print_header():
    print("====== 系统菜单 ======")

def print_menu():
    print_header()  #嵌套调用
    print("1.查询余额")
    print("2.退出系统")

print_menu()

# 2.局部变量 vs 全局变量
total = 100 #全局变量

def update_total():
    global total    #声明使用全局变量
    total += 50
    local_var = "临时变量"  #局部变量,外部无法访问

update_total()
print(total)  # 输出: 150
# print(local_var)  # 报错：NameError


#六.ATM模拟系统




















