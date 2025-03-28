# 第一个python程序
print('hello world')

#字面量:数字  字符串  列表  元组  集合  字典
a = 10
b = 13.14

name = "lice"
# name1 = "lice"
# name2 = 'lice'


# 单行注释
"""
多行注释1
"""

'''
多行注释2
'''


# 变量:如上面a,b  name1 name2 的就是变量
# a的变量类型为int型   b:float型   name1:str型
print(type(a))
print(type(b))
print(type(name))
# a的变量类型为int型   b:float型   name1:str型

#类型转换
c = float(a)
d = int(b)
print(c)
print(d)

#标识符: sister_age  father_name


# 运算符:
a_b = a+b
print(a_b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

a+=b
print(a)  #此时a=a+b a现在的值为23.14


#字符串
name1 = "lice"
name2 = 'lice'
name3 = """lice"""
print(name1)
print(name2)
print(name3)
# "baidu"
#name4 = '"baidu"'
name4 = "\"baidu\""
print(name4)

#字符串拼接
print("hello"+"\t"+'world')

#字符串格式化
class_num = 57
avg_salary = 16757
message = "python大数据学科,北京%s期,毕业平均工资:%s"%(class_num,avg_salary)
print(message)    #多个变量占位,变量要用括号括起来,并按照占位的顺序填入
#通过占位的形式,完成了数字和字符串的拼接

class_num1 = 57
avg_salary1 = 16757.7
message1 = "python大数据学科,北京%d期,毕业平均工资:%f"%(class_num1,avg_salary1)
print(message1)
#不同变量的占位

#字符串格式化的精度控制
num_1 = 11
num_2 = 11.345
print("数字11的宽度限制5,结果是:%5d"%num_1)
print("数字11的宽度限制1,结果是:%1d"%num_2)
print("数字11.345的宽度限制7,小数精度2,结果是:%7.2f"%num_2)
print("数字11.345不限制宽度,小数精度2,结果是:%.2f"%num_2)

#快速格式化
name_a = "传智播客"
set_up_year = 2006
stock_price = 19.99
print(f"我是{name},我成立于:{set_up_year}年,我今天的股价是:{stock_price}")

#对表达式进行格式化
print("1*1的结果是:%d"%(1*1))
print(f"1*2的结果是:{1*2}")
print("字符串在python中的类型名是:%s"%type("字符串"))


# #数据输入
# print("你是谁")
# my_name = input()
# print(my_name)
#等同于
my_name = input("请告诉我你是谁")
print(my_name)
#输入数字类型
my_num = input("我的银行卡密码是:")
print("你的银行卡密码类型是:",type(my_num))


































