#一.布尔类型和比较运算符
#   布尔变量定义
is_active = True    #直接赋值
age = 20
is_adult = (age >=18)   #通过比较运算得到布尔值

print(type(is_active))
print(is_active)    #True
print(is_adult)    #True

#   比较运算符示例
a, b = 10, 20
print(a == b)   #False
print(a != b)   #True
print(a < b)    #True
print(a + 10 <= b)  #True


#二.基础if语句
#   场景:判断是否成年
age1 = 16
if age1 >= 18:
    print("你已经成年啦!")
# 输出：无（条件不成立）


# #三.if-else语句
# #   场景:登录验证
# username = input("请输入用户名:")
# password = input("请输入密码:")
#
# if username == "admin" and password == "123456":
#     print("登录成功!")
# else:
#     print("用户名或密码错误!")


#四.if-elif-else组合判断语句
#   场景:成绩评定
score = 85
if score >=90:
    print("优秀!")
elif 80 <= score <90:
    print("良好")
elif 60 <=score <80:
    print("及格")
else:
    print("不及格!")


#五.嵌套if语句
#   场景:网购优惠判断
is_vip = True
total_price = 150

if is_vip:
    if total_price >= 100:
        print("vip用户享受八折优惠")
    else:
        print("vip用户无折扣")
else:
    print("普通用户需满200元才能享受折扣")


#六.结合input的实用案例
#   场景:温度提醒
temperature = float(input("请输入当前温度(℃):"))

if temperature >= 30:
    print("高温预警!建议减少外出")
elif 18 <= temperature < 30:
    print("温度适宜!")
else:
    print("低温注意保暖")



# #       注意事项:
#
# #1.缩进决定代码归属
# # 错误示例：缩进不一致导致逻辑错误
# if True:
#     print("A")
#   print("B")  # IndentationError!
#
# #2.条件顺序影响结果
# # 错误示例：范围判断顺序不当
# num = 75
# if num > 60:
#     print("及格")
# elif num > 80:  # 永远不会执行！
#     print("优秀")
#
# #3.灵活组合条件
# # 使用逻辑运算符 and/or/not
# is_weekend = True
# time = 14
# if is_weekend and 10 <= time <= 22:
#     print("商场营业中")



























