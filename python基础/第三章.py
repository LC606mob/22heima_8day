#一.while循环

#   基础示例:计数器
#打印1~5
count = 1
while count <=5:
    print(count)
    count += 1     #终止条件,防止无限循环

# #避免无限循环
# #   错误示例:缺少终止条件
# while True:
#     print("我在无限循环...")


#二.while循环嵌套
#   打印星号三角形
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end="") #end=""表示不换行
        col += 1
    print() #换行
    row += 1


#三.补充知识点
# print语句输出内容自动换行
print("hello")
print("world")
# 1. 输出不换行 & 制表符 \t &换行符 \n
print("hello",end="")
print("world",end="\t")
print("love",end="\n")
print("python")

#2. 九九乘 法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}×{i}={i*j}", end="\t")  # \t对齐内容
        j += 1
    print()  # 换行
    i += 1


# 四.for循环
#1.遍历字符串统计字符
text = "hello world"
count1 = 0
for char in text:
    if char == "l":
        count1 += 1
print(count1)
#完成内容统计
name1 = "itheima is a brand of itcast"
q = 0
for x in name1:
    if x == "a":
        q += 1
print("一共有%d个a"%q)

#2.range语句
# range语法1 range(num)
for x in range(10):
    # 输出0-9,不包含10
    print(x)
# range语法2 range(num1,num2)
for x in range(5, 10):
    # 输出5-9的一个数字序列,不包含10
    print(x)
# range语法3 range(num1,num2,step)
for x in range(5, 10, 2):
    # 输出5,7,9的一个数字序列,数字间隔为2,不包含10
    print(x)
#   range语法示例
# for num_1 in range(3):
#     print(num_1,end="") # 0,1,2
# print()
# for num_2 in range(2, 5):
#     print(num_2,end="") # 2,3,4
# print()
# for num_3 in range(1, 10, 3):
#     print(num_3,end="")  # 1,4,7
# print()


#五.for循环嵌套
# 小练习
x = 0
for x in range(1, 11):
    print("今天是表白的第%d天"%x)
    for y in range(1, 6):
        print("今天送出的第%d朵玫瑰花"%y)
    print("i love you!")
print(f"第{x}天表白成功!")
# 九九 乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{i}*{j}={i*j}\t",end="")
    print()


#六.continue和break
#   工资发放案例(综合案例)
# 某公司,账户余额有1W元，给20名员工发工资。
# 员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
# 领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
# 如果工资发完了，结束发工资。

# 员工12，绩效分3，低于5，不发工资，下一位。
# 员工13，绩效分1，低于5，不发工资，下一位。
# 员工14，绩效分4，低于5，不发工资，下一位。
# 向员工15发放工资1000元，账户余额还剩余2000元
# 向员工16发放工资1000元，账户余额还剩余1000元
# 员工17，绩效分2，低于5，不发工资，下一位。
# 向员工18发放工资1000元，账户余额还剩余0元
# 工资发完了，下个月领取吧.

# 提示:
# 使用循环对员工依次发放工资
# continue用于跳过员工，break直接结束发工资
# 随机数可以用：import random


money = 10000
#for循环对员工发放工资
for i in range(1, 21):
    import random
    num = random.randint(1,10)
    if num < 5:
        print(f"员工{i},绩效分{num},低于5,不发工资,下一位")
        #continue跳过发放
        continue

    #判断余额足不足
    if money >= 1000:
        money -= 1000
        print(f"员工{i},绩效分{num},发放工资1000,账户余额还剩{money}元")
    else:
        print(f"公司账户还剩{money}元，公司没有余额下个月发放")
        #break结束发放
        break



#       该章节注意事项:

# 1.缩进决定代码归属
# # 错误示例：缩进不一致导致逻辑错误
# for x in range(3):
# print(x)  # IndentationError!

# 2.避免修改循环变量
# # 错误示例：在循环内修改计数器
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         i = 10  # 直接跳过后续循环

# 3.临时变量作用域
# for num in range(3):
#     pass
# print(num)  # 输出: 2（可以访问，但不建议）


















